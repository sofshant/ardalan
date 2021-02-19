import discord
from discord.ext import commands

class responses(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if 'sofshant' in message.content.lower():
            await message.channel.send('aha sofshant is very hot')



def setup(client):
    client.add_cog(responses(client))
