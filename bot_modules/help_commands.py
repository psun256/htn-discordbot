import discord
import config

async def execute(msg, args, flags):
    channel = msg.channel

    if (len(args) == 1 and args[0] == "help"):
        
        # help command (general help)
        embed3 = discord.Embed(title = "Run the help command followed by another command to learn more about the command. In the examples given for the commands, mandatory arguments are indicated with <>, and optional arguments are indicated with ().")
        await channel.send(embed=embed3)

        embed = discord.Embed(title = "Media Commands")
        embed.add_field(name="Pause", value="Pauses whatever is currently playing", inline=True)
        embed.add_field(name="Continue", value="Continue playing the music after a pause", inline=True)
        embed.add_field(name="Stop", value="Stops whatever is currently playing", inline=True)
        embed.add_field(name="Volume", value="Changes the volume of the music", inline=True)
        embed.add_field(name="Play", value="Plays a certain video (from a YouTube link)", inline=True)
        await channel.send(embed=embed)

        embed2 = discord.Embed(title = "Channel Commands")
        embed2.add_field(name="Join", value="Makes the bot join the voice channel you are currently in", inline=True)
        embed2.add_field(name="Leave", value="Disconnects the the bot from any voice channel", inline=True)
        embed2.add_field(name="Search", value="Returns the top 5 search results for a given keyword", inline=True)
        await channel.send(embed=embed2)

    # help commands for the specific commands
    # --------------------------------------------------------------------------------
    elif (len(args) == 2 and args[1] == "pause"):
        embed = discord.Embed(title = "Pause",description = "Pauses whatever is currently playing")
        embed.add_field(name="Usage", value= "``" + config.PREFIX + "pause``", inline=True)
        await channel.send(embed=embed)

    elif (len(args) == 2 and args[1] == "continue"):
        embed = discord.Embed(title = "Continue",description = "Continue playing the music after a pause")
        embed.add_field(name="Usage", value= "``" + config.PREFIX + "continue``", inline=True)
        await channel.send(embed=embed)

    elif (len(args) == 2 and args[1] == "stop"):
        embed = discord.Embed(title = "Stop",description = "Stops whatever is currently playing")
        embed.add_field(name="Usage", value= "``" + config.PREFIX + "stop``", inline=True)
        await channel.send(embed=embed)

    elif (len(args) == 2 and args[1] == "join"):
        embed = discord.Embed(title = "Join",description = "Makes the bot join the voice channel you are currently in")
        embed.add_field(name="Usage", value= "``" + config.PREFIX + "join``", inline=True)
        await channel.send(embed=embed)

    elif (len(args) == 2 and args[1] == "leave"):
        embed = discord.Embed(title = "Leave",description = "Disconnects the the bot from any voice channel")
        embed.add_field(name="Usage", value= "``" + config.PREFIX + "leave``", inline=True)
        await channel.send(embed=embed)

    elif (len(args) == 2 and args[1] == "volume"):
        embed = discord.Embed(title = "Volume",description = "Changes the volume of the music")
        embed.add_field(name="Usage", value= "``" + config.PREFIX + "volume <percentage>``", inline=True)
        embed.add_field(name="Percentage", value= "The percentage you want to change the volume by (between 1 and 200)", inline=False)
        embed.add_field(name="Example 1", value="``" + config.PREFIX + "volume 200`` (makes the volume twice as loud)")
        embed.add_field(name="Example 2", value = "``" + config.PREFIX + "volume 50`` (makes the volume half as loud)")
        await channel.send(embed=embed)

    elif (len(args) == 2 and args[1] == "play"):
        embed = discord.Embed(title = "Play",description = "Plays a certain video (from a YouTube link)")
        embed.add_field(name="Usage", value= "``" + config.PREFIX + "play <link> (-v:volume)``", inline=True)
        embed.add_field(name="Link", value= "The link of the video that you want to be played", inline=False)
        embed.add_field(name="Volume (optional)", value= "The volume you want the video to be played at (between 1 and 200)", inline=False)
        embed.add_field(name="Example 1", value = "``" + config.PREFIX + "play https://www.youtube.com/watch?v=dQw4w9WgXcQ``")
        embed.add_field(name="Example 2", value = "``" + config.PREFIX + "play https://www.youtube.com/watch?v=dQw4w9WgXcQ -v:150`` (plays the video at 150% volume)")
        await channel.send(embed=embed)

    elif (len(args) == 2 and args[1] == "search"):
        embed = discord.Embed(title = "Search",description = "Returns the top 5 search results for a given keyword")
        embed.add_field(name="Usage", value= "``" + config.PREFIX + "search <keywords>``", inline=True)
        embed.add_field(name="Keywords", value= "Any keywords you want to search for", inline=False)
        embed.add_field(name="Example", value = "``" + config.PREFIX + "search among us trap remix``")
        await channel.send(embed=embed)