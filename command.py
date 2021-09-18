import discord
import config

async def process(msg):
    await msg.channel.send(msg.content[len(config.PREFIX):])