import discord
import random
from discord.ext import commands

class networth(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def networth(self, ctx, user: discord.User=None):
        if not user:
            await ctx.send(f'{ctx.author.name} has a networth of **{random.randint(100, 100000)}$**')
        else:
            await ctx.send(f'{user.name} has a networth of **{random.randint(100, 100000)}$**')

def setup(client):
    client.add_cog(networth(client))
