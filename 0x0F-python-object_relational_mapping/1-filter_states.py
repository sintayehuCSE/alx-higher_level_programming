#!/usr/bin/python3
"""  A script that lists all STATES with a name starting with N (upper N) """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    qry = """SELECT * FROM states WHERE states.name LIKE BINARY 'N%' ORDER BY
    states.id ASC"""
    cur.execute(qry)
    res = cur.fetchall()
    for row in res:
        print(row)
    cur.close()
    conn.close()
