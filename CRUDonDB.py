#BLL

import pymysql


def executeQuery(strQuery):
    '''This str executeQuery(str) method takes a SQL query as string input and
    returns a string of the results obtained'''
    global con
    myCursor = con.cursor()
    rows_fetched = myCursor.execute(strQuery)                     # cursor.execute(sql_query) executes the input sql query and returns the no. of records fetched

    l = []
    strData = ""

    # following 'if' statement is just to get the column names from the table and apply formatting on it for better visualisation
    # it's for cosmetic purpose and you can skip it entirely
    if 'SELECT' in strQuery or 'select' in strQuery:
        for column_name in myCursor.description:            # cursor.description returns a list of tuples describing columns in result set
            strData += str(column_name[0].title()) + '  '   # tuple's 0th location has the name of the column
            l.append(len(column_name[0]) + 2)               # calculates the spacing reqd. for the column name
        strData += "\n"

    for row in myCursor.fetchall():                        # cursor.fetchall() fetches the data from the table on the basis of the query you have provided
        i = 0                                              #just to iterate list 'l' conatining the width of column names
        for cell in row:
            strData += str(cell) + "\t"
            i += 1
        strData += "\n"
    return strData + "Total Records: " + str(rows_fetched)


def login(host, user, password):
    '''This function takes host, user name and password from
    the user and creates a conncection using pymysql class'''
    global con
    try:
        con = pymysql.connect(host = host, user = user, password = password)
    except:
        raise Exception("Invalid Credentials!! Retry.")


global host, user, password

#PL

if __name__ == '__main__':
    while(True):
        try:
            host = input("Enter Server Name: ")
            user = input("Enter UserName: ")
            password = input("Enter Password: ")
            login(host, user, password)
            print("- Login Successful!! -".center(100, '*'))
            break
        except Exception as err:
            print(err)

    while(True):
        try:
            strQuery = input("Enter Your Query: ")
            strResult = executeQuery(strQuery)
            print(strResult)
        except Exception as err:
            print(err)
