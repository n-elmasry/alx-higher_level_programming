#!/usr/bin/python3
"""takes an argument and displays all values where name matches the argument"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cursor = db.cursor()
    cursor.execute(
        """SELECT * FROM states WHERE name = '{}'
        ORDER BY states.id ASC""".format(argv[4]))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
