# -*- coding: utf-8 -*-
# filename          : bot.py
# description       : Get eth gas prices thru discord
# author            : Warren
# email             : warren@secmail.pro
# date              : 03-06-1970
# version           : v1.0
# usage             : python bot.py
# notes             :
# license           : MIT
# py version        : 3.9.7 (must run on 3.6 or higher)
#==============================================================================
from discord.ext import commands
import scraper
token = ''

bot = commands.Bot(command_prefix="~")

@bot.command()
async def getgas(ctx):
	price = scraper.get_prices()
	await ctx.send(price)
bot.run(token)

if __name__ == "__main__":
	bot.run(token)