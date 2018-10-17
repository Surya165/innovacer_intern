
import requests
import sys
sys.path.append("..")
from util.scrapeUtil import getSoup
from util.dateUtil import getNumberedDate,getFormattedDate,getCurrentDate
from config import baseLink

def checkIfSeriesComplete(soup):
    """ checks if the series is completed

    : type soup : beautiful soup object
    : param soup : soup object of the IMDB page of the series
    """
    titleBlock = soup.find_all('div',{'class':'titleBar'})
    titleBlock = titleBlock[0]
    subtext = titleBlock.find_all('div',{'class':'subtext'})[0]
    timeline = ""
    for a in subtext.find_all('a'):
        if(a.text.find('TV Series') != -1):
            timeline = a.text
            break
    timeline = timeline.replace('TV Series',"")
    timeline = timeline.replace(" ","")
    timeline = timeline[6:-2]
    #print(timeline)
    if(len(timeline) != 0):
        return True
    return False
def getLastSeasonLink(soup):
    """Returns the link of the last season's page of the seriesId

    : type soup : beautiful soup object
    : param soup : soup object of the IMDB page of the series
    """
    articles = soup.find_all('div',{'class':'seasons-and-year-nav'})[0]
    lastSeason = articles.find_all('a')[0]
    lastSeason = lastSeason.attrs['href']
    lastSeasonLink = baseLink + lastSeason
    return lastSeasonLink
def getAirDates(soup):
    """Returns the Air dates

    : type soup : beautiful soup object
    : param soup : soup object of the IMDB page of the series
    """
    lastSeasonLink = getLastSeasonLink(soup)
    soup = getSoup(lastSeasonLink)
    nextEpisode = soup.find_all('div',{'class':'list detail eplist'})[0]
    airDates = nextEpisode.find_all('div',{'class':'airdate'})
    return airDates
def getNextEpisodeDate(soup):
    """Returns the air date of the next episode

    : type soup : beautiful soup object
    : param soup : soup object of the IMDB page of the series
    """
    airDates = getAirDates(soup)
    ds = ""
    currentDate = getCurrentDate()
    latestDate = 0
    for date in airDates:
        ds = date.text.strip()
        if(len(ds) == 0):
            break
        numberedDate = getNumberedDate(ds)
        if(numberedDate > currentDate):
            formattedDate = getFormattedDate(numberedDate)
            return numberedDate,latestDate
        lastestDate = numberedDate
    return None,None
