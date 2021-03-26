import discord
import random
from discord.ext import commands

class braincells(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def braincells(self, ctx, user: discord.User=None):
        if not user:
            await ctx.send(f'{ctx.author.name} has {random.randint(1, 10000)} brain cells')
        else:
            await ctx.send(f'{user.name} has an iq of {random.randint(1, 10000)} brain cells')

def setup(client):
    client.add_cog(braincells(client))
