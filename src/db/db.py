import sqlite3
from typing import Optional
from pathlib import Path

# constants
DB_PATH = "Username.db"
DB_SETUP_PATH = (Path(__file__).parent / "./setup.sql").resolve()

# globals
db: Optional[sqlite3.Connection] = None


def get_db() -> sqlite3.Connection:
    """
    create a database
    :return: connection to the database
    """
    global db

    if db == None:
        db = sqlite3.connect(DB_PATH)

    return db


def create_tables(db):
    cursor = db.cursor()

    # Initialize database with setup file
    with open(DB_SETUP_PATH, 'r') as file:
        setup_queries = file.read()
    cursor.executescript(setup_queries)

    db.commit()
    return db
