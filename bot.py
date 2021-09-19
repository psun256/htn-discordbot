import discord
import config
import command

class htn2021(discord.Client):
    # lets you know in the console once its logged on and ready
    async def on_ready(self):
        print('{0} ready to vibe ig'.format(self.user))

    async def on_message(self, message):
        # ignores bot messages
        if (message.author.bot): return

        # where all the magic begins (lets code know its a command, and will process it)
        if (message.content.startswith(config.PREFIX)):
            await command.process(message)

# run
client = htn2021()
client.run(config.TOKEN)