#!/usr/bin/python3
import sys
import MySQLdb


conn = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                       passwd=sys.argv[2], db=sys.argv[3])
cur = conn.cursor()
cur.execute('SELECT * FROM states ORDER BY states.id ASC')
res = cur.fetchall()
for row in res:
    print(row)
cur.close()
conn.close()
