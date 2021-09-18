import discord
import youtube_dl
import config

# manages the downloading of the video
async def downloadVideo(url, message):
    
    # idk, some options i found online
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        # extract some info from the video
        vidInfo = ydl.extract_info(url, download = False)
        print(vidInfo['duration'])

        # if the video doesn't TLE
        if (vidInfo['duration'] <= config.MAX_DURATION):
            await message.channel.send("Downloading audio")
            ydl.download([url])
            await message.channel.send("Successfully downloaded the audio!")
        
        else:   # TLE
            await message.channel.send("This video is too long! The maximum length is " + str(config.MAX_DURATION))