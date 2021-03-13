# DEFAULT IMPORTS
import random
import json
import os

# EXTRA IMPORTS
from extra.webserver import keep_alive
import discord
from discord.ext import commands
import asyncio
from kermit import *

# COG IMPORTS
from cogs.bank import *





intents = discord.Intents.all()
intents.members = True


client = commands.Bot(command_prefix=('k!', 'K!'), intents=intents)
client.remove_command('help')

@client.listen('on_message')
async def empty(message):
	if message.content == "k!" or message.content == "K!":
		await message.channel.send("You need me?")
	else:
		pass



# COG EXTENSIONS
client.load_extension('cogs.bank')
client.load_extension('kermit')
client.load_extension('cars')




@client.event
async def on_ready():
    print("Running")
    activity = discord.Game(name="Kermit.exe")
    await client.change_presence(activity=discord.Streaming(name="Kermit da frog", url="https://www.youtube.com/watch?v=zpmrAdM4D8w"))


keep_alive()
#TOKEN = os.environ.get("DISCORD_BOT_SECRET")
#print(TOKEN)
client.run('ODE2Njg0OTI2MzAzNzMxNzMy.YD-jGw.Om-H7F9sIWrQfuBXVp9b_m3F0UM') 



