import sqlite3
def emoji_enter(blocked_user, data):
    conn = sqlite3.connect(r"C:\Users\ADMIN\Desktop\codes\automations\discord_db.db")
    dbase = conn.cursor()
    dbase.execute("INSERT INTO EMO(emoji,link) VALUES(?,?)", (blocked_user, data))
    conn.commit()


def emoji_get(emoji_name):
    conn = sqlite3.connect(r"C:\Users\ADMIN\Desktop\codes\automations\discord_db.db")
    dbase = conn.cursor()
    dbase.execute("SELECT * FROM EMO WHERE emoji=?", (emoji_name,))
    link = dbase.fetchall()
    return link

