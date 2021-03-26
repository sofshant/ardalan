import discord
from discord.ext import commands

class nuke(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def nuke(self, ctx):
        try:
            pos = ctx.channel.position
            await ctx.channel.delete(reason="nuke")
            channel = await ctx.channel.clone(reason="nuke")
            await channel.edit(position=pos)
            await channel.send("Nuked the channel")
        except discord.Forbidden:
            await ctx.send("I dont have the manage channels permission to do that!")

def setup(client):
    client.add_cog(nuke(client))
