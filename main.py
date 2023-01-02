import discord
from memebot import MemeBot
import os

intents = discord.Intents.all()
client = discord.Client(intents=intents)

memeBot = MemeBot()

@client.event
async def on_ready():
    memeBot.login(client)


@client.event
async def on_message(message):

    if message.author == client.user:
        return
  
    if message.content.startswith('$meme'):
        await memeBot.playMemeOnMessage(message)

client.run(os.environ['TOKEN'])