import sqlite3
connect = sqlite3.connect('spoilers')
cursor = connect.cursor()
print("Enter the email Address")
email = input()
while(email != "-1"):

    print("Enter the Series Names ( Enter -1 if you want to stop)")
    seriesList = []
    series = input()
    while(series != '-1'):
        seriesList.append(series)
        series = input()
    print("Enter the email Address")
    email = input()
