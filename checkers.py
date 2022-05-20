import json


async def checker(msg, message, messageTab):
    await reader(msg, message, messageTab)
    await ping_pong(msg, message)


async def reader(msg, message, messageTab):
    f = open('public.json')
    data = json.load(f)
    for i in data:
        if msg.endswith(i["prefix"] + "?") or i["prefix"] in messageTab:
            await message.channel.send(i["suffix"])
    f.close()


async def ping_pong(msg, message):
    if msg == "ping":
        response = 'pong'
        await message.channel.send(response)
        return
