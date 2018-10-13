import sys

sys.path.append("..")
from scraper.search import searchIMDB
from util.fileUtil import readFile

from operations import insertEmail,insertSeries,insertEmailSeries,showEmails,showSeries,showEmailSeries
from operationsUtil.seriesUtil import getNameLink
from util.databaseUtil import connect,savedb
def insertEntry(email,seriesNames,cursor):
    email = email.strip()
    insertEmail(email,cursor)
    seriesNames = [y.strip() for y in seriesNames]
    for series in seriesNames:
        print("Getting Link for "+series)
        name,link,year = getNameLink(series,cursor)
        insertSeries(name,link,year,cursor)
        insertEmailSeries(email,name,link,cursor)
    return
def showDatabase(cursor):
    breakLine = "\n##########################"
    print(breakLine)
    print("Emails:")
    showEmails(cursor)

    print(breakLine)
    print("Series:")
    showSeries(cursor)

    print(breakLine)
    print("emailSeries:")
    showEmailSeries(cursor)
    #showEmailSeries(cursor)


#This function is to "dump" the database with the given information
#The inputs are :
#1.The list of emails
#2.The list of seriesNames
#This function reads the lists and modifies the databse appropriately
def dumpDatabase(emails,seriesNames):
    mydb = connect()
    cursor = mydb.cursor()
    numberOfEntries = len(emails)
    for i in range(numberOfEntries):
        insertEntry(emails[i],seriesNames[i],cursor)
    showDatabase(cursor)
    savedb(mydb,cursor)


#this function is the driver function to test with the input file
def testWithInputFile(inputFile):
    emails,seriesNames = readFile(inputFile)
    dumpDatabase(emails,seriesNames)
testWithInputFile('input.txt')
