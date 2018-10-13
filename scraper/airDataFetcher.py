import datetime
import requests
import sys
sys.path.append("..")
from util.scrapeUtil import getSoup
from util.dateUtil import getNumberedDate,getFormattedDate
from config import baseLink
def checkIfSeriesComplete(soup):
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
    articles = soup.find_all('div',{'class':'seasons-and-year-nav'})[0]
    lastSeason = articles.find_all('a')[0]
    lastSeason = lastSeason.attrs['href']
    lastSeasonLink = baseLink + lastSeason
    return lastSeasonLink
def getAirDates(soup):
    lastSeasonLink = getLastSeasonLink(soup)
    soup = getSoup(lastSeasonLink)
    nextEpisode = soup.find_all('div',{'class':'list detail eplist'})[0]
    airDates = nextEpisode.find_all('div',{'class':'airdate'})
    return airDates
def getNextEpisodeDate(soup):
    airDates = getAirDates(soup)
    ds = ""
    currentDate = int(datetime.datetime.now().strftime("%Y%m%d"))
    for date in airDates:
        ds = date.text.strip()
        if(len(ds) == 0):
            break
        numberedDate = getNumberedDate(ds)
        if(numberedDate > currentDate):
            formattedDate = getFormattedDate(numberedDate)
            return formattedDate
    return None
