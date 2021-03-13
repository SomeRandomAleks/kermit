import discord
from discord.ext import commands
from discord.ext.commands import Cog

class EmptyPrefix(Cog):

	@Cog.listener()
	async def empty(message):
		if message.content == 'k!' or message.content == 'K!':
			await message.channel.send("Do you need me?")
	

def setup(client):
	client.add_cog(EmptyPrefix(Cog))
