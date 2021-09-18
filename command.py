import discord
import ydl
import config

async def process(message):
    # just testing to see if input is handled properly
    await message.channel.send(message.content[len(config.PREFIX):])
    await ydl.downloadVideo(message.content[len(config.PREFIX):], message)