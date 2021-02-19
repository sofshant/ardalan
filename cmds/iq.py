import discord
import random
from discord.ext import commands

class iq(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def iq(self, ctx, user: discord.User=None):
        if not user:
            await ctx.send(f'{ctx.author.name} has an iq of {random.randint(1, 200)}')
        else:
            await ctx.send(f'{user.name} has an iq of {random.randint(1, 200)}')

def setup(client):
    client.add_cog(iq(client))
