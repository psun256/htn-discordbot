import discord
import config
from bot_modules import parse_args
from bot_modules import media_commands
from bot_modules import channel_commands

async def process(msg):
    await msg.channel.send(msg.content[len(config.PREFIX):])
    args, flags = parse_args.parse(msg.content[len(config.PREFIX):])
    mediaCommands = {"play", "pause", "continue"}
    channelCommands = {"join", "leave"}
    # debug
    print("args:")
    print(args)
    print("flags")
    print(flags)

    # if its under media commands
    if args and args[0] in mediaCommands:
        await media_commands.execute(msg, args, flags)
    
    # if its under channel commands
    if args and args[0] in channelCommands:
        await channel_commands.execute(msg, args, flags)
    
    # invalid command, nothing is modified
    else:
        await msg.channel.send("invalid command")
    return
