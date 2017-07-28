import discord
from discord.ext.commands import Bot
from discord.ext import commands
import os
import asyncio
import random

Client = discord.Client()


@Client.event
async def on_ready():
	print ("Bot Online!")
	print ("Name: {}".format(Client.user.name))
	print ("ID: {}".format(Client.user.id))

@Client.event
async def on_message(message): # Event for whenever a message is sent to a channel on booty bot's server
	if(message.content.startswith("?meme")):
		imgList = os.listdir('/Users/craigrondinelli/Desktop/EVERYTHING/HoTS MAY MAYS/')
		imgString = random.choice(imgList)
		path = '/Users/craigrondinelli/Desktop/EVERYTHING/HoTS MAY MAYS/' + imgString
		msg = await Client.send_file(message.channel, path) # Send that shit

Client.run("MzM5OTE4NTI4MjU1NzU0MjQ0.DFq9UQ.sQ4LNE9L2HDDKhLH9eGTCIIFO08")