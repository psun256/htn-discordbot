from youtube_dl import YoutubeDL
from requests import get
import discord
async def find_videos(arg, message):
    ydl_opts = {
        'noplaylist' : 'True'
    }
    with YoutubeDL(ydl_opts) as ydl:
        try:
            get(arg)
        except:
            video = ydl.extract_info(f"ytsearch5:{arg}", download = False)['entries']
        else:
            video = ydl.extract_info(arg, download = 'False')
    ans = ""
    for i in range(min(5, len(video))):
        ans += "**" + str(i + 1) + "." + "**"
        ans += "\n"
        ans += video[i]['title']
        ans += "\n"
        ans += "<" + video[i]['webpage_url'] + ">"
        ans += "\n"
        duration = int(video[i]['duration'])
        minutes = duration // 60
        seconds = duration % 60
        ans += "Duration: " + str(minutes) + " minute(s), " + str(seconds) + " second(s)"
        ans += "\n"
        ans += "\n"
    if not ans:
        await message.channel.send("No results :(")
    else:
        await message.channel.send(ans, allowed_mentions = discord.AllowedMentions(everyone = False))
