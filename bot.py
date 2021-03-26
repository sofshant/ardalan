import discord
import os
from discord.ext import commands, tasks
from dotenv import load_dotenv

client = commands.Bot(command_prefix = '$', help_command=None) #you can change prefix on the $

#simple error handler
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.UserNotFound):
        await ctx.send("couldn't find that user.")
        return
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You arent allowed to do that!")
        return
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('You are missing required arguments! Type "$help" for help')
        return
    if isinstance(error, commands.CommandNotFound):
        return
    if isinstance(error, commands.CommandError):
        await ctx.send("Something went wrong.")
        print(error)

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

#ping command
@client.command()
async def ping(ctx):
        await ctx.send(f'**Pong** {round(client.latency * 1000)} ms')

@client.event
async def on_ready():
    print('Hi stockr \n')

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client.run(TOKEN)
