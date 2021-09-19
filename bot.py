import discord
import config
import command

class MyClient(discord.Client):
    async def on_ready(self):
        print('{0} ready to vibe ig'.format(self.user))

    async def on_message(self, message):
        if (message.author.bot): return                 # to ignore bot messages
        if (message.content.startswith(config.PREFIX)):
            await command.process(message)

client = MyClient()
client.run(config.TOKEN)