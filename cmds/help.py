import discord

from discord.ext import commands

class help(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(
            title = 'Ardalan Bot Help Commands',
            description = 'Help commands. Use prefix ($) before every command. words inside [] can be ignored, words inside {} must be included.',
            colour = discord.Colour.purple()
        )
        embed.set_footer(text='Made with ♡ by sofshant')
        embed.set_author(name='Arda Bot',
        icon_url='https://i.imgur.com/4g02jKo.png')
        embed.add_field(name='help', value='the command you just used', inline=False)
        embed.add_field(name='ping', value='shows bot latency', inline=True)
        embed.add_field(name='ban {user} [reason]', value='bans user', inline=False)
        embed.add_field(name='unban {user+discrim}', value='unbans user', inline=False)
        embed.add_field(name='kick {user} [reason]', value='kicks user', inline=False)
        embed.add_field(name='nuke', value='nukes channel', inline=False)
        embed.add_field(name='purge [message amount]', value='deletes bulk messages', inline=False)
        embed.add_field(name='say {message}', value='repeats any message', inline=False)
        embed.add_field(name='ping', value='shows bot latency', inline=False)
        embed.add_field(name='8ball {question}', value='anwsers question', inline=False)
        embed.add_field(name='dice', value='rolls dice', inline=False)
        embed.add_field(name='networth [user]', value='shows networth', inline=False)
        embed.add_field(name='iq [user]', value='shows iq', inline=False)
        embed.add_field(name='brain [user]', value='shows brain size', inline=False)
        embed.add_field(name='braincells [user]', value='shows braincells', inline=False)
        embed.add_field(name='balls [user]', value='shows ball size', inline=False)
        embed.add_field(name='gender [user]', value='shows gender', inline=False)

    
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(help(client))
        
