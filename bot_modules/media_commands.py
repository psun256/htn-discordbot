import discord
import youtube_dl
from . import vc

def isnumber(str):
    dig = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    return all([c in dig for c in str])

async def execute(msg, args, flags):
    user = msg.author
    channel = msg.channel

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
    vc.src.stop()
    vol = 100

    if ("youtube.com/watch?v=" in args[1]):

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
                if not flag[1]:
                    flag[1] = "0"
                if not isnumber(flag[1]):
                    await channel.send("Enter a positive integer for the volume")
                    return
                if int(flag[1]) > 100:
                    await channel.send("Between 0 and 100 please")
                    return
                await channel.send("Playing the video at volume " + flag[1])
                vol = int(flag[1])

        with youtube_dl.YoutubeDL({}) as ydl:
            song = ydl.extract_info(args[1], download=False)
            
        vc.src.play(discord.FFmpegPCMAudio(song["formats"][0]["url"]))
        vc.src.source = discord.PCMVolumeTransformer(vc.src.source, volume = (vol/100))

async def pause(channel):
    if (not vc.src.is_playing()):   
        await channel.send("Already not playing")
        return
    vc.src.pause()

async def resume(channel):
    if (vc.src.is_playing()):   
        await channel.send("Already playing")
        return
    vc.src.resume()

async def stop(channel):
    if (not vc.src.is_playing()):   
        await channel.send("Already not playing")
        return
    vc.src.stop()

async def volume(channel, args):
    if (not vc.src.is_playing()):   
        await channel.send("Nothing is playing")
        return

    vol = 100

    if (len(args) >= 2):
        args[1] = args[1].lstrip("0")
        
        if (isnumber(args[1])):
            vol = int(args[1])
            await channel.send("Set the volume to " + str(vol) + " percent of previous level")
            vc.src.source = discord.PCMVolumeTransformer(vc.src.source, volume = (vol/100))

        else:
            await channel.send("Enter a positive integer for the volume (the percentage you want to make it louder or quieter)")
            return