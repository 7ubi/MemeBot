import os
from dotenv import load_dotenv
import discord
import time
import glob
import random

load_dotenv()

intents = discord.Intents.all()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
  
    if message.content.startswith('$meme'):
        user = message.author
        voice_channel = user.voice.channel

        if voice_channel != None:
            
            await voice_channel.connect()

            voice_client = message.guild.voice_client

            txtfiles = []
            for file in glob.glob('./sounds/*'):
                txtfiles.append(file)

            voice_client.play(
                discord.FFmpegPCMAudio(
                    random.choice(txtfiles),
                    executable='C:/Program Files/ffmpeg/bin/ffmpeg.exe'
                )
            )
            while voice_client.is_playing():
                time.sleep(0.5)
            await voice_client.disconnect()
        else:
            await message.channel.send('User is not in a channel.')


client.run(os.environ['TOKEN'])