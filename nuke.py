import discord
from discord.ext import commands

class nuke(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def nuke(self, ctx):
        pos = ctx.channel.position
        await ctx.channel.delete(reason="nuke")
        channel = await ctx.channel.clone(reason="nuke")
        await channel.edit(position=pos)
        await channel.send("Nuked the channel")
        

def setup(client):
    client.add_cog(nuke(client))
