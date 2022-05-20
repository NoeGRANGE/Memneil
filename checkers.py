import json


async def checker(msg, message, messageTab):
    await reader(msg, message, messageTab)
    await supremacy(msg, message, messageTab)
    await ping_pong(msg, message)


async def reader(msg, message, messageTab):
    pub = open('public.json')
    priv = open('private.json')
    data = json.load(pub) + json.load(priv)
    for i in data:
        if msg.endswith(i["prefix"] + "?") or i["prefix"] in messageTab:
            await message.reply(i["suffix"])
    pub.close()


async def ping_pong(msg, message):
    if msg == "ping":
        response = 'pong'
        await message.reply(response)
        return


async def supremacy(msg, message, messageTab):
    if msg == "qui suis-je ?":
        if message.author.id == 474218528162054158:
            await message.reply("Un gros bggggg")
        else:
            await message.reply("Une grosse merde")
