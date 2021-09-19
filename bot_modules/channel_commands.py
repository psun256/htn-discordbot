import config
from . import vc
from . import search

async def execute(msg, args, flags):
    user = msg.author
    channel = msg.channel

    if (args[0] == "join"):
        await join(user, channel)

    elif (args[0] == "leave"):
        await leave(user, channel)

    elif (args[0] == "search"):
        await(initialize_search(msg))

async def join(user, channel):
    if (user.voice):
        if (vc.src != None and vc.src.is_connected()):
            await channel.send("I am in a voice channel already!")
            return

        vc.src = await user.voice.channel.connect()
        await channel.send("I have connected")

    else:   await channel.send("You are not in a vc")

async def leave(user, channel):
    if (vc.src != None and vc.src.is_connected()):
        await vc.src.disconnect()
        await channel.send("I have left the vc")

    else:   await channel.send("I am not in a vc, silly!")

async def initialize_search(msg):
    query = msg.content[len(config.PREFIX):]
    query = query[7:]
    await search.find_videos(query, msg)
