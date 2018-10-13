from scraper.search import searchIMDB

def seriesLinkExists(link,cursor):
    search = "select name from series where link='"+link+"';"
    cursor.execute(search)
    if(len(cursor.fetchall())):
        return True
    return False
def checkNameInDatabase(name,cursor):
    search = "select title,link,year from nameLinks where lower(name)='"+name.lower()+"';"
    cursor.execute(search)
    result = cursor.fetchall()
    if(len(result) == 0):
        return(None,None,None)
    return result[0]
def insertNameLink(name,title,link,year,cursor):
    insert = "insert into nameLinks(name,link,title,year) values"
    insert += "('"+name+"',"
    insert += "'"+link+"',"
    insert += "\""+title+"\","
    insert += year +");"
    print(insert)
    cursor.execute(insert)

    return
def getNameLink(series,cursor):
    name,link,year = checkNameInDatabase(series,cursor)
    if(name == None and link == None):
        link,name = searchIMDB(series)
        name = name.replace("(TV Series)","").strip()
        year = name[-6:]
        name = name.replace(year,"").strip()
        year = year[1:-1]

        insertNameLink(series,name,link,year,cursor)
        return(name,link,year)
    else:
        return(name,link,year)
