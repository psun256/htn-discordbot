import discord
import ydl
import config
import parse_args

async def process(msg):
    await msg.channel.send(msg.content[len(config.PREFIX):])
    args, flags = parse_args.parse(msg.content[len(config.PREFIX):])
    print("args:")
    print(args)
    print("flags")
    print(flags)