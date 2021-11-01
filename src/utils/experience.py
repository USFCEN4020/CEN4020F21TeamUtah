from .db import get_db


conn = get_db()
c = conn.cursor()

# inserts data into new row in experience table


def exp_entry(username, title, employer, startDate, endDate, location, description):
    data = (username, title, employer, startDate,
            endDate, location, description)
    query = """INSERT INTO Experience(username,title,employer, startDate, endDate, location, description) VAlUES(?,?,?,?,?,?,?);"""
    c.execute(query, data)
    conn.commit()


# returns number of entries for the experience table created by the same user
def count_exp_entries():
    query = """SELECT * FROM Experience WHERE username = (SELECT username FROM Username)"""
    c.execute(query)
    conn.commit()
    rows = len(c.fetchall())
    #print("The number of rows is ", rows)
    return rows
