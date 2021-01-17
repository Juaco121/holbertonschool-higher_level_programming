#!/usr/bin/python3
"""
Script will display states sorted by id in ascending order
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':

    db = MySQLdb.connect(
        host="localhost", user=argv[1], passwd=argv[2], db=argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print("{}".format(row))
