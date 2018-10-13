import sys
sys.path.append("..")
from util.scrapeUtil import getSoup
from config import baseLink as baseLink
from time import time
from search import searchIMDB
from airDataFetcher import checkIfSeriesComplete,getNextEpisodeDate


def getData(seriesName):

    link,name = searchIMDB(seriesName)
    soup = getSoup(link)

    if(soup == None):
        return "The series with the name "+seriesName+" doesn't seem to exist"
    if(checkIfSeriesComplete(soup)):
        return "The Series Completed all it's episodes"

    nextEpisodeDate = getNextEpisodeDate(soup)
    return "The next Episode airs at "+nextEpisodeDate

message = "vinay"
message = getData('flash')

print(message)
targetMail = "ihm2015004@iiita.ac.in"
#sendMail(message,targetMail)
