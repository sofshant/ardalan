import discord
from discord.ext import commands

class kick(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member:discord.User=None, reason =None):
        if member == ctx.message.author:
            await ctx.channel.send("You cant kick yourself")
            return
        if member == None:
            await ctx.channel.send("Who do you want to kick")
            return
        if reason == None:
            reason = "No reason provided"
        message = f"You have been kicked from: {ctx.guild.name} for: {reason}"
        await member.send(message)
        await ctx.guild.kick(member, reason=reason)
        await ctx.channel.send(f"kicked {member.mention}")
        

def setup(client):
    client.add_cog(kick(client))
