#!/usr/bin/python3
"""
This module lists all cities of a state given as an argument.
"""
import MySQLdb
import sys


def filter_cities_by_state():
    """
    Connects to MySQL server at localhost:3306 and lists all cities
    of the specified state argument.
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
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE BINARY states.name = %s "
        "ORDER BY cities.id ASC",
        (sys.argv[4],)
    )
    rows = cursor.fetchall()
    print(", ".join([row[0] for row in rows]))
    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_cities_by_state()
