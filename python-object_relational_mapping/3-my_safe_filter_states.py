#!/usr/bin/python3
"""
This module safely filters states by user input to prevent SQL injection.
"""
import MySQLdb
import sys


def safe_filter_states():
    """
    Connects to MySQL server at localhost:3306 and safely queries
    states matching the argument.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC",
        (sys.argv[4],)
    )
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    safe_filter_states()
