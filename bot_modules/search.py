import discord
import re
import youtube_dl
from requests import get

async def find_videos(arg, message):
    # empty arg
    if (arg.strip() == ""):
        await message.channel.send("Please enter a search parameter")
        return

    # regex thing i stole off the internet to help us filter out websites,
    # because youtube dl doesn't have fun when you enter a website or video
    expression = r"(http(s)?:\/\/.)?(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)"
    if (re.search(expression, arg)):
        await message.channel.send("Please don't put a url here")
        return

    # get the search results
    waiting = await message.channel.send("Fetching search results...")
    with youtube_dl.YoutubeDL({'noplaylist' : 'True'}) as ydl:
        try:
            get(arg)
        except:
            try:
                video = ydl.extract_info(f"ytsearch5:{arg}", download = False)['entries']
            except youtube_dl.utils.DownloadError as e:
                if ("age" in str(e)):
                    await message.channel.send('Unsafe search query!')
                else:
                    await message.channel.send('An error has occured')
        else:
            video = ydl.extract_info(arg, download = 'False')

    empty = True

    # iterate through all the returned videos
    for i in range(min(5, len(video))):
        empty = False
        duration = int(video[i]['duration'])
        hours = duration // 3600
        duration -= hours * 3600
        minutes = duration // 60
        duration -= minutes * 60
        seconds = duration

        # build the embed
        embd = discord.Embed(title = "Search Result " + str(i+1))
        ## check if the video length is over an hour
        if hours:
            embd.add_field(
                name = str(i + 1) + ". " + video[i]['title'],
                value = "[Video Link](" + video[i]['webpage_url'] + ") | Channel: [" + video[i]['uploader'] + "](" + video[i]['uploader_url'] + ")\nDuration: " + str(hours) + "h " + str(minutes) + "m " + str(seconds) + "s\n" + '\n'.join(re.sub(r'\n+', '\n', video[i]['description'][:100]).strip().split('\n')[:3]) + ("..." if len(video[i]['description']) > 100 else ""),
                inline = False
            )
        else:
            embd.add_field(
                name = str(i + 1) + ". " + video[i]['title'],
                value = "[Video Link](" + video[i]['webpage_url'] + ") | Channel: [" + video[i]['uploader'] + "](" + video[i]['uploader_url'] + ")\nDuration: " + str(minutes) + "m " + str(seconds) + "s\n" + '\n'.join(re.sub(r'\n+', '\n', video[i]['description'][:100]).strip().split('\n')[:3]) + ("..." if len(video[i]['description']) > 100 else ""),
                inline = False
            )
        embd.set_thumbnail(url=video[i]['thumbnail'])

        await message.channel.send(embed = embd)

    # if its empty then let them know
    if empty:
        await message.channel.send("No results :(")

    await discord.Message.delete(waiting)
