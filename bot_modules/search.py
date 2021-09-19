import discord
import re
import youtube_dl
import requests

async def find_videos(arg, message):
    # empty arg
    if (arg.strip() == ""):
        await message.channel.send("Please enter a search parameter")
        return

    # get the search results
    waiting = await message.channel.send("Fetching search results...")
    with youtube_dl.YoutubeDL({'noplaylist' : 'True'}) as ydl:
        try:
            # tests if its a link ##############
            requests.get(arg)
            discord.Message.delete(waiting)
            await message.channel.send("Please do not enter a URL")
            return

        except requests.exceptions.MissingSchema as e:
            # try to search for the video
            try:
                video = ydl.extract_info(f"ytsearch5:{arg}", download = False)['entries']
               
			# if something went wrong, and output why (or try to)
            except youtube_dl.utils.DownloadError as e:
                if ("age" in str(e)):
                    await channel.send("The video is flagged as inappropriate")
					await discord.Message.delete(waiting)
                    return
				
                elif ("unavailable" in str(e)):
                    await channel.send("The video is unavailable")
					await discord.Message.delete(waiting)
                    return
                
                elif ("Premieres" in str(e)):
                    await channel.send("Cannot play premieres")
					await discord.Message.delete(waiting)
                    return
                
                else:
                    await channel.send("An error occurred")
					await discord.Message.delete(waiting)
                    return

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
        embd.add_field(
            name = str(i + 1) + ". " + video[i]['title'],
            value = "[Video Link](" + video[i]['webpage_url'] + ") | Channel: [" + video[i]['uploader'] + "](" + video[i]['uploader_url'] + ")\nDuration: " + (str(hours) + "h ") if hours else "" +  str(minutes) + "m " + str(seconds) + "s\n" + '\n'.join(re.sub(r'\n+', '\n', video[i]['description'][:100]).strip().split('\n')[:3]) + ("..." if len(video[i]['description']) > 100 else ""),
            inline = False
        )
        embd.set_thumbnail(url=video[i]['thumbnail'])

        await message.channel.send(embed = embd)

    # if its empty then let them know
    if empty:
        await message.channel.send("No results :(")

    await discord.Message.delete(waiting)
