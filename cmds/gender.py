import discord
import random
from discord.ext import commands, tasks


class balls(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def gender(self, ctx, user: discord.User=None):
        responses = ['male',
                     'female',
                     'female',
                     'female',
                     'femboy',
                     'femboy',
                     'femboy',
                     'femboy']
        if not user:
            await ctx.send(f'{ctx.author.name} is a {random.choice(responses)}.')
        else:
            await ctx.send(f'{user.name} is a {random.choice(responses)}.')

def setup(client):
    client.add_cog(balls(client))
