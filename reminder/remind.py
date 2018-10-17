import sys
sys.path.append("..")
from util.dateUtil import getCurrentDate
from database.operationsUtil.seriesUtil import getEmailListForSeries,getSeriesList,isSent
from util.databaseUtil import connect
from scraper.scrape import getData
from util.emailUtil import sendMail
from reminder.refresh import refresh
def isTimeToRemind(interval,seriesId="",emailId=""):
    if(email == "" and seriesId==""):
        if(currentTime % interval == 0):
            return True
        return False

def getRemindList(cursor):
    remindList = []
    seriesIdList,seriesNameList = getSeriesList(cursor)
    print(seriesIdList)
    for seriesIndex,seriesId in enumerate(seriesIdList):
        if(isSent(seriesId,cursor)):
            continue
        emailList = getEmailListForSeries(seriesId,cursor)
        #print(emailList)
        for email in emailList:
            print("getData")
            reminder = (email,getData(seriesNameList[seriesIndex],seriesId=seriesId))
            remindList.append(reminder)
    return remindList

def remindAll(cursor):
    print("hello")
    remindList = getRemindList(cursor)
    print(remindList)
    for email,message in remindList:
        print("sending mail")
        sendMail(email,message)
def run(interval):
    mydb = connect()
    cursor = mydb.cursor()
    previousTime = 0
    print("running")
    while(1):
        currentTime = getCurrentDate()
        if(currentTime == previousTime):
            continue
        if(currentTime % interval == 0):
            remindAll(cursor)
            print("Refresh")
            refresh(cursor)
            print("Reminding")

        previousTime = currentTime
run(1)
