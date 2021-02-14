import discord
import os
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix = '$')

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

@client.command()
async def ping(ctx):
        await ctx.send(f'**Pong**   {round(client.latency * 1000)} ms')

@client.event
async def on_ready():
    print('Hi stockr \n')

    print('Server list:')
    for guild in client.guilds:
        print(guild.name)


client.run('put your token over here')
