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


def is_plus(user):
    query = """SELECT isPlus FROM Username WHERE username = ?"""
    data = (user,)
    c.execute(query, data)
    tuple = c.fetchone()
    return bool(tuple[0])


def are_friends(user1, user2):
    query = """
        SELECT userOne, userRequested FROM Friends
        WHERE ((userOne = ? AND userRequested = ?) 
            OR (userOne = ? AND userRequested = ?))
            AND request = 2
    """

    data = (user1, user2, user2, user1)
    c.execute(query, data)
    tuple = c.fetchone()

    return tuple != None


def is_user(user):
    query = """SELECT username FROM Username WHERE username = ?"""
    data = (user,)
    c.execute(query, data)
    tuple = c.fetchone()

    return tuple != None
