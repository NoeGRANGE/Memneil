import discord
import requests
import random
import os
from dotenv import load_dotenv

from checkers import checker

# init discord bot
client = discord.Client()

load_dotenv()

# init discord token
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')


@client.event
async def on_message(message):
    msg = message.content.lower()
    if message.author == client.user:
        return

    msgTab = msg.split(' ')
    if msgTab[0] == '!meme-creator' and len(msgTab) == 3:
        data = requests.get('https://api.imgflip.com/get_memes').json()
        URL = 'https://api.imgflip.com/caption_image'
        i = random.randint(1, 100)

        params = {
            'username': USERNAME,
            'password': PASSWORD,
            'template_id': data['data']['memes'][i]['id'],
            'text0': msgTab[1],
            'text1': msgTab[2]
        }
        response = requests.request('POST', URL, params=params).json()
        print(response)
        await message.reply(response['data']['url'])
        return

    await checker(msg, message, msgTab)

    if msg == '!meme':
        response = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        await message.reply(response)
        return

    if msg == '!viken':
        response = '!meme'
        await message.reply('https://viken.fun/')
        return


client.run(DISCORD_TOKEN)
