import discord

async def execute(msg, args, flags):
    user = msg.author
    channel = msg.channel

    if (args[0] == "help"):
        embed = discord.Embed(
            title = "Media Commands"
        )

        embed.add_field(name="Pause", value="Pauses whatever is currently playing", inline=True)

        embed.add_field(name="Continue", value="Continue playing the music after a pause", inline=True)

        embed.add_field(name="Stop", value="Stops whatever is currently playing", inline=True)

        embed.add_field(name="Volume", value="Change volume of the music", inline=True)

        embed.add_field(name="Play", value="Plays a certain video (from a YouTube link)", inline=True)

        await channel.send(embed=embed)



        embed2 = discord.Embed(
            title = "Channel Commands"
        )

        embed2.add_field(name="Join", value="Makes the bot join the voice channel you are currently in", inline=True)

        embed2.add_field(name="Leave", value="Disconnects the the bot from any voice channel", inline=True)

        embed2.add_field(name="Search", value="Returns the top 5 search results for a given keyword", inline=True)

        await channel.send(embed=embed2)



        embed3 = discord.Embed(
            title = "Run the help command followed by another command to learn more about the command"
        )

        await channel.send(embed=embed3)
