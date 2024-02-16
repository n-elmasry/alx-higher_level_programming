#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""
from sys import argv
import MySQLdb

if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    mycursor = db.cursor()
    mycursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    rows = mycursor.fetchall()
    for row in rows:
        print(row)
    mycursor.close()
    db.close()
