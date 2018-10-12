import sys
sys.path.append("..")
import requests
from bs4 import BeautifulSoup
import datetime
import smtplib
import config
import socks
from time import time
baseLink = "https://www.imdb.com"
def getNumberedDate(date):
    datesDict = {'Jan':1,
    'Feb':2,
    'Mar':3,
    'Apr':4,
    'May':5,
    'Jun':6,
    'Jul':7,
    'Aug':8,
    'Sep':9,
    'Oct':10,
    'Nov':11,
    'Dec':12
    }
    numberedDate = 1
    if(len(date) == 4):
        numberedDate = int(date) * 10000
        return numberedDate
    splits = date.split(" ")
    date,month,year = splits
    month = datesDict[month[:-1]]
    numberedDate = int(year)
    numberedDate *= 100
    numberedDate += int(month)
    numberedDate *= 100
    numberedDate += int(date)
    return numberedDate
def getSeriesSearchPage(seriesName):
    print("Getting the request")
    data = requests.get('https://www.imdb.com/find?ref_=nv_sr_fn&q='+seriesName+'&s=all')
    print("Got the request")
    soup = BeautifulSoup(data.text,"lxml")
    return soup
def getSeriesSuggestionList(divs):
    linksList = []
    namesList = []
    for div in divs:
        for tr in div.find_all('td',{'class':'result_text'}):
            name = tr.text
            if(name.find('(TV Series)') == -1):
                continue
            links = tr.find_all('a')
            #print(len(links))
            if(len(links) == 0):
                #print("The site "+seriesName+" doesn't seem to exist")
                return
            for a in links:
                linksList.append(baseLink + a.attrs['href'])
                print(name.strip())
                namesList.append(name.strip())
    return linksList,namesList
def getSeriesPage(soup,baseLink):
    divs = soup.find_all('div',{'class':'findSection'})
    if(len(divs) == 0):
        return None
    link = getSeriesSuggestionList(divs)[0][0]
    data = requests.get(link)
    soup = BeautifulSoup(data.text,"lxml")
    return soup
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
    data = requests.get(lastSeasonLink)
    soup = BeautifulSoup(data.text,"lxml")
    nextEpisode = soup.find_all('div',{'class':'list detail eplist'})[0]
    airDates = nextEpisode.find_all('div',{'class':'airdate'})
    return airDates
def getNextEpisodeDate(airDates):
    ds = ""
    currentDate = datetime.datetime.now().strftime("%Y%m%d")
    currentDate = int(currentDate)
    for date in airDates:
        ds = date.text.strip()

        if(len(ds) == 0):
            break
        ##print(ds)
        numberedDate = getNumberedDate(ds)
        if(numberedDate > currentDate):
            return numberedDate
def getFormattedDate(date):
    monthNames = ['Jan','Feb','Mar','Jun','Jul','Aug','Feb','Aug','Sep','Oct','Nov','Dec']
    if(date % 10000 == 0):
        return str(date / 10000)
    year = str(int(date / 10000))
    date %= 10000
    month = int(date / 100)
    date %= 100
    day = str(date)
    monthName = monthNames[month - 1]
    return day + " " + monthName + " " + year

def getData(seriesName):
    baseLink = "https://www.imdb.com"
    soup = getSeriesSearchPage(seriesName)
    print("Got the Series Page")
    soup = getSeriesPage(soup,baseLink)

    if(soup == None):
        return "The series with the name "+seriesName+" doesn't seem to exist"
    if(checkIfSeriesComplete(soup)):
        return "The Series Completed all it's episodes"

    airDates = getAirDates(soup)
    nextEpisodeDate = getNextEpisodeDate(airDates)
    if(nextEpisodeDate == None):
        return "The next episode's air date is still to be declared"
    formattedDate = getFormattedDate(nextEpisodeDate)
    return "The next Episode Airs at "+ formattedDate
message = "vinay"
message = getData('suits')
print(message)
targetMail = "ihm2015004@iiita.ac.in"
#sendMail(message,targetMail)
