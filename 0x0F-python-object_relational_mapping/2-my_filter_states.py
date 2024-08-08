#!/usr/bin/python3
""" A script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument """
import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(host="127.0.0.1", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE states.name={}".format(argv[4]))
    res = cur.fetchall()
    for row in res:
        print(row)
    cur.close()
    conn.close()
