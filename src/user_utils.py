import sqlite3

conn = sqlite3.connect('Username.db')
c = conn.cursor()


def get_user():
    query = """SELECT username FROM Username WHERE logedin = 1"""
    c.execute(query)
    conn.commit()
    tuple = c.fetchone()
    # print(type(tuple))
    return tuple[0]


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


def get_friends(user):
    query = """
        SELECT userOne, userRequested FROM Friends
        WHERE (userOne = ? OR userRequested = ?)
            AND request = 2
    """

    data = (user, user)
    c.execute(query, data)
    rows = c.fetchall()

    friends = set()

    for user_one, user_requested in rows:
        other_person = user_one if user_one != user else user_requested
        friends.add(other_person)

    return friends


def get_all_users():
    query = """SELECT username FROM Username"""
    c.execute(query)
    rows = c.fetchall()

    return set(row[0] for row in rows)
