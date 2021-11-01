from db.db import get_db


conn = get_db()
c = conn.cursor()


# inserts data into new row of friends table
def friends_entry(userOne, userRequested, request):
    data = (userOne, userRequested, request)
    query = """INSERT INTO Friends(userOne, userRequested, request) VALUES (?,?,?)"""
    c.execute(query, data)
    conn.commit()


def delete_friend(user1, user2):
    query = """
        DELETE FROM Friends WHERE ((userOne = ? AND userRequested = ?) 
        OR (userOne = ? AND userRequested = ?))
        AND request = 2
    """

    data = (user1, user2, user2, user1)
    c.execute(query, data)
    conn.commit()


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


# updates key in friends table to send a request to another user to become friends
def send_request(username, requestedUser):
    query = """UPDATE Friends SET request = 1 WHERE userOne = ? AND userRequested = ?"""
    target = (username, requestedUser)
    c.execute(query, target)
    conn.commit()


# updates key in friends table to decline a friend request
def decline_request(username, requestedUser):
    query = """UPDATE Friends SET request = 0 WHERE userOne = ? AND userRequested = ?"""
    target = (username, requestedUser)
    c.execute(query, target)
    conn.commit()


# updates key in friends table to accept a friend request
def accept_request(username, requestedUser):
    query = """UPDATE Friends SET request = 2 WHERE userOne = ? AND userRequested = ?"""
    target = (username, requestedUser)
    c.execute(query, target)
    conn.commit()


def get_friend_requests(user):
    query = """
        SELECT userOne FROM Friends
        WHERE request = 1 AND userRequested = ?
    """

    data = (user,)
    c.execute(query, data)
    rows = c.fetchall()

    return [row[0] for row in rows]
