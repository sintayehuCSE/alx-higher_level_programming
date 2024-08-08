#!/usr/bin/python3
"""  A script that lists all STATES with a name starting with N (upper N) """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    i = 0
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("""SELECT cities.name FROM states INNER JOIN cities ON
    cities.state_id = states.id WHERE states.name=%s ORDER BY cities.id""",
                (argv[4], ))
    res = cur.fetchall()
    for row in res:
        print(row[0], end='')
        if (i < len(res) - 1):
            print(", ", end='')
            i += 1
    print()
    cur.close()
    conn.close()
