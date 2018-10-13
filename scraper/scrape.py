import sys
sys.path.append("..")
from util.databaseUtil import connect
from util.scrapeUtil import getSoup
from config import baseLink as baseLink
from time import time
from search import getNameLink
from airDataFetcher import checkIfSeriesComplete,getNextEpisodeDate
from util.databaseUtil import savedb


def getData(seriesName):
    mydb = connect()
    cursor = mydb.cursor()
    name,link,year = getNameLink(seriesName,cursor)
    savedb(mydb,cursor)
    soup = getSoup(link)

    if(soup == None):
        return "The series with the name "+seriesName+" doesn't seem to exist"
    if(checkIfSeriesComplete(soup)):
        return "The Series Completed all it's episodes"

    nextEpisodeDate = getNextEpisodeDate(soup)
    return "The next Episode airs at "+nextEpisodeDate

message = "vinay"
message = getData('legends of tomorrow')

print(message)
targetMail = "ihm2015004@iiita.ac.in"
#sendMail(message,targetMail)
