import logging
from dotenv import load_dotenv
import discord
import glob
import random
import time

load_dotenv()

class MemeBot:
    logger = logging.getLogger(discord.__name__)

    def login(self, client):
        self.logger.info('We have logged in as {0.user}'.format(client))

    async def playMeme(self, message):
        voice_client = message.guild.voice_client
        voicefiles = []
        for file in glob.glob('./sounds/*.MP3'):
            voicefiles.append(file)

        memeSound = random.choice(voicefiles)

        self.logger.info('Playing {0}'.format(memeSound))

        voice_client.play(
            discord.FFmpegPCMAudio(
                memeSound,
                executable='C:/Program Files/ffmpeg/bin/ffmpeg.exe'
            )
        )

    async def playMemeOnMessage(self, message):
        user = message.author

        if user.voice == None:
            await message.channel.send('You have to be in a voice channel.') 
            return
        
        voice_channel = user.voice.channel
        await voice_channel.connect()

        await self.playMeme(message)
        
        voice_client = message.guild.voice_client
        while voice_client.is_playing():
            time.sleep(0.5)

        await voice_client.disconnect()