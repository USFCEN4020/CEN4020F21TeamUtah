from pathlib import Path
from typing import List, Dict
from src.utils.user import create_user, get_user_count, is_user
from src.utils.jobs import job_entry, number_job_rows
from src.learning_menu import add_course
import logging
import re


# Constants
NEW_TRAININGS_FILE: str = "newTrainings.txt"
STUDENT_ACC_FILE: str = "studentAccounts.txt"
NEW_JOBS_FILE: str = "newJobs.txt"
JOBS_IN_SYSTEM_FILE: str = "Mycollege_jobs.txt"
USER_PROFILES_FILE: str = "Mycollege_profiles.txt"
USERS_IN_SYSTEM_FILE: str = "Mycollege_users.txt"
TRAININGS_PER_USER_FILE: str = "Mycollege_training.txt"
APPLIED_JOBS_FILE: str = "Mycollege_appliedJobs.txt"
SAVED_JOBS_FILE: str = "Mycollege_savedJobs.txt"
MAX_USER_COUNT: int = 10
MAX_JOB_COUNT: int = 10


def parse_accounts(filename: str) -> List[Dict[str, str]]:
    """
    read student account info from a file
    @param filename: name of file to read from
    @return: list of parsed accounts
    """
    student_acc_path: Path = Path(filename)
    accounts: List[Dict[str, str]] = list()
    if student_acc_path.exists():
        with open(student_acc_path, 'r') as file:
            has_next: bool = True
            while has_next:
                account = dict()
                try:
                    line: List[str] = re.split("[;, \t]", file.readline().strip())
                    account["username"], account["first_name"], account["last_name"] = line
                    account["password"]: str = file.readline().strip()
                    end: str = file.readline().strip()
                except ValueError:
                    logging.error("Invalid student account file format")
                    return accounts
                accounts.append(account)
                if end != "=====":
                    has_next = False
    else:
        logging.info("Student account file not found")

    return accounts


def parse_jobs(filename: str) -> List[Dict[str, str]]:
    """
    read new job info from a file
    @param filename: name of file to read from
    @return: list of parsed jobs
    """
    job_path: Path = Path(filename)
    jobs: List[Dict[str, str]] = list()
    if job_path.exists():
        with open(job_path, 'r') as file:
            has_next: bool = True
            while has_next:
                job = dict()
                try:
                    job["title"]: str = file.readline().strip()
                    job["description"] = str()
                    line = file.readline()
                    while line and line != "&&&\n":
                        job["description"] += line
                        line = file.readline()
                    job["poster"]: str = file.readline().strip()
                    job["employer"]: str = file.readline().strip()
                    job["location"]: str = file.readline().strip()
                    job["salary"]: str = file.readline().strip()
                    end: str = file.readline().strip()
                except ValueError:
                    logging.error("Invalid new job file format")
                    return jobs
                jobs.append(job)
                if end != "=====":
                    has_next = False
    else:
        logging.info("new job file not found")

    return jobs


def parse_trainings(filename: str) -> List[str]:
    """
    read training info from file
    @param filename: name of file to read from
    @return: list of new trainings
    """
    trainings_path: Path = Path(filename)
    if trainings_path.exists():
        with open(trainings_path, 'r') as file:
            trainings = file.read().split('\n')
    else:
        logging.info("New trainings file not found")

    return trainings


def create_account_api() -> None:
    """
    create student accounts for api
    """
    accounts: List[Dict[str, str]] = parse_accounts(STUDENT_ACC_FILE)
    for account in accounts:
        if get_user_count() < MAX_USER_COUNT:
            if is_unique_username(account["username"]) and is_valid_password(account["password"]):
                create_user(account["username"], account["password"],
                            account["first_name"], account["last_name"],
                            logedin=False, isPlus=False)
                logging.info(f"Created new account: {account['username']}")
            else:
                logging.error("Invalid username or password")
        else:
            logging.error(f"Max number of users ({MAX_USER_COUNT}) reached. Ignoring account")


def create_job_api() -> None:
    """
    create new job posts for api
    """
    jobs: List[Dict[str, str]] = parse_jobs(NEW_JOBS_FILE)
    for i, job in enumerate(jobs):
        if number_job_rows() < MAX_JOB_COUNT:
            if is_user(job["poster"]):
                job_entry(i+1, job["poster"], job["title"],
                          job["description"], job["employer"],
                          job["location"], job["salary"])
                logging.info(f"Posted new job: {job['title']} by {job['poster']}")
            else:
                logging.error("Job poster is not a user")
        else:
            logging.error(f"Max number of jobs ({MAX_JOB_COUNT}) reached. Ignoring job")


def create_training_api() -> None:
    """
    create new training entries for api
    """
    trainings = parse_trainings(NEW_TRAININGS_FILE)
    for training in trainings:
        add_course(training)
        logging.info(f"Added new training: {training}")


def is_valid_password(password: str) -> bool:
    regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,12}$"
    criteria = re.compile(regex)
    return re.search(criteria, password) is not None


def is_unique_username(username: str) -> bool:
    return not is_user(username)


def run_input_api() -> None:
    logging.basicConfig(filename='api.log',
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.DEBUG)
    logging.info("Running input APIs")
    create_account_api()
    create_job_api()
    create_training_api()
    logging.info("Execution End\n\n")


def parse_profiles(filename: str) -> List[str]:
    return 1    #PLACEHOLDER


def create_profile_api() -> None:
    return 2    #PLACEHOLDER


if __name__ == '__main__':
    run_input_api()
