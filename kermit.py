import discord
from discord.ext import commands
from discord.ext.commands import Cog
import json


class Fun(Cog):
    async def get_bank_data():
        with open("accounts.json", "r") as f:
            users = json.load(f)
        return users


@commands.command()
async def gifhelp(self, ctx):
    embed = discord.Embed(title='Kermit Gifs', color=0x17FF00)
    embed.add_field(name='Dance', value='Kermit dancing: `k!dance`')
    embed.add_field(name='Fell', value='Send a gif of kermit falling: `k!fell`')
    embed.add_field(name='Striptease', value='Send a gif of kermit making a stripper dance: `k!strip`')
    embed.add_field(name='Panic', value='Send a gif of kermit in panic: `k!panic`')
    embed.add_field(name='Triggered', value='Send a gif of kermit getting triggered: `k!triggered`')
    embed.add_field(name='Yay', value='Send a gif of kermit celebrating: `k!yay`')
    embed.add_field(name='Good morning', value='Send a gif of kermit waking up: `k!gm`')
    embed.add_field(name='Ak47', value='Send a gif of kermit using his AK47: `k!ak47`')

    await ctx.send(embed=embed)

		
@commands.command()
async def no(self, ctx):
    embed = discord.Embed(title ='Nao Nao', color=0x17FF00) 
    embed.set_image(url="https://i.pinimg.com/originals/b9/6d/35/b96d3501377690061fe82bf5103d0e66.gif")
    await ctx.send(embed=embed)
    
@commands.command()
async def ak47(self, ctx):
    embed = discord.Embed(title ='RATATATATATA', color=0x17FF00) 
    embed.set_image(url="https://media.giphy.com/media/xUA7b4HyaSLH07bRo4/giphy.gif")
    await ctx.send(embed=embed)

@commands.command()
async def bot(self, ctx):
    '''Shows info about bot'''
    embed = discord.Embed(color=discord.Color.green())
    embed.title = 'Bot Info'
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.add_field(name="Servers", value=len(bot.guilds))
    embed.add_field(name='Total Users', value=len(bot.users))
    embed.add_field(name="Bot Latency", value=f"{bot.ws.latency * 1000:.0f} ms")
    await ctx.send(embed=embed)

@commands.command()
async def panic(self, ctx):
    embed = discord.Embed(title ='PAAAANIC', color=0xff0000) 
    embed.set_image(url="https://i.imgur.com/IJnxZ3w.gif")
    await ctx.send(embed=embed)

@commands.command()
async def goodmorning(self, ctx):
            embed = discord.Embed(title ='Good Morning', color=0xff0000) 
            embed.set_image(url="https://tenor.com/7dji.gif")
            await ctx.send(embed=embed)

@commands.command()
async def fell(self, ctx):
            embed = discord.Embed(title ='*fells down*', color=0x797979) 
            embed.set_image(url="https://media1.tenor.com/images/523f0a4bddd1c879b13689498bd81c17/tenor.gif")
            await ctx.send(embed=embed)


@commands.command()
async def strip(self, ctx):
        embed = discord.Embed(title ='*Bring out your money*', color=0xfa7234) 
        embed.set_image(url="https://i.pinimg.com/originals/aa/3a/79/aa3a79969c79421a91455da4b2ba3708.gif")
        await ctx.send(embed=embed)

@commands.command()
async def dance(self, ctx):
        embed = discord.Embed(title ='*/dance*', color=0x17FF00) 
        embed.set_image(url="https://media3.giphy.com/media/etOX3h7ApZuDe7Fc5w/giphy-downsized-large.gif")
        await ctx.send(embed=embed)

@commands.command()
async def yay(self, ctx):
        embed = discord.Embed(title ='PARTY TIME', color=0x17FF00) 
        embed.set_image(url="https://i.gifer.com/8z0C.gif")
        await ctx.send(embed=embed)
@commands.command()
async def triggered(self, ctx):
        embed = discord.Embed(title ='kermit triggered', color=0xff0000) 
        embed.set_image(url="https://media.tenor.com/images/fc447b70d1d61962836b0e444964c83b/tenor.gif")
        await ctx.send(embed=embed)

@commands.command()
async def gamehelp(self, ctx):
        embed = discord.Embed(title='Kermit Gifs', color=0x17FF00)
        embed.add_field(name='Dance', value='Send a gif of kermit dancing: `k!dance`')
        embed.add_field(name='Fell', value='Send a gif of kermit falling: `k!fell`')
        await ctx.send(embed=embed)

@commands.command()
async def help(self, ctx):
        embed = discord.Embed(title='Kermit Info', color=0x17FF00, description = "My prefix is k! and K! and I'm a Kermit fun bot :robot:")
        embed.add_field(name='Gaming', value='If you want to see the game commands use: `k!gamehelp`')
        embed.add_field(name='Gifs', value='If you want to see the gif commands use: `k!gifhelp`')
        embed.add_field(name= 'Economy', value= 'If you want to check how my economy works use: `k!economyhelp` ' )
        await ctx.send(embed=embed)









def setup(client):
	client.add_cog(Fun(Cog))

