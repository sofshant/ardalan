import discord
import asyncio
from discord.ext import commands

class mute(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def mute(self, ctx, user : discord.Member, duration = 0, unit = None):
        role = discord.utils.get(ctx.guild.roles, name="ardamute")
        if not role:
            try:
                muted = await ctx.guild.create_role(name="ardamute", reason="mute role")
                for channel in ctx.guild.channels:
                    await channel.set_permissions(ardamute, send_messages=False)
            except discord.Forbidden:
                return await ctx.send("I have no permissions to make a muted role")

        ardamute = discord.utils.get(ctx.message.guild.roles, id=809178860229885954)
        await ctx.send(f"Muted {user.mention} for {duration}{unit}")
        await user.add_roles(ardamute)
        if unit == "s":
            wait = 1 * duration
            await asyncio.sleep(wait)
        elif unit == "m":
            wait = 60 * duration
            await asyncio.sleep(wait)
        elif unit == "h":
            wait = 60 * duration * 60
            await asynco.sleep(wait)
        elif unit == "d":
            wait = 60 * duration * 60 * 24
            await asynco.sleep(wait)
        elif unit == "":
            wait = 60 * 15
            await asynco.sleep(wait)
            
        await user.remove_roles(ardamute)

        


def setup(client):
    client.add_cog(mute(client))
