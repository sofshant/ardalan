import discord
import asyncio
from discord.ext import commands

class mute(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def mute(self, ctx, user : discord.Member, duration = 0,*, unit = None):
        roleobject = discord.utils.get(ctx.message.guild.roles, id=809178860229885954)
        await ctx.send(f":white_check_mark: Muted {user} for {duration}{unit}")
        await user.add_roles(roleobject)
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
        await user.remove_roles(roleobject)
        await ctx.send(f":white_check_mark: {user} was unmuted")    


def setup(client):
    client.add_cog(mute(client))
