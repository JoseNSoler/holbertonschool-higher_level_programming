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


def execCommSQL(strComm):
    '''Execute x sql command '''

    cursor.execute(strComm)
    principalRows = cursor.fetchall()
    return (principalRows)

if __name__ == "__main__":
    '''Module'''
    ListSQL = []
    finalStr = ""

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

    getAllSQL = "SELECT cities.id, cities.name, states.name\
                FROM states, cities\
                WHERE cities.state_id = states.id"
    '''Execute a separate command '''
    ListSQL = execCommSQL(getAllSQL)
    for row in ListSQL:
        for command in strArgs:
            if (command == row[2]):
                finalStr += row[1] + ', '
    finalStr = finalStr[:-2]
    print(finalStr)
