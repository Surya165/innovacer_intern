import sqlite3
connect = sqlite3.connect('spoilers')
cursor = connect.cursor()
def dumpDataIntoDatabase(emails,seriesNames):
    insert = '''insert into emails (email) values(?)'''
    print(insert)
    print(emails)
    cursor.execute(insert,str(emails[0]))
    select = '''select * from emails"'''
    print(cursor.execute(select).fetchall())
print("Enter the email Address")
emails = []
seriesNames = []
email = input()
while(email != "-1"):
    emails.append(email)
    print("Enter the Series Names ( Enter -1 if you want to stop)")
    seriesList = []
    series = input()
    while(series != '-1'):
        seriesList.append(series)
        series = input()
    seriesNames.append(seriesList)
    print("Enter the email Address")
    email = input()
dumpDataIntoDatabase(emails,seriesNames)
