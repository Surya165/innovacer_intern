import sys
sys.path.append("..")
from util.scrapeUtil import getSoup
from config import baseLink as baseLink
from database.operationsUtil.seriesUtil import insertNameLink
def checkNameInDatabase(name,cursor):
    search = "select title,link,year from nameLinks where lower(name)='"+name.lower()+"';"
    cursor.execute(search)
    result = cursor.fetchall()
    if(len(result) == 0):
        return(None,None,None)
    return result[0]
def getSeriesSearchPage(seriesName):
    link = 'https://www.imdb.com/find?ref_=nv_sr_fn&q='+seriesName+'&s=all'
    soup = getSoup(link)
    return soup
def getSearchResult(divs,forList=0):
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
                link = baseLink + a.attrs['href']
                name = name.strip()
                linksList.append(link)
                namesList.append(name)
                if(forList == 0):
                    return link,name
    return linksList,namesList
def searchIMDB(seriesName,forList=0):
    soup = getSeriesSearchPage(seriesName)
    divs = soup.find_all('div',{'class':'findSection'})
    if(len(divs) == 0):
        return None
    if forList == 0:
        link,name = getSearchResult(divs,0)
        return link,name
    if forList == 1:
        linksList,namesList = getSearchResult(divs,1)
        return linksList,namesList
    return None
def getNameLink(series,cursor):
    name,link,year = checkNameInDatabase(series,cursor)
    if(name == None and link == None):
        print("Fetching the link for "+series)
        link,name = searchIMDB(series)
        name = name.replace("(TV Series)","").strip()
        year = name[-6:]
        name = name.replace(year,"").strip()
        year = year[1:-1]

        insertNameLink(series,name,link,year,cursor)
        return(name,link,year)
    else:
        print("Loading from the stored link for "+name)
        return(name,link,year)
