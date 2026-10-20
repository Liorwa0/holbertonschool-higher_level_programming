#!/usr/bin/python3
"""
This module connects to a MySQL database and fetches all states
from the specified database, ordered by states.id in ascending order.
"""
import MySQLdb
import sys


def list_states():
    """
    Connects to a MySQL server running on localhost at port 3306
    and lists all states from the database passed as arguments.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    list_states()
