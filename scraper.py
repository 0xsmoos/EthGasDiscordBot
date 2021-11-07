# -*- coding: utf-8 -*-
# filename          : scraper.py
# description       : Get eth gas prices
# author            : Warren
# email             : warren@secmail.pro
# date              : 03-06-1970
# version           : v1.0
# usage             : python scraper.py
# notes             : find_elements_by_xpath returns a list of elements not just one, so you need iterate over them with a loop or just grab the first one if you believe it to be the only one, which is why I add the [0].
# license           : MIT
# py version        : 3.9.7 (must run on 3.6 or higher)
#==============================================================================
import time
from selenium import webdriver
# from discord.ext import commands

def get_prices():
	driver = webdriver.Chrome()
	driver.minimize_window()
	driver.get('http://www.ethgasnow.com')
	time.sleep(2)
	eth_gas_usd = driver.find_elements_by_xpath("/html/body/div/div/div/section[3]/div/div/div/section/div/div/div/div[2]/div/div/span[2]")[0].text
	mint_usd = driver.find_elements_by_xpath("/html/body/div/div/div/section[8]/div/div/div/section/div/div[1]/div/div[2]/div/span[2]")[0].text
	accept_offer = driver.find_elements_by_xpath("/html/body/div/div/div/section[5]/div/div/div/section/div/div[2]/div/div[2]/div/span[2]")[0].text
	price = ("USD Gas price: $", eth_gas_usd,
		", Minting Price: $", mint_usd,
		", Accept Offer Price: $", accept_offer)
	punctuations = r'''!()-[]{};:'"\<>./?@#%^&*_~'''
	goodPrices = ""
	for char in price:
	   if char not in punctuations:
	       goodPrices = goodPrices + char
	print(goodPrices)
	driver.close()

if __name__ == "__main__":
	get_prices()
