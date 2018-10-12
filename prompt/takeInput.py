import sqlite3
connect = sqlite3.connect('spoilers')
cursor = connect.cursor()
print("Enter the email Address")
email = input()
emails = []
seriesNames = []
def dumpIntoDatabase(emails,seriesNames):
    select  = '''select * from emails'''
    print(cursor.execute(select).fetchall())
    return
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
dumpIntoDatabase(emails,seriesNames)
