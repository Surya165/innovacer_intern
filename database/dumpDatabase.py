import mysql.connector
import sys
sys.path.append("..")
from util.fileUtil import readFile
def insertEntry(email,seriesNames):
    return


#This function is to "dump" the database with the given information
#The inputs are :
#1.The list of emails
#2.The list of seriesNames
#This function reads the lists and modifies the databse appropriately
def dumpDatabase(emails,seriesNames):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234"
    )
    numberOfEntries = len(emails)
    for i in range(numberOfEntries):
        insertEntry(emails[i],seriesNames[i])


#this function is the driver function to test with the input file
def testWithInputFile(inputFile):
    emails,seriesNames = readFile(inputFile)
    dumpDatabase(emails,seriesNames)
testWithInputFile('input.txt')
