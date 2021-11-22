from typing import Callable
from db.db import get_db
from utils.learning import get_courses, insert_course, set_course_completed
from utils.menu import Menu
from utils.user import get_user
from colorama import Fore, Style

db = get_db()


class LearningMenu(Menu):
    """inCollege learning menu class"""

    def __init__(self) -> None:
        super().__init__()

        # database variables
        self.username = get_user()
        course_setup(self.username)
        self.courses = [course[0] for course in get_courses(self.username)]
        self.courses_with_status = dict()
        self.read_db()

        # menu options
        self.title = "InCollege Learning"
        for course_with_status, value in self.courses_with_status.items():
            self.options[course_with_status] = self.complete_course(
                value[0], value[1])

    def read_db(self) -> None:
        """read course status from db"""
        courses = get_courses(self.username)

        if not courses:
            for course in self.courses:
                insert_course(course, self.username)

        courses = get_courses(self.username)

        completed: str = f"{Fore.GREEN}(Completed) {Style.RESET_ALL}"
        not_completed: str = f"{Fore.RED}(Not Completed) {Style.RESET_ALL}"
        for course, status in courses:
            self.courses_with_status[(
                f"{completed if status else not_completed}{course}")] = (course, status)

    def complete_course(self, course, status) -> Callable:
        """wrapper for complete course callable"""
        def complete():
            """mark a course as completed"""
            if status:
                response = input(
                    "You have already taken this course, do you want to take it again? ").lower()
                if response != "yes":
                    print("Course Cancelled")
                    return

            set_course_completed(course, self.username)
            print("You have now completed this training")
            self.__init__()  # update menu values
        return complete

    def run(self) -> None:
        self.read_db()
        super(LearningMenu, self).run()


def course_setup(user):
    default_courses = ["How to use In College learning",
                       "Train the trainer", "Gamification of learning",
                       "Understanding the Architectural Design Process",
                       "Project Management Simplified"]
    for course in default_courses:
        insert_course(course, user)
