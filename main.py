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

    await checker(msg, message, msgTab)

    if msg == '!meme':
        response = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        await message.reply(response)
        return

    if msg == '!viken':
        response = '!meme'
        await message.reply('https://viken.fun/')
        return

    if msg == '!help':
        response = '!meme - get a random meme url\n\n' \
                   '!meme-creator "text1" "text2" - create a random meme with 2 lalbels\n\n' \
                   '!viken - get the URL of a strange website'
        await message.reply(response)
        return

    msgArg = msg.split('"')

    if msgTab[0] == '!meme-creator' and len(msgArg) == 5:
        data = requests.get('https://api.imgflip.com/get_memes').json()
        URL = 'https://api.imgflip.com/caption_image'
        i = random.randint(1, 100)

        params = {
            'username': USERNAME,
            'password': PASSWORD,
            'template_id': data['data']['memes'][i]['id'],
            'text0': msgArg[1],
            'text1': msgArg[3]
        }
        response = requests.request('POST', URL, params=params).json()
        print(response)
        await message.reply(response['data']['url'])
        return

client.run(DISCORD_TOKEN)
