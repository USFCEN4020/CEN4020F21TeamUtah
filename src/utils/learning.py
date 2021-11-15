from db.db import get_db


conn = get_db()
c = conn.cursor()


def get_courses(user):
    query = "SELECT course, status FROM Courses WHERE username = ?"
    data = (user,)

    c.execute(query, data)
    result = c.fetchall()

    return result


def insert_course(course, user):
    query: str = "INSERT INTO Courses VALUES (?, ?)"
    data = (user, course)
    c.execute(query, data)


def set_course_completed(course, user):
    query = "UPDATE Courses SET status=1 WHERE username=? AND course=?"
    data = (user, course)

    c.execute(query, data)
    conn.commit()
