import discord
from discord.ext import commands

class ban(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='ban')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member:discord.User=None, reason =None):
        if member == ctx.message.author:
            await ctx.channel.send("You cant ban yourself")
            return
        if member == None:
            await ctx.channel.send("Who do you want to ban")
            return
        if reason == None:
            reason = "No reason provided"
        message = f"You have been banned from: {ctx.guild.name} for: {reason}"
        await member.send(message)
        await ctx.guild.ban(member, reason=reason)
        await ctx.channel.send(f"Banned {member.mention}")
        

def setup(client):
    client.add_cog(ban(client))
