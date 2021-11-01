from db.db import get_db
from utils.user import get_user
from utils.education import edu_entry
from utils.experience import exp_entry, count_exp_entries


conn = get_db()
c = conn.cursor()


# returns user selection input
def get_user_selection():
    selection_text = input("Please make a choice from the menu: ")
    return int(selection_text)


# menu that allows for user to add experience and/or education to their profile
def exp_n_edu_menu():
    # testing_data_entry()
    while True:
        print("\n1 - Add experience \n2 - Add education \n3 - Go back \n\n")
        selection = get_user_selection()
        # add experience
        if selection == 1:
            user_exp = count_exp_entries()
            # checks if max per user has already been reached
            if user_exp == 3:
                print(
                    "The maximum amount of experience have been added to your profile. Please come back again later.")
                continue
            # user-inputted data
            username = get_user()
            title = input("Job title: ")
            employer = input("Employer: ")
            startDate = input("Start date: ")
            endDate = input("End date: ")
            location = input("Location: ")
            description = input("Description: ")
            exp_entry(username, title, employer, startDate,
                      endDate, location, description)
        # add education
        elif selection == 2:
            username = get_user()
            schoolName = input("School name: ")
            degree = input("Degree: ")
            yearsAttended = int(input("Years attended: "))
            edu_entry(username, schoolName, degree, yearsAttended)
        # end loop
        elif selection == 3:
            break
        # input validation
        else:
            print("Invalid input. Please make a choice from the menu options.\n")
