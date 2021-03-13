# import discord
# from discord.ext import commands
# from discord.ext.commands import Cog

# class BattleCog(Cog):

# 	def __init__(self, client):
# 		member = ""
		

# 	@commands.command()
# 	async def battle(self, ctx, member : discord.Member=None, amount=None):
# 		if ctx.author.bot:
# 			return
# 		elif not member:
# 			await ctx.send(f"{ctx.author.mention}, you have not picked anyone to battle with")
# 			return
# 		elif not amount:
# 			await ctx.send(f"{ctx.author.mention}, you have not picked an amount to battle with")
# 			return
# 		elif not isinstance(amount, int):
# 			await ctx.send(f"{ctx.author.mention}, your amount is not a number/integer")
# 			return
# 		elif member.bot:
# 			await ctx.send("Bots can't battle")
		
		
# 		with open('accounts.json', 'r') as f:
# 			users = json.load(f)
# 		if str(message.author.id) not in users:
# 			await ctx.send(f"{message.author.mention}, you don't have an account to battle with")
		
# 		await ctx.send(f"Great! {member.mention} do you want to battle with {ctx.author.mention} for {int}")
	
# 	@Cog.listener()
# 	async def on_message(message):
# 		if member != str(message.author.id) or agreement:
# 			return
		
		
		

		
		
		


