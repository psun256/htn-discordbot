import config
from bot_modules import parse_args
from bot_modules import media_commands
from bot_modules import channel_commands
from bot_modules import help_commands

async def process(msg):
    # debug
    #await msg.channel.send(msg.content[len(config.PREFIX):])

    # parse
    args, flags = parse_args.parse(msg.content[len(config.PREFIX):])

    # the commands
    mediaCommands = {"play", "pause", "continue", "stop", "volume"}
    channelCommands = {"join", "leave", "search"}
    helpCommands = {"help"}

    # debug
    #print("args:")
    #print(args)
    #print("flags")
    #print(flags)

    # if its under the respective category, then run for that respective category
    # --------------------------------------------------------------------------------

    if args and args[0] in mediaCommands:
        await media_commands.execute(msg, args, flags)

    elif args and args[0] in channelCommands:
        await channel_commands.execute(msg, args, flags)

    elif args and args[0] in helpCommands:
        await help_commands.execute(msg, args, flags)


    # invalid command, nothing is modified
    else:
        await msg.channel.send("Invalid command, try again")
    return
