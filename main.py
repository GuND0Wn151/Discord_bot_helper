import discord
import os
from functions.pokemon import *
from functions.emoji import *
from functions.memes import *
from functions.help import *
bot = discord.Client()
token = 'tokenhere'

banned_user = "////"

@bot.event
async def on_message(message):
    global banned_user
    message_author = str(message.author).split("#")[0]
    message_data = message.content.split(' ')

    if message.author == bot.user:
        return

    '''if any([ "hmm", "lets see","ok","okay","yeah"]) in message.content:
        await message.channel.send("hmm")
    if any(["lol","lmao","rofl"]) in message.content:
        await message.channel.send("lol")
    if any(["sadge","sad"]) in message.content:
        await message.channel.send("sadge :(")'''

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

        if ".h meme" in message.content:
            name, url = meme_generator()
            emb = discord.Embed(title=name)
            emb.set_image(url=url)
            await message.channel.send(embed=emb)

        if ".h emoji" in message.content:
            p = emoji_get(message_data[2])
            await message.delete()
            await message.channel.send(p[0][1])

        if ".h help" in message.content:
            data = help_command()

            await message.channel.send(embed=data)

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
