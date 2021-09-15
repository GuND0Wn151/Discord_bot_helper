import discord
from functions.pokemon import *
from functions.emoji import *
bot = discord.Client()
token = "token"


banned_user = "////"


@bot.event
async def on_message(message):
    global banned_user
    message_author = str(message.author).split("#")[0]
    message_data = message.content.split(' ')
    print("banned", banned_user, message_author)
    if message.author == bot.user:
        return

    if message.content == "hmm":
        await message.channel.send("hmm")

    if banned_user in message_author:
        await message.delete()

    if message.content.split()[0] == ".h":
        if ".h name" in message.content:
            banned_user = str(message.content).split(' ')[2]

        if ".h add" in message.content:
            name = message_data[2]
            link = message_data[3]
            emoji_enter(name, link)
            await message.channel.send("Emoji has been Added")

        if ".h emoji" in message.content:
            p = emoji_get(message_data[2])
            await message.delete()
            await message.channel.send(p[0][1])

        if ".h weekness" in message.content:
            mes = pokemon_weakness(message_data[2])
            await message.channel.send("```" + " ".join(mes) + "```")

        if ".h ban" in message.content:
            try:
                banned_user = message.content.split(" ")[2]
            except IndexError:
                await message.channel.send("Enter A Valid user")

        if ".h unban" in message.content:
            banned_user = "////"

bot.run(token)
