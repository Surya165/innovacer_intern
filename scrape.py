import requests
from bs4 import BeautifulSoup
import time
import datetime
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

def getData(seriesName):
    data = requests.get('https://www.imdb.com/find?ref_=nv_sr_fn&q='+seriesName+'&s=all')
    soup = BeautifulSoup(data.text,"lxml")
    if(soup):
        print("soup exists")
    baseLink = "https://www.imdb.com"
    actualLink = "https://www.imdb.com/title/tt1396484/?ref_=fn_al_tt_1"
    divs = soup.find_all('div',{'class':'findSection'})
    if(len(divs) == 0):
        print("The Series "+seriesName+ " doesn't seem to exist")
        return
    for div in divs:
        for tr in div.find_all('td',{'class':'result_text'}):
            links = tr.find_all('a')
            print(len(links))
            if(len(links) == 0):
                print("The site "+seriesName+" doesn't seem to exist")
                return
            for a in links:
                link = baseLink + a.attrs['href']
            break
        break
    print(link)
    data = requests.get(link)
    soup = BeautifulSoup(data.text,"lxml")
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
    print(timeline)
    if(len(timeline) != 0):
        print("Series completed all it's episodes in "+timeline)
        return
    articles = soup.find_all('div',{'class':'seasons-and-year-nav'})[0]
    lastSeason = articles.find_all('a')[0]
    lastSeason = lastSeason.attrs['href']
    lastSeasonLink = baseLink + lastSeason
    actualLink = "https://www.imdb.com/title/tt0944947/episodes?season=8&ref_=tt_eps_sn_8"
    #print(actualLink)
    #print(lastSeasonLink)
    data = requests.get(lastSeasonLink)
    soup = BeautifulSoup(data.text,"lxml")
    nextEpisode = soup.find_all('div',{'class':'list detail eplist'})[0]
    airDates = nextEpisode.find_all('div',{'class':'airdate'})
    #print(len(airDates))
    ds = ""
    currentDate = datetime.datetime.now().strftime("%Y%m%d")
    currentDate = int(currentDate)
    for date in airDates:
        ds = date.text.strip()

        if(len(ds) == 0):
            break
        #print(ds)
        numberedDate = getNumberedDate(ds)
        if(numberedDate > currentDate):
            print("The next Episode Airs at ",numberedDate)
            break
    #print(len(airDates))


    #print(nextEpisode.text)"""
getData('friends')
