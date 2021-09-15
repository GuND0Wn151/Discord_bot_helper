import discord
from functions.pokemon import *
from functions.emoji import *
bot = discord.Client()
token = "ODEyNzE3NTM4MzQ5NDE2NDUw.YDE0MA.vpkTGJ9znG6jB2hlnXNy1WE-fUg"


# def emoji_enter(blocked_user, data):
#     conn = sqlite3.connect(r"C:\Users\ADMIN\Desktop\codes\automations\discord_db.db")
#     dbase = conn.cursor()
#     dbase.execute("INSERT INTO EMO(emoji,link) VALUES(?,?)", (blocked_user, data))
#     conn.commit()
#
#
# def emoji_get(emoji_name):
#     conn = sqlite3.connect(r"C:\Users\ADMIN\Desktop\codes\automations\discord_db.db")
#     dbase = conn.cursor()
#     dbase.execute("SELECT * FROM EMO WHERE emoji=?", (emoji_name,))
#     link = dbase.fetchall()
#
#     return link
#

# def pokemon_weakness(poke_name):
#     content = requests.get("https://www.pokemon.com/us/pokedex/" + poke_name).text
#     soup = BeautifulSoup(content, 'lxml')
#     try:
#
#         data = soup.find_all('div', {"class": "dtm-weaknesses"})
#         clean_data = data[0].text.split(' ')
#         weakness = []
#         for i in clean_data:
#             if i != '' and i != '\n':
#                 weakness += i
#         t = ''
#         for i in weakness:
#             if i.isalpha():
#                 t += i
#             else:
#                 if t != '':
#                     weakness.append(t)
#                     t = ''
#         final_weekness = []
#         for i in weakness:
#             if len(i) > 2 and i != 'Weaknesses':
#                 final_weekness.append(i)
#
#         return final_weekness
#     except TypeError:
#         return "check the spelling of the pokemon"


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