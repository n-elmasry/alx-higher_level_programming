#!/usr/bin/python3
""" lists all states with a name starting with N """

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
        """SELECT * FROM states WHERE name LIKE BINARY 'N%'
        ORDER BY states.id ASC""")

    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
