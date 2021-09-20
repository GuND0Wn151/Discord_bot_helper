import discord


def help_command():
    dic = {
        "meme": "Use this to show memes",
        "add {name} {emoji}": "use this to add a emoji to bot",
        "emoji {name}": "Use this to show the emoji",
        "weekness {Name}": "Use this command to find weekness of a particular pokemon",
        "ban {username}": "Ban a user with this command",
        "unban {username}": "Unban the user",
    }


    em = discord.Embed(colour=discord.Colour.blue())
    em.add_field(name='Helper Bot Help Command', value="All the Available commands are", inline=False)
    for i in dic.keys():
        em.add_field(name="."+i, value=dic[i], inline=False)
    return em
