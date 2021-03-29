#!/usr/bin/python3
'''Display states starting with upper N'''

import sys
import MySQLdb
import re


def deleteChar(strArg):
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
    stringSQL = 'SELECT id, name FROM `states`'
    cursor.execute(stringSQL)
    principalRows = cursor.fetchall()

    for row in principalRows:
        for command in strArgs:
            if (command == row[1]):
                print(row)
