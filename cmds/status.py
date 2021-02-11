import discord
import os
from discord.ext import commands, tasks
from itertools import cycle

class status(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.status = cycle(['A | https://sofshant.club/', 'Ar | https://sofshant.club/', 'Ard | https://sofshant.club/', 'Arda | https://sofshant.club/', 'Ardal | https://sofshant.club/', 'Ardala | https://sofshant.club/', 'Ardalan | https://sofshant.club/', 'Ardala | https://sofshant.club/', 'Ardal | https://sofshant.club/', 'Arda | https://sofshant.club/', 'Ard | https://sofshant.club/', 'Ar | https://sofshant.club/'])
        print("status loaded")

    @tasks.loop(seconds=3.0)
    async def change_status(self):
        await self.client.change_presence(activity=discord.Game(next(self.status)))
        
    @commands.Cog.listener()
    async def on_ready(self):
        await self.client.wait_until_ready()
        self.change_status.start()

def setup(client):
    client.add_cog(status(client))