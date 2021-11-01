from db.db import get_db


conn = get_db()
c = conn.cursor()


# inserts data into new row in education table
def edu_entry(username, schoolName, degree, yearsAttended):
    data = (username, schoolName, degree, yearsAttended)
    query = """INSERT INTO Education(username, schoolName, degree, yearsAttended) VALUES (?, ?, ?, ?)"""
    c.execute(query, data)
    conn.commit()
