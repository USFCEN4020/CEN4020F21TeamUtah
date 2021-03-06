from db.db import get_db

conn = get_db()
c = conn.cursor()


def are_credentials_valid(username, password):
    query = """SELECT * FROM Username WHERE username = ? AND password = ?;"""
    data = (username, password)
    c.execute(query, data)
    conn.commit()
    tuple = c.fetchall()

    return len(tuple) != 0


def login(username):
    query = """UPDATE Username SET logedin = 1 WHERE username = ?"""
    target = (username,)
    c.execute(query, target)
    conn.commit()

def logout(username):
    query = """UPDATE Username SET logedin = 0 WHERE username != ?"""
    c.execute(query, (username,))
    conn.commit()
