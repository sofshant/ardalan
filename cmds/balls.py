import discord
import random
from discord.ext import commands, tasks


class balls(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['balls', 'ballsize'])
    async def _balls(self, ctx, user: discord.User=None):
        responses = ['incredibly tiny balls',
                     'very very small balls',
                     'super small balls',
                     'non existant balls',
                     'non existant balls',
                     'non existant balls',
                     'incredibly tiny balls',
                     'super small balls',
                     'small balls',
                     'small balls',
                     'normal sized balls',
                     'kinda big balls',
                     'large balls',
                     'huge balls',
                     'insanely massive balls']
        if not user:
            await ctx.send(f'{ctx.author.name} has {random.choice(responses)}.')
        else:
            await ctx.send(f'{user.name} has {random.choice(responses)}.')


def setup(client):
    client.add_cog(balls(client))
