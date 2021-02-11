import discord
from discord.ext import commands

class say(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def say(self, ctx, *, message: commands.clean_content):
        message_components = message.split()
        if "@​everyone" in message_components or "@​here" in message_components:
            await ctx.send("Nice try noob")
            return
        
        await ctx.send(message)

def setup(client):
    client.add_cog(say(client))
