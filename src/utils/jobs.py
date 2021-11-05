from db.db import get_db
import datetime

conn = get_db()
c = conn.cursor()


def get_all_jobs():
    query = """SELECT * FROM Jobs"""
    c.execute(query)
    return c.fetchall()


def job_entry(jobid, username, title, description, employer, location, salary):

    data = (jobid, username,title, description, employer, location, salary)
    query = """INSERT INTO Jobs(jobid, username,title,description,employer,location,salary) VAlUES(?,?,?,?,?,?,?);"""
    c.execute(query, data)
    conn.commit()


def number_job_rows():
    query = """SELECT * FROM Jobs"""
    c.execute(query)
    conn.commit()
    rows = len(c.fetchall())
    # print("The number of rows is ", rows)
    return rows


def job_deletion(jobid, username, title, description, employer, location, salary):
    data = (jobid, username, title, description, employer, location, salary)
    query = """DELETE Jobs(jobid, username, title,description,employer,location,salary) VAlUES(?,?,?,?,?,?,?);"""
    c.execute(query, data)
    conn.commit()


def apply_job_entry(jobid, username, title, grad_date, entry_date, description):
    data = (jobid,username, title, grad_date, entry_date, description)
    query = """INSERT INTO Applications(jobid, username, title, grad_date, entry_date, description) VALUES(?,?,?,?,?,?)"""
    c.execute(query, data)
    conn.commit()


def increase_app_count(user):
    query = """SELECT applnumber FROM Username WHERE username = ?;"""
    c.execute(query, (user,))
    conn.commit()
    app_count = c.fetchone()[0] + 1
    query = """UPDATE Username SET applnumber = ? WHERE username = ?;"""
    data = (app_count, user)
    c.execute(query, data)
    conn.commit()

def get_deleted_jobs(user):
    query = """SELECT *
FROM   Applications C
WHERE  NOT EXISTS (SELECT 1
                   FROM   Jobs e
                   WHERE  c.title = e.title) and username = ?;
        """

    data=(user,)


    c.execute(query, data)

    rows=c.fetchall()
    if len(rows)>0:
        print("tuple of deleted jobs")
    for row in rows:
        print(row)
    return 0


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

def insert_into_seenjobs(jobid, username):

    data = (jobid, username)
    query = """INSERT INTO Seenjobs (jobid, username) VALUES(?,?)"""
    c.execute(query, data)
    conn.commit()

def get_unseen_jobs(user):
    query = """
    SELECT * FROM Jobs as j where not exists (select 1 from Seenjobs as s where j.jobid=s.jobid and s.username=?);
       """
    data = (user,)

    c.execute(query, data)
    rows = c.fetchall()
    if len(rows)>0:
        print("tuple of unseen jobs:")
    for row in rows:
        print(row)
        insert_into_seenjobs(row[0],user)

    return 0


def insert_into_seenprofiles(user, profilename):
    data = (user, profilename)
    query = """INSERT INTO Seenprofiles(username, profilename) VALUES(?,?)"""
    c.execute(query, data)
    conn.commit()


def check_new_profiles(user):
    query=""" SELECT * from Profile as p where NOT exists (select 1 from Seenprofiles as s where p.username=s.profilename"""
    data = (user,)
    c.execute(query, data)
    rows = c.fetchall()

    for row in rows:
        print(row[0]+row[1]+" has joined In college")
        insert_into_seenprofiles(user,row[0])

def check_if_profile_exists(user):
    query= """ SELECT * from Profile where username=?"""
    data=(user,)
    c.execute(query,data)
    rows=c.fetchall()

    if len(rows)<1:
        print("please Don't forget to create a profile")


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
