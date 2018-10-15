import sys
sys.path.append("..")
from util.databaseUtil import connect
from util.scrapeUtil import getSoup
from config import baseLink as baseLink
from time import time
from scraper.search import getNameLink
from scraper.airDataFetcher import checkIfSeriesComplete,getNextEpisodeDate
from util.databaseUtil import savedb
from database.operationsUtil.seriesUtil import nextEpisodeStored,isComplete


#return -2 if the series is non-existent
#return -1 if the series is complete
#return the date in numbered format : yyyymmdd if the series is ongoing
def getData(seriesName,returnDate=False,seriesId=-1):
    mydb = connect()
    cursor = mydb.cursor()
    if(seriesId!=-1):
        if(isComplete(cursor,seriesId) == 1):
            print(seriesId,"is  complete")
            return -1
        print(seriesId,"is not complete")
        possibleNextEpisode = nextEpisodeStored(cursor,seriesId)
        if(possibleNextEpisode != None):
            return possibleNextEpisode

    name,link,year = getNameLink(seriesName,cursor)
    savedb(mydb,cursor)
    soup = getSoup(link)

    if(soup == None):
        return -2
    if(checkIfSeriesComplete(soup)):
        return -1

    nextEpisodeDate = getNextEpisodeDate(soup)
    return nextEpisodeDate

'''message = "vinay"
message = getData('got')


print(message)
targetMail = "ihm2015004@iiita.ac.in"
#sendMail(message,targetMail)'''
