import discord
import config
import parse_args
import media_commands

async def process(msg):
    await msg.channel.send(msg.content[len(config.PREFIX):])
    args, flags = parse_args.parse(msg.content[len(config.PREFIX):])
    commands = {"play", "pause", "continue"}
    
    # debug
    print("args:")
    print(args)
    print("flags")
    print(flags)

    # valid command (at the moment)
    if args and args[0] in commands:
        await media_commands.execute(msg, args, flags)
        
    # invalid command, nothing is modified
    else:
        await msg.channel.send("invalid command")
    return