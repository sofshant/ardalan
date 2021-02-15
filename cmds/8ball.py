import discord
import random
from discord.ext import commands

class eightball(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(aliases=['8ball', 'eightball'])
    async def _8ball(self, ctx, *, question):
        responses = ['100% yes',
                     'Most probably',
                     'Yes',
                     'I think so',
                     'Maybe',
                     'I have 0 clue, try again?',
                     'I dont think so',
                     'No',
                     'Probably not',
                     '100% no']
        await ctx.send(f'{random.choice(responses)}')

def setup(client):
    client.add_cog(eightball(client))
    
