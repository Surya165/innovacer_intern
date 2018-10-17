import sys
sys.path.append("..")
from database.operationsUtil.seriesUtil import getSeriesList,setIsComplete
from scraper.scrape import getDataFromNet
from util.databaseUtil import connect,savedb
def refresh(cursor):
    seriesIdList,seriesNameList = getSeriesList(cursor)
    print(seriesIdList)
    for count,seriesId in enumerate(seriesIdList):
        print(seriesId)
        nextEpisodeDate,latestEpisode = getDataFromNet(cursor,seriesNameList[count],returnDate=True)
        if(nextEpisodeDate == -1):
            setIsComplete(cursor,seriesId)
