from db.db import get_db
import datetime

conn = get_db()
c = conn.cursor()


def get_all_jobs():
    query = """SELECT * FROM Jobs"""
    c.execute(query)
    return c.fetchall()


def job_entry(username, title, description, employer, location, salary):

    data = (username, title, description, employer, location, salary)
    query = """INSERT INTO Jobs(username,title,description,employer,location,salary) VAlUES(?,?,?,?,?,?);"""
    c.execute(query, data)
    conn.commit()


def number_job_rows():
    query = """SELECT * FROM Jobs"""
    c.execute(query)
    conn.commit()
    rows = len(c.fetchall())
    # print("The number of rows is ", rows)
    return rows


def job_deletion(username, title, description, employer, location, salary):
    data = (username, title, description, employer, location, salary)
    query = """DELETE Jobs(username,title,description,employer,location,salary) VAlUES(?,?,?,?,?,?);"""
    c.execute(query, data)
    conn.commit()


def apply_job_entry(username, title, grad_date, entry_date, description):
    data = (username, title, grad_date, entry_date, description)
    query = """INSERT INTO Applications(username, title, grad_date, entry_date, description) VALUES(?,?,?,?,?)"""
    c.execute(query, data)
    conn.commit()


def increase_app_count(user):
    query = """SELECT applnumber FROM Username WHERE username = ?;"""
    c.execute(query, user)
    conn.commit()
    app_count = c.fetchone() + 1
    query = """UPDATE Username SET applnumber = ? WHERE username = ?;"""
    data = (app_count, user)
    c.execute(query, data)
    conn.commit()


def get_applications_count(user):
    query = """
        SELECT COUNT(rowid) FROM Applications
        WHERE username = ?;
    """
    data = (user,)

    c.execute(query, data)
    row = c.fetchone()
    application_count = row[0]

    return application_count


def get_last_application(user):
    query = """
        SELECT MAX(timestamp) FROM Applications
        WHERE username = ?;
    """
    data = (user, )

    c.execute(query, data)
    row = c.fetchone()
    last_application = row[0]

    return last_application


def is_on_job_application_drought(user):
    last_application_epoch = get_last_application(user)

    if last_application_epoch == None:
        return True

    last_application = datetime.datetime.fromtimestamp(last_application_epoch)

    now = datetime.datetime.now()
    delta = now - last_application

    return delta.days >= 7
