import discord
from discord.ext import commands
from main import client
from discord.ext.commands import Cog
import asyncio
import random


class Cars(Cog):

	@commands.command()
	async def cars(self, ctx):
		await ctx.send(
			embed=discord.Embed(
				title="Cars 🚦",
				description=f"{ctx.author.mention} is playing cars!",
				color=0xffa724
			)
		)
		await asyncio.sleep(2)
		efficiency = [
			"Driving...",
			"Driving...",
			"Driving...",
			"Driving...",
			"Driving...",
			"Driving...",
			"Driving...",
			"Driving...",
			"Driving...",
			"Driving...",
			"Driving...",
			"Driving...",
			f"Oh no, {ctx.author.mention} didn't keep their eyes on the road and crashed!",
			f"Oh no, {ctx.author.mention} went too fast and got arrested by a police officer!",
			f"Oh no, {ctx.author.mention} hit a tree!",
			f"Oh no, {ctx.author.mention} got murdered by a squirrel on the highway!",
			f"Oh no, {ctx.author.mention} got lost and died of thirst!",
			f"{ctx.author.mention} successfully went on a car trip and came back unscathed!"
		]
		await ctx.send("Driving...")
		await asyncio.sleep(3)
		while True:
			msg = random.choice(efficiency)
			if msg != "Driving...":
				await ctx.send(msg)
				break
			await ctx.send(msg)
			await asyncio.sleep(3)
	

def setup(client):
	client.add_cog(Cars(client))