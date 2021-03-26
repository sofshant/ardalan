import discord
from discord.ext import commands, tasks

class purge(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['clear', 'purge', 'prune'])
    @commands.has_permissions(manage_messages = True)
    async def _clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f'cleared {amount} messages')


def setup(client):
    client.add_cog(purge(client))
