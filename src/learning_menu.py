from colorama.ansi import Cursor
from src.profile_menu import ProfileMenu
from typing import Callable, Optional, Tuple
from utils.menu import Menu
from db.db import get_db
from colorama import Fore, Style

db = get_db()

class LearningMenu(Menu):
    """inCollege learning menu class"""

    def __init__(self) -> None:
        super().__init__()

        # database variables
        self.courses = ["How to use In College learning", 
                        "Train the trainer",
                        "Gamification of learning",
                        "Understanding the Architectural Design Process",
                        "Project Management Simplified"]
        self.username = str()
        self.courses_with_status = dict()
        self.read_db()

        # menu options
        self.title = "InCollege Learning"
        for course_with_status, value in self.courses_with_status.items():
            self.options[course_with_status] = self.complete_course(value[0], value[1])


    def read_db(self) -> None:
        """read course status from db"""
        cursor = db.cursor()
        query: str = "SELECT username FROM Username WHERE logedin=1"
        cursor.execute(query)
        result: Optional[Tuple] = cursor.fetchone()
        self.username = result[0] if result is not None else None
        query = "SELECT course, status FROM Courses WHERE username = ?"
        cursor.execute(query, (self.username, ))
        result = cursor.fetchall()
        if result:
            completed: str = f"{Fore.GREEN}(Completed) {Style.RESET_ALL}"
            not_completed: str = f"{Fore.RED}(Not Completed) {Style.RESET_ALL}"
            for course, status in result:
                self.courses_with_status[(f"{completed if status else not_completed}{course}")] = (course, status)
        else:
            for course in self.courses:
                query: str = "INSERT INTO Courses VALUES (?, ?, ?)"
                cursor.execute(query, (self.username, course, 0))
            db.commit()


    def complete_course(self, course, status) -> Callable:
        """wrapper for complete course callable"""
        def complete():
            """mark a course as completed"""
            cursor = db.cursor()
            if status:
                response = input("You have already taken this course, do you want to take it again? ").lower()
                if response != "yes":
                    print("Course Cancelled")
                    return

            query = "UPDATE Courses SET status=? WHERE username=? AND course=?"
            cursor.execute(query, (1, self.username, course))
            db.commit()
            print("You have now completed this training")
            self.__init__()  # update menu values
        return complete


    def run(self) -> None:
        self.read_db()
        super(LearningMenu, self).run()
