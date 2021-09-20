import praw
import random
def meme_generator():
    memes = praw.Reddit(
        client_id="g_DgbALQYuBhGGxiR3NcPQ",
        client_secret="TxT0093iZVDEjzUz9wnL4LGt6YKZYQ",
        username="GuND0Wn15",
        password="mahesh31",
        user_agent="memer",
    )

    bot = memes.subreddit("memes")

    data = bot.top(limit=50)
    data_list=[i for i in data]
    random_meme = random.choice(data_list)
    return [random_meme.name, random_meme.url]