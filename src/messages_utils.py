from db_session import db
from contextlib import closing


def send_message(sender, receiver, content):
    query = """INSERT INTO Messages (sender, receiver, content) VALUES(?,?,?);"""
    data = (sender, receiver, content)

    with closing(db.cursor()) as cursor:
        cursor.execute(query, data)
        db.commit()


def delete_messages(user, messages):
    query = """INSERT INTO DeletedMessages (user, messageId) VALUES(?,?);"""
    cursor = db.cursor()

    for message in messages:
        data = (user, message)
        cursor.execute(query, data)

    db.commit()
    cursor.close()


def get_messages(participant1, participant2):
    query = """
        SELECT * FROM Messages
        WHERE (sender = ? AND receiver = ?)
            OR (sender = ? AND receiver = ?)
        ORDER BY timestamp;
    """

    data = (participant1, participant2, participant2, participant1)

    with closing(db.cursor()) as cursor:
        cursor.execute(query, data)
        return cursor.fetchall()


def get_conversations(user):
    query = """
        SELECT sender, receiver FROM Messages
        WHERE sender = ? OR receiver = ?
        GROUP BY sender, receiver;
    """

    data = (user, user)

    with closing(db.cursor()) as cursor:
        cursor.execute(query, data)
        rows = cursor.fetchall()

    conversations = set()

    for sender, receiver in rows:
        other_person = sender if sender != user else receiver
        conversations.add(other_person)

    return conversations
