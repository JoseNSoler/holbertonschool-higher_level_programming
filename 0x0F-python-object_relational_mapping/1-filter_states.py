#!/usr/bin/python3
'''Display states starting with upper N'''

import sys
import MySQLdb

if __name__ == "__main__":
    '''Module'''
    database = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    cursor = database.cursor()
    
    cursor.execute("""SELECT id, name
                    FROM states
                    ORDER BY id ASC""")
    principalRows = cursor.fetchall()

    for row in principalRows:
        strRow = str(row)
        if row [1][0] == "N": print(row)
