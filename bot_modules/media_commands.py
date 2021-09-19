import discord
import youtube_dl
from . import vc

# custom function to determine if a string is an integer since built in functions were sus
def isnumber(str):
    dig = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    return all([c in dig for c in str])

async def execute(msg, args, flags):
    channel = msg.channel

    # tells the user to run the join command before using the media commands
    if (vc.src == None or not vc.src.is_connected()):
        await channel.send("Run the join command first")
        return

    if (args[0] == "play"):
        await play(args, flags, channel)

    if (args[0] == "pause"):
        await pause(channel)

    if (args[0] == "continue"):
        await resume(channel)

    if (args[0] == "stop"):
        await stop(channel)

    if (args[0] == "volume"):
        await volume(channel, args)

async def play(args, flags, channel):
    vol = 100

    # if there are enough arguments (so its a good link)
    if (len(args) >= 2 and "youtube.com/watch?v=" in args[1]):

        # parse flags (volume is the only one)
        if (flags):
            flag = flags[0].split(":")

            # if we do not have 2 tokens after splitting then the flag is formatted incorrectly
            if (len(flag) != 2):
                await channel.send("Invalid flag format")
                return

            # if the flag doesn't start with the proper volume flag synatax
            if (flag[0] != "-v"):
                await channel.send("Invalid flag format")
                return

            else:
                flag[1] = flag[1].lstrip("0")

                ## in case flag[1] = 0
                if (not flag[1]):
                    flag[1] = "0"

                if (not isnumber(flag[1])):
                    await channel.send("Enter a positive integer for the volume")
                    return

                if (int(flag[1]) > 200 or int(flag[1]) < 1):
                    await channel.send("Between 1 and 200 please")
                    return

                vol = int(flag[1])

        # stops all existing audio sources
        vc.src.stop()

        waiting = await channel.send("Processing request...")
        
        # extract source info from url
        with youtube_dl.YoutubeDL({}) as ydl:
            song = ydl.extract_info(args[1], download=False)

        # play the audio at the proper volume
        vc.src.play(discord.FFmpegPCMAudio(song["formats"][0]["url"]))
        await discord.Message.delete(waiting)
        vc.src.source = discord.PCMVolumeTransformer(vc.src.source, volume = (vol/100))
        await channel.send("Playing the video at volume level " + str(vol))
    
    # if they didn't enter enough arguments
    else: await channel.send("Please enter something valid")

async def pause(channel):
    if (not vc.src.is_playing()):
        await channel.send("Already not playing")
        return

    await channel.send("Paused")
    vc.src.pause()

async def resume(channel):
    if (vc.src.is_playing()):
        await channel.send("Already playing")
        return

    await channel.send("Resumed")
    vc.src.resume()
    
async def stop(channel):
    if (not vc.src.is_playing()):
        await channel.send("Already not playing")
        return

    await channel.send("Stopped")
    vc.src.stop()

async def volume(channel, args):
    if (not vc.src.is_playing()):
        await channel.send("Nothing is playing")
        return

    vol = 100

    # parse volume control arguments (is integer, and is within range)
    if (len(args) >= 2):
        args[1] = args[1].lstrip("0")

        if (isnumber(args[1])):
            vol = int(args[1])

            if (int(args[1]) > 200 or int(args[1]) < 1):
                await channel.send("Between 1 and 200 please")
                return

            vc.src.source = discord.PCMVolumeTransformer(vc.src.source, volume = (vol/100))
            await channel.send("Set the volume to " + str(vol) + " percent of previous level")

        else:
            await channel.send("Enter a positive integer for the volume (the percentage you want to make it louder or quieter)")
            return
