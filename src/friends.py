from db.db import get_db
from utils.user import get_user
from utils.friends import get_friends, delete_friend, get_friend_requests
from typing import Optional

conn = get_db()
c = conn.cursor()


# returns username of student that a user searches for to send a friend request if it matches a user within the inCollege system.
def search_for_user():
    choice = 0
    while(choice != 4):
        choice = int(input("1. Search by last name \n"
                           "2. Search by university \n"
                           "3. Search by major \n"
                           "4. Go back\n"
                           "Please make a selection: "))

        if(choice == 1):
            lastName = input("Enter a student's last name: ")
            query = """SELECT username FROM Username WHERE lastname = ?"""
            c.execute(query, (lastName,))
            result: Optional[tuple] = c.fetchone()
        elif(choice == 2):
            university = input("Enter a student's university: ")
            query = """SELECT username FROM Profile WHERE universityName = ?"""
            c.execute(query, (university,))
            result: Optional[tuple] = c.fetchone()
        elif(choice == 3):
            major = input("Enter a student's major: ")
            query = """SELECT username FROM Profile WHERE major = ?"""
            c.execute(query, (major,))
            result: Optional[tuple] = c.fetchone()
        elif(choice == 4):
            return

        if result is None:
            print("There are no students registered with that data. ")
            return
        else:
            return result


# reads data from friends table
def read_friend_requests(user):
    myFriendRequests = get_friend_requests(user)
    if(len(myFriendRequests) > 0):
        print("You have " + str(len(myFriendRequests)) +
              " new friend requests from ")
        for request in range(len(myFriendRequests)):
            print(request, end=" ")


def show_my_network():
    user = get_user()

    for i, friend in enumerate(get_friends(), start=1):
        print(f"{i} - {friend}")

    user_to_delete = input(
        "If you would like to delete anyone from your list, type their name: ")
    delete_friend(user, user_to_delete)
