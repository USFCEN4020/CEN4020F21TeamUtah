from getpass import getpass

from links_menu import LinksMenu
from db.db import get_db, create_tables
from main_menu import find_deleted_appl, main_menu
from utils.user import create_user, is_user, get_user_count, get_user
from utils.auth import login, are_credentials_valid
from utils.messages import get_unread_message_count
from utils.jobs import is_on_job_application_drought, get_applications_count, get_deleted_jobs, get_unseen_jobs, check_if_profile_exists

conn = get_db()
create_tables(conn)
c = conn.cursor()


# function to check if the username is unique when creating an account
def look_value(username):
    while is_user(username):
        print("Username already exist.")
        username = input("Username: ")

    return username


# function to check that all passwords meet the required criteria
def check_pw(password):
    Capital = False
    digit = False
    alnum = False
    while Capital == False and digit == False and alnum == False:
        for i in password:
            if i.isupper():
                Capital = True
            if i.isdigit():
                digit = True
            if not i.isalnum():
                alnum = True
        if Capital == True and digit == True and alnum == True:
            if len(password) < 8 or len(password) > 12:
                print(
                    "Password must be at least 8 and no more than 12 characters in length.")
                password = getpass()
                check_pw(password)
        elif Capital != True:
            print("Password must contain at least one capital letter")
            password = getpass()
            check_pw(password)
        elif digit != True:
            print("Password must contain at least one digit")
            password = getpass()
            check_pw(password)
        elif alnum != True:
            print("Password must contain at least one alphanumeric symbol")
            password = getpass()
            check_pw(password)


def find_in_db(first_name, last_name):

    for row in c.execute("""SELECT * FROM Username"""):
        if first_name == row[2] and last_name == row[3]:
            print("They are a part of the InCollege system")
            return
    print("They are not yet a part of the InCollege system yet")


def general():
    choice = '*'
    while choice != 'q':
        print("1 - Sign Up\n2 - Help Center\n3 - About\n4 - Press\n5 - Blog\n6 - Careers\n7 - Developers\nq - Quit")
        print()
        choice = input("Please select a option: ")
        print()

        if choice == '1':
            createnewacc()
        if choice == '2':
            print("We're here to help")
        if choice == '3':
            print("In College: Welcome to In College, the world's largest college student network with many users in many countries and territories worldwide")
        if choice == '4':
            print(
                "In College Pressroom: Stay on top of the latest news, updates, and reports")
        if choice == '5':
            print("Under construction")
        if choice == '6':
            print("Under construction")
        if choice == '7':
            print("Under construction")
        if choice not in ['1', '2', '3', '4', '5', '6', '7']:
            print("Invalid choice. Please pick an option from the menu.")

        print()


def usefulllinks():
    choice = '*'
    while choice != 'q':
        print("1 - General")
        print("2 - Browse InCollege")
        print("3 - Business Solutions")
        print("4 - Directories")
        print("q - Quit")
        print()

        choice = input("Please select a option: ")
        print()

        if choice == '1':
            general()
        if choice in ['2', '3', '4']:
            print("Under construction")
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please pick an option from the menu.")

        print()


def createnewacc():
    capacity = get_user_count()
    if capacity < 10:
        print("Please input a unique username and password")
        username = input("Username: ")
        username2 = look_value(username)
        first_name = input("First name: ")
        last_name = input("Last name: ")
        password = getpass()
        check_pw(password)
        isPlus = input(
            "Do you want to be a plus member? It will cost $10 each month (y/n) ").strip() == "y"
        logedin = 0
        create_user(username2, password, first_name,
                    last_name, logedin, isPlus)
    elif capacity == 10:
        print("The amount of allowed accounts (10) has been reached")


def notify_unread_messages():
    user = get_user()
    unread_message_count = get_unread_message_count(user)

    if unread_message_count != 0:
        print(f"You have {unread_message_count} unread messages\n")


def notify_job_application_drought():
    user = get_user()

    if is_on_job_application_drought(user):
        print("Remember – you're going to want to have a job when you graduate. Make sure that you start to apply for jobs today!")


def notify_job_application_count():
    count = get_applications_count()

    print(f"You have currently applied for {count} jobs")


# CHOICE IS A CHAR THAT HELPS NAVIGATE THROUGH THE PROGRAM MENU
def main():
    choice = '?'

    print("Jacob had dreamed about working at Southwest Airlines for as long as he can remember. He applied and interviewed for internships and full-time jobs to no avail. But after each meeting, he connected with each Southwest employee and recruiter on CollegeIn. With a growing family to support, he eventually accepted a job at a B2B IT company. Then one day he noticed that CollegeIn's people you may knowmodule suggested he connect with a Southwest recruiter he was linked to through another connection. He sent the recruiter a connection request and she responded asking if he had time to chat about a job opening. On Aug. 27, 2021, Jacob joined Southwest.")
    print()

    while choice != 'q':
        print("          MENU     ")
        print("n - Create new account")
        print("l - Login")
        print("f - Find a friend")
        print("s - Play a video of success story")
        print("t - Training")
        print("i - InCollege Important Links")
        print("u - Usefull links")
        print("q - Quit")
        print()

        question = input("Please make a choice from the menu: ")
        print()

        choice = question

        if choice == 't':
            print("t - Training and Education")
            print("i - IT Help Desk")
            print("b - Business Analysis and Strategy")
            print("s - Security")
            print()

            que = input("Please make a choice from the menu: ")
            print()

            choice = que

            if choice == 't':
                print("j - Java")
                print("c - C program")
                print("p - Python")
                print("a - Angular")
                print()

                ques = input("Please make a choice from the menu: ")
                print()

                choice = ques

                if choice == 'j':
                    print("Under Construction")
                if choice == 'c':
                    print("Under Construction")
                if choice == 'p':
                    print("Under Construction")
                if choice == 'a':
                    print("Under Construction")

                print()

            if choice == 'i':
                print("Coming soon!")
                print()
            if choice == 's':
                print("Coming soon!")
                print()
            if choice == 'b':
                print("Results in list of the following trending courses:")
                print("h - How to use In College learning")
                print("t - Train the trainer")
                print("g - Gamification of learning")
                print(
                    "Not seeing what you’re looking for? Sign in to see all 7,609 results")
                print()

                quest = input("Please make a choice from the menu: ")
                print()

                choice = quest

                if choice == 'h':
                    print("Please sign in")
                    username = input("Username: ")
                    password = getpass()
                    print()
                    isLoggedIn = are_credentials_valid(username, password)

                    if isLoggedIn:
                        login(username)
                        print("You have successfully logged in")
                        notify_unread_messages()
                        get_unseen_jobs(username)
                        check_if_profile_exists(username)
                        get_deleted_jobs(username)

                        notify_job_application_drought()
                        find_deleted_appl()
                        print()
                        main_menu()
                    else:
                        print("Incorrect username/password, please try again")

                if choice == 't':
                    print("Please sign in")
                    username = input("Username: t")
                    password = getpass()
                    print()
                    isLoggedIn = are_credentials_valid(username, password)

                    if isLoggedIn:
                        login(username)
                        print("You have successfully logged in")
                        notify_unread_messages()
                        get_unseen_jobs(username)
                        check_if_profile_exists(username)
                        get_deleted_jobs(username)

                        notify_job_application_drought()
                        find_deleted_appl()
                        print()
                        main_menu()
                    else:
                        print("Incorrect username/password, please try again")

                if choice == 'g':
                    print("Please sign in")
                    username = input("Username: ")
                    password = getpass()
                    print()
                    isLoggedIn = are_credentials_valid(username, password)

                    if isLoggedIn:
                        login(username)
                        print("You have successfully logged in")
                        notify_unread_messages()
                        get_unseen_jobs(username)
                        check_if_profile_exists(username)
                        get_deleted_jobs(username)

                        notify_job_application_drought()
                        find_deleted_appl()
                        print()
                        main_menu()

                    else:
                        print("Incorrect username/password, please try again")

        elif choice == 'f':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            print()
            find_in_db(first_name, last_name)
            previous_page = input("Press enter to go to the previous page")
            print()
        elif choice == 's':
            print("Video is now playing")
            Previous_page = input("Press enter to go to the previous page")
            print()
        elif choice == 'i':
            LinksMenu().run()
            Previous_page = input("Press enter to go to the previous page")
            print()
        elif choice == 'u':
            usefulllinks()

    # QUITS THE PROGRAM
        elif choice == 'q':
            exit()

    # CREATES NEW ACCOUNT
        elif choice == 'n':
            createnewacc()
            print()

    # LOGIN TO PROGRAM
        elif choice == 'l':
            username = input("Username: ")
            password = getpass()
            print()
            isLoggedIn = are_credentials_valid(username, password)

            if isLoggedIn:
                login(username)
                print("You have successfully logged in")
                notify_unread_messages()
                get_unseen_jobs(username)
                check_if_profile_exists(username)
                get_deleted_jobs(username)

                notify_job_application_drought()
                find_deleted_appl()
                print()
                main_menu()
            else:
                print("Incorrect username/password, please try again")

        else:
            print("Invalid choice. Please pick an option from the menu.")


if __name__ == '__main__':  # pragma: no cover
    main()
