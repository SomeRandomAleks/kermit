import discord
from discord.ext import commands
from discord.ext.commands import Cog
from main import client
import json
import random





class Bank(Cog):

    #@commands.command()
    #async def coinflip(ctx, amnt = None, side = None):
     #   with open('accounts.json', 'r') as file:
      #  	users = json.load(file)

       # if not amnt : await ctx.send("Invalid command. Usage: `!coinflip <amount> <coinside>`")
        #try:
         # accept = int(amnt)
        #except ValueError:
         #   await ctx.send("That didn't work out... have you entered a number?")
          #  return
        #await open_account(ctx.author)

        #users = await get_bank_data()

        #if not side:
         #   await ctx.send("Invalid command. Usage: `!coinflip <amount> <coinside>`")
        #elif not amnt:
         #   await ctx.send("Invalid command. Usage: `!coinflip <amount> <coinside>`")
        #else:
         #   if side in ("heads", "tails"):
          #      if users[str(user.id)]["wallet"] < accept:
           #         await ctx.send("You can't bet more money than you have")
            #    else:
             #       num1 = random.choice(["heads", "tails"])
              #      if num1 != side:
               #         users[str(user.id)]["wallet"] -= accept
                        #embed = discord.Embed#(title=':red_circle: LOSS', description=f'You got **{num1}** and lost {accept} coins', color=0xfd0000)
                        #await ctx.send(embed=embed)
                    #elif num1 == side:
                     #   users[str(user.id)]["wallet"] += accept
                      #  embed = discord.Embed(title=':green_circle: WIN', description=f'You got **{num1}** and won {accept} coins', color=0x00ff0a)
                       # await ctx.send(embed=embed)
            #else:
             #   await ctx.send("Wrong coin side! It can only be `heads` or `tails`")
              #  return
            #with open ("mainbank.json", "w") as f:
              #  json.dump(users,f)

    @commands.command()
    async def make(self, ctx, account):

        if ctx.author.bot:
            return

		# make the account
        if account != "account":
            return
		# return the file
        with open('accounts.json', 'r') as file:
            users = json.load(file)
		
		# check if the user is already in the file
        if str(ctx.author.id) in users:
            await ctx.send(f"{ctx.author.mention}, you already have an account")
            return
		
		# if they aren't in the file then you make an account for them
        with open('accounts.json', 'w') as f:
            users[str(ctx.author.id)] = {}
            users[str(ctx.author.id)]["cash"] = 100
            json.dump(users, f, indent=4)
		
		# send the embed
        embed = discord.Embed(description=f"{ctx.author.mention} is now officially registered and can battle", color=0xe0e024)
        await ctx.send(embed=embed)




	
    @commands.command()
    async def profile(self, ctx, member : discord.Member=None):
        with open('accounts.json', 'r') as file:
            users = json.load(file)
		
        if ctx.author.bot:
            return
		
        try:
            if member.bot:
                await ctx.send(f"Bots can't have accounts")
                return
        except AttributeError:
            pass
		
        if not member:

            if str(ctx.author.id) not in users:
                await ctx.send(f"{ctx.author.mention}, you don't have an account")
                return
            member_new = ctx.author
        else:
            member_new = member
		
            if str(member.id) not in users:
                await ctx.send(f"{member.mention} does not have an account")
                return
		
        member_account = users[str(member_new.id)]



		# making the embed, test embed for now
        embed = discord.Embed(title=f"Profile of {member_new}", 
        description=f"Total HP: {member_account['hp']}", color=0xffa724)
        embed.add_field(name="Wallet", value=member_account['cash'])
        embed.add_field(name="Battles Won", value=member_account['wins'])
        embed.add_field(name="Battles Lost", value=member_account['losses'])
        embed.set_thumbnail(url=member_new.avatar_url)
        await ctx.send(embed=embed)

    #@commands.command()
    #@commands.cooldown(1, 10, commands.BucketType.member)
    #async def beg(self, ctx):

     #   with open('accounts.json', 'r') as file:
      #    users = json.load(file)
		
       # if str(ctx.author.id) not in users:
			  #    await ctx.send(f"{ctx.author.mention}, you don't have an account: `k!make account`")
			      
        #return
        #earnings = random.randrange(


		
		
	#	await ctx.send(
   #         embed = discord.Embed(
    #            title=f"Beg",
     #           description=f"Some person just gave you {earnings} coins",
      #          color=0xffa724
       #     )
        #)
		
		

        #with open ("accounts.json", "w") as f:
			  #users[str(ctx.author.id)]["cash"] += earnings
			  #json.dump(users, f, indent=4)





 



    




	


def setup(client):
	client.add_cog(Bank(Cog)) 