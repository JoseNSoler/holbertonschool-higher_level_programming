#!/usr/bin/python3
'''Display cities and id_state'''

import sys
import MySQLdb
import re


def deleteChar(strArg):
    '''Delete designed chars from  a string '''
    for ch in [' ', '[', ']', '"', '\'', '\\']:
        strArg = strArg.replace(ch, "")
    return (strArg)

if __name__ == "__main__":
    '''Module'''
    database = MySQLdb.connect(
        host='localhost',
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    strArgs = str(str(sys.argv[4:]).split(';'))
    strArgs = deleteChar(strArgs).split(',')

    cursor = database.cursor()

    stringSQL = 'SELECT cities.id, cities.name, states.name\
                FROM states, cities\
                WHERE cities.state_id = states.id'
    cursor.execute(stringSQL)
    principalRows = cursor.fetchall()

    for row in principalRows:
        print(row)
