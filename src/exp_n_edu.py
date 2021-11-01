import sqlite3
from db_session import db
from user_utils import get_user


conn = db
c = conn.cursor()


#inserts data into new row in experience table
def exp_entry(username, title, employer, startDate, endDate, location, description):
    data = (username, title, employer, startDate, endDate, location, description)
    query = """INSERT INTO Experience(username,title,employer, startDate, endDate, location, description) VAlUES(?,?,?,?,?,?,?);"""
    c.execute(query, data)
    conn.commit()


#returns number of entries for the experience table created by the same user
def count_exp_entries():
    query = """SELECT * FROM Experience WHERE username = (SELECT username FROM Username)"""
    c.execute(query)
    conn.commit()
    rows = len(c.fetchall())
    #print("The number of rows is ", rows)
    return rows


#inserts data into new row in education table
def edu_entry(username, schoolName, degree, yearsAttended):
    data = (username, schoolName, degree, yearsAttended)
    query = """INSERT INTO Education(username, schoolName, degree, yearsAttended) VALUES (?, ?, ?, ?)"""
    c.execute(query, data)
    conn.commit()


#returns user selection input
def get_user_selection():
    selection_text = input("Please make a choice from the menu: ")
    return int(selection_text)


#menu that allows for user to add experience and/or education to their profile
def exp_n_edu_menu():
    #testing_data_entry()
    while True:
        print("\n1 - Add experience \n2 - Add education \n3 - Go back \n\n")
        selection = get_user_selection()
        #add experience
        if selection == 1:
            user_exp = count_exp_entries()
            #checks if max per user has already been reached
            if user_exp == 3:
                print("The maximum amount of experience have been added to your profile. Please come back again later.")
                continue
            #user-inputted data
            username = get_user()
            title = input("Job title: ")
            employer = input("Employer: ")
            startDate = input("Start date: ")
            endDate = input("End date: ")
            location = input("Location: ")
            description = input("Description: ")
            exp_entry(username, title, employer, startDate, endDate, location, description)
        #add education
        elif selection == 2:
            username = get_user()
            schoolName = input("School name: ")
            degree = input("Degree: ")
            yearsAttended = int(input("Years attended: "))
            edu_entry(username, schoolName, degree, yearsAttended)
        # end loop
        elif selection == 3:
            break
        #input validation
        else:
            print("Invalid input. Please make a choice from the menu options.\n")

