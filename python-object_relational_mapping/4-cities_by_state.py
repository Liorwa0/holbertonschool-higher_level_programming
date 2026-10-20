#!/usr/bin/python3
"""
This module lists all cities from the database hbtn_0e_4_usa.
"""
import MySQLdb
import sys


def list_cities():
    """
    Connects to MySQL server at localhost:3306 and lists all cities
    sorted by cities.id in ascending order.
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
        "SELECT cities.id, cities.name, states.name "
        "FROM cities JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    list_cities()
