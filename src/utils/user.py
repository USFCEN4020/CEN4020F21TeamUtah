from db.db import get_db

conn = get_db()
c = conn.cursor()


def create_user(username, password, firstname, lastname, logedin, isPlus):
    query = """INSERT INTO Username (username, password,firstname,lastname, logedin, isPlus) VALUES(?,?,?,?,?,?);"""
    data = (username, password, firstname, lastname, logedin, isPlus)
    c.execute(query, data)
    conn.commit()


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


def is_user(user):
    query = """SELECT username FROM Username WHERE username = ?"""
    data = (user,)
    c.execute(query, data)
    tuple = c.fetchone()

    return tuple != None


def get_all_users():
    query = """SELECT username FROM Username"""
    c.execute(query)
    rows = c.fetchall()

    return set(row[0] for row in rows)


def get_user_count():
    query = """SELECT count(username) FROM Username"""
    c.execute(query)
    row = c.fetchone()

    return row[0]
