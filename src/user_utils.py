import sqlite3

conn = sqlite3.connect('Username.db')
c = conn.cursor()


def get_user():
    query = """SELECT username FROM Username WHERE logedin = 1"""
    c.execute(query)
    conn.commit()
    tuple = c.fetchone()
    # print(type(tuple))
    return tuple
