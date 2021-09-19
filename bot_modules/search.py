import discord
import re
from youtube_dl import YoutubeDL
from requests import get

ydl_opts = {
    'noplaylist' : 'True',
    'nopremiere' : 'True'
}

async def find_videos(arg, message):
    # empty arg
    if (arg.strip() == ""):
        await message.channel.send("Please enter a search parameter")
        return
    
    # regex thing i stole off the internet to help us filter out websites,
    # because youtube dl doesn't have fun when you enter a website or video
    expression = "(http(s)?:\\/\\/.)?(www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{2,256}\\.[a-z]{2,6}\\b([-a-zA-Z0-9@:%_\\+.~#?&//=]*)"
    if (re.search(expression, arg)):
        await message.channel.send("Please don't put a url here")
        return

    # get the search results
    waiting = await message.channel.send("Fetching search results...")
    with YoutubeDL(ydl_opts) as ydl:
        try:
            get(arg)
        except:
            video = ydl.extract_info(f"ytsearch5:{arg}", download = False)['entries']
        else:
            video = ydl.extract_info(arg, download = 'False')

    # create embed
    empty = True

    for i in range(min(5, len(video))):

        empty = False
        duration = int(video[i]['duration'])
        minutes = duration // 60
        seconds = duration % 60

        # build the embed
        embd = discord.Embed(title = "Search Result " + str(i+1))
        
        embd.add_field(name = str(i + 1) + ". " + video[i]['title'],
        value = "[Video Link](" + video[i]['webpage_url'] + ") | Channel: [" + video[i]['uploader'] + "](" + video[i]['uploader_url'] + ")\nDuration: " + str(minutes) + "m " + str(seconds) + "s" + '\n' + re.sub(r'\n+', '\n', video[i]['description'][:100]).strip() + ("..." if len(video[i]['description']) > 100 else ""),
        inline = False
        )

        embd.set_thumbnail(url=video[i]['thumbnail'])

        await message.channel.send(embed = embd, allowed_mentions = discord.AllowedMentions(everyone = False))
        
    if empty:
        await message.channel.send("No results :(")

    await discord.Message.delete(waiting)
        
  
