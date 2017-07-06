from gtts import gTTS
from playsound import playsound
import discord
import asyncio
import os
#import tempfile
import time

client = discord.Client()

@client.event
async def on_message(message):
    millis = int(round(time.time() * 1000))
    fn = str(millis)+".mp3"
    print(message.content)
    tts = gTTS(text=str(message.content), lang='th', slow=False)
    tts.save(fn)
    playsound(fn)
    os.remove(fn)
    

client.run('')

