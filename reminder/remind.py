#This file is a draft for the remind file
import sys
sys.path.append("..")
from util.dateUtil import getCurrentDate
from database.operationsUtil.seriesUtil import getEmailListForSeries
from util.databaseUtil import connect
def isTimeToRemind(interval,seriesId="",emailId=""):
    if(email == "" and seriesId==""):
        if(currentTime % interval == 0):
            return True
        return False

def getRemindList(cursor):
    remindList = []
    for seriesId in seriesList:
        if(isSent(seriesId,cursor)):
            continue
        emailList = getEmailListForSeries(seriesId,cursor)
        for email in emailList:
            reminder = (email,series)
            remindList.append(reminder)
    return remindList

def remind(cursor):
    remindList = getRemindList(database,cursor)
    for email,message in remindList:
        sendMail(email,message)
def run(interval):
    mydb = connect()
    cursor = mydb.cursor()
    previousTime = 0
    while(1):
        currentTime = getCurrentDate()
        if(currentTime == previousTime):
            print("Nothing")
            continue
        if(currentTime % interval == 0):
            print("Reminding")
            remind(cursor)
        previousTime = currentTime
