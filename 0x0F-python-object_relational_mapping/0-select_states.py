#!/usr/bin/python3
"""
Script will display states sorted by id in ascending order
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    user = argv[1]
    password = argv[2]
    database = argv[3]

    db = MySQLdb.connect(host="127.0.0.1", port=3306, user=root,
                         passwd=root, db=database)

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
