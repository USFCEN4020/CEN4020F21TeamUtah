import sqlite3
from src.db import db


def get_mock_db():
    mock_db = sqlite3.connect(':memory:')
    db.create_tables(mock_db)

    return mock_db


def add_user(db: sqlite3.Connection, username: str = None, password: str = None,
             firstname: str = None, lastname: str = None) -> None:
    """Add user to Username table"""
    if username is not None and password is not None:
        query = "INSERT INTO Username (username, password, firstname, lastname) VALUES(?, ?, ?, ?);"
        db.cursor().execute(query, (username, password, firstname, lastname))
    db.commit()


def add_friend(db: sqlite3.Connection, self_username: str = None,
               requested_username: str = None, request: int = 0):
    data = (self_username, requested_username, request)
    if self_username is not None and requested_username is not None:
        query = "INSERT INTO Friends(userOne, userRequested, request) VALUES (?,?,?)"
        db.execute(query, data)
    db.commit()


def add_profile(db: sqlite3.Connection, username: str, title: str,
                major: str, university: str, about: str):
    query = "INSERT INTO Profile(username, title, major, universityName, about) VALUES (?, ?, ?, ?, ?)"
    db.execute(query, (username, title, major, university, about))
    db.commit()


def login_user(db: sqlite3.Connection, username: str):
    query = """UPDATE Username SET logedin = 1 WHERE username = ?"""
    db.execute(query, (username, ))
    db.commit()


def add_new_message(db: sqlite3.Connection, sender_user: str = None, receiver_user: str = None,
                    sample_content: str = None):
    query = """INSERT INTO Messages (sender, receiver, content) VALUES(?,?,?);"""
    db.execute(query, (sender_user, receiver_user, sample_content))
    db.commit()
