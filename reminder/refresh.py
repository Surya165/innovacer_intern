from database.operationsUtil.seriesUtil import getSeriesList,updateNextEpisodeDate,setIsComplete
from scraper.scrape import getData
def refresh(cursor):
    seriesIdList,seriesNameList = getSeriesList(cursor)
    print(seriesIdList)
    for count,seriesId in enumerate(seriesIdList):
        #print(seriesId)
        nextEpisodeDate = getData(seriesNameList[count],returnDate=True,seriesId=seriesId)
        if(nextEpisodeDate == -1):
            setIsComplete(cursor,seriesId)
        updateNextEpisodeDate(cursor,seriesId,nextEpisodeDate)
