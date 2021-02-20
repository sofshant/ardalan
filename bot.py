import discord
import os
from discord.ext import commands, tasks
from dotenv import load_dotenv

client = commands.Bot(command_prefix = '$', help_command=None) #you can change prefix on the $

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cmds.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cmds.{extension}')

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cmds.{extension}')
    client.load_extension(f'cmds.{extension}')

for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        client.load_extension(f'cmds.{filename[:-3]}')

#the ping commmand
@client.command()
async def ping(ctx):
        await ctx.send(f'**Pong**   {round(client.latency * 1000)} ms')

@client.event
async def on_ready():
    print('Bot ready \n')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client.run(TOKEN)
