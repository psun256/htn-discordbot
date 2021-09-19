import discord

audio = None

async def execute(msg, args, flags): 
    user = msg.author
    channel = msg.channel

    if (args[0] == "join"):
        await join(user, channel)
    
    elif (args[0] == "leave"):
        await leave(user, channel)

async def join(user, channel):
    global audio
    if (user.voice):
        audio = await user.voice.channel.connect()

    else:   await channel.send("You are not in a vc")

async def leave(user, channel):
    global audio
    if (audio != None and audio.is_connected()):
        await audio.disconnect()
        await channel.send("I have left the vc")

    else:   await channel.send("I am not in a vc, silly!")
    