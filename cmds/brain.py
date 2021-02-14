import discord
import random
from discord.ext import commands, tasks


class brain(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['brain', 'brainsize'])
    async def _brain(self, ctx, user: discord.User=None):
        responses = ['incredibly tiny',
                     'very very small',
                     'super small',
                     'non existant',
                     'non existant',
                     'non existant',
                     'incredibly tiny',
                     'super small',
                     'small',
                     'small',
                     'normal sized',
                     'kinda big',
                     'large',
                     'huge',
                     'insanely massive']
        if not user:
            await ctx.send(f'{ctx.author.name} has a {random.choice(responses)} brain.')
        else:
            await ctx.send(f'{user.name} has a {random.choice(responses)} brain.')

def setup(client):
    client.add_cog(brain(client))
