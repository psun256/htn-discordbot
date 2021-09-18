import discord
import config
import command

class MyClient(discord.Client):
    async def on_ready(self):
        print('{0} ready to vibe ig'.format(self.user))

    async def on_message(self, message):
        if (message.author.bot): return


client = MyClient()
client.run(config.TOKEN)