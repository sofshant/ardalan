import discord
from discord.ext import commands

class ban(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='ban')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member:discord.User=None, reason =None):
        try:
            if member == ctx.message.author:
                await ctx.channel.send("You cant ban yourself")
                return
            if member == None:
                await ctx.channel.send("Who do you want to ban")
                return
            if reason == None:
                reason = "No reason provided"
            await ctx.guild.ban(member, reason=reason)
            await ctx.channel.send(f"Banned {member.mention}")
        except discord.Forbidden:
            await ctx.send("I dont have the ban permission to do that!")

def setup(client):
    client.add_cog(ban(client))
