#!/usr/bin/python3
"""takes the name of a state as an
argument and lists all cities of that state"""

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
    cursor.execute("""SELECT cities.name
                   FROM cities
                   JOIN states ON cities.state_id = states.id
                   WHERE states.name = %s
                   ORDER BY cities.id ASC""", (argv[4],))

    rows = cursor.fetchall()
    cities = []
    for row in rows:
        cities.append(row[0])

    print(', '.join(cities))
    cursor.close()
    db.close()
