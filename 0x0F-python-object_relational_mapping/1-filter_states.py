#!/usr/bin/python3

"""
This is a module script that lists all states with a name starting with N (upper N) 
from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    try:
        db = MySQLdb.connect(
                port = 3306,
                host = "localhost"
                username = sys.argv[1],
                passwd = sys.argv[2],
                db = sys.argv[3])
        cur = db.cursor()
        cur.execute("SELECT * FROM states\
                     WHERE name LIKE BINARY 'N%'\
                     ORDER BY id ASC")
        states = cur.fetchall()

        db = fetchall()
        
        for name in states:
            print(name)
    
    except MySQLdb.Error, e:
        print(f"Error connecting to MySQL: {e}")

    cur.close()
    db.close()

