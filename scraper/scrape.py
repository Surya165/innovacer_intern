import sys
sys.path.append("..")
from util.databaseUtil import connect
from util.scrapeUtil import getSoup
from config import baseLink as baseLink
from time import time
from scraper.search import getNameLink
from scraper.airDataFetcher import checkIfSeriesComplete,getNextEpisodeDate
from util.databaseUtil import savedb
from database.operationsUtil.seriesUtil import nextEpisodeStored,isComplete,updateSeriesInfo

def getDataFromDatabase(cursor,seriesName):
    """Takes input a cursor, and the name of the series. Checks if the data of the series is already stored
    in the database. If not it returns None

    : type cursor : cursor
    : param cursor : mysqlDb cursor

    : type seriesName : string
    : param seriesName : Name of the series """
    possibleNextEpisode = nextEpisodeStored(cursor,seriesName)
    if(possibleNextEpisode != None):
        return possibleNextEpisode

#return -2 if the series is non-existent
#return -1 if the series is complete
#return the date in numbered format : yyyymmdd if the series is ongoing
def getDataFromNet(cursor,seriesName,returnDate=False):
    """ Return latest and nextEpisodeDate of the series, scrapped from the net

    : type cursor : cursor
    : param cursor : mysqlDb cursor

    : type seriesName : string
    : param seriesName : Name of the series
    """
    name,link,year = getNameLink(seriesName,cursor)

    soup = getSoup(link)
    if(soup == None):
        return -2,-2
    if(checkIfSeriesComplete(soup)):
        updateSeriesInfo(cursor,name,link,year,-1,year)
        return -1,-1
    print("getting the next episode")
    nextEpisodeDate,latestEpisodeDate = getNextEpisodeDate(soup)
    print("updating the series info")
    updateSeriesInfo(cursor,name,link,year,nextEpisodeDate,latestEpisodeDate)
    return nextEpisodeDate,latestEpisodeDate
def getData(keyword):
    """Returns the data of the series related to the keyword

    : type keyword : string
    : param keyword : Name used to search the series
    """
    mydb = connect()
    cursor = mydb.cursor()
    possibleNextEpisode = getDataFromDatabase(cursor,keyword)
    if(possibleNextEpisode != None):
        return possibleNextEpisode
    else:
        return getDataFromNet(cursor,keyword,returnDate=True)
