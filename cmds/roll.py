import discord
import random
from discord.ext import commands

class roll(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['roll', 'dice'])
    async def _roll(self, ctx):
        await ctx.send(f'{ctx.author.name} rolled a {random.randint(1, 6)}')
        await ctx.message.delete()

def setup(client):
    client.add_cog(roll(client))
