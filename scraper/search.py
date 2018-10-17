import sys
sys.path.append("..")
from util.scrapeUtil import getSoup
from config import baseLink as baseLink
from database.operationsUtil.seriesUtil import insertNameLink,getSeriesIdByLink
def checkNameInDatabase(name,cursor):
    """Checks if the series data is present in the database
    : type name : string
    : param name : series name

    : type cursor : cursor
    : param cursor : mysqlDB cursor
    """
    search = "select title,link,year,id from nameLinks where lower(name)='"+name.lower()+"';"
    cursor.execute(search)
    result = cursor.fetchall()
    if(len(result) == 0):
        return(None,None,None,None)
    return result[0]
def getSeriesSearchPage(seriesName):
    """Returns the search page of the keyword

    : type seriesName : string
    : param seriesName : Keyword for searching the series
    """
    link = 'https://www.imdb.com/find?ref_=nv_sr_fn&q='+seriesName+'&s=all'
    soup = getSoup(link)
    return soup
def getSearchResult(divs,forList=0):
    """Returns the links and names from the search page

    : type divs : soup
    : param divs : soup object of the results division of the search page

    : type forList : int
    : param forList : argument to determine whether to return the whole result or only the first result
    """
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
    """Searches the IMDB site for the seriesName

    : type seriesName : string
    : param seriesName : keyword for searching the series

    : type forList : int
    : param forList : argument to determine whether to return the whole result or only the first result
    """
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
    """Checks if the link for the keyword is already stored in the database

    : type series : string
    : param series : keyword for searching the series

    : type cursor : cursor
    : param cursor : mysqlDB cursor
     """
    name,link,year,id = checkNameInDatabase(series,cursor)
    if(name == None and link == None):
        print("Fetching the link for "+series)
        link,name = searchIMDB(series)
        name = name.replace("(TV Series)","").strip()
        year = name[-6:]
        name = name.replace(year,"").strip()
        year = year[1:-1]

        insertNameLink(series,name,link,year,cursor)
        id = getSeriesIdByLink(cursor,link)
        return(name,link,year)
    else:
        print("Loading from the stored link for "+name)
        return(name,link,year)
