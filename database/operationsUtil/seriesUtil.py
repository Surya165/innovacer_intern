from util.dateUtil import getCurrentDate
def getEmailListForSeries(seriesId,cursor):
    select = "select emails from emails where id in "
    select +="(select emailId from emailSeries where seriesId='"+str(seriesId)+"');"
    cursor.execute(select)
    resultList = cursor.fetchall()
    emailList = [x[0] for x in resultList]
    return emailList
def getSeriesList(cursor):
    select = "select id,name from series;"
    cursor.execute(select)
    result = cursor.fetchall()
    idList = [x[0] for x in result]
    nameList =[x[1] for x in result ]
    return idList,nameList
def getSeriesIdByLink(cursor,link):
    select = "select id from series where link='"+link+"';"
    cursor.execute(select)
    print(select)
    result = cursor.fetchall()
    if(len(result) == 0):
        return -1
    else:
        return result[0][0]
def insertNameLink(name,title,link,year,cursor):
    insert = "insert into nameLinks(name,link,title,year) values"
    insert += "('"+name+"',"
    insert += "'"+link+"',"
    insert += "\""+title+"\","
    insert += year +");"
    cursor.execute(insert)
    print(cursor)

    return
def isComplete(cursor,seriesId):
    select = " select isComplete from series where id="+str(seriesId);
    cursor.execute(select)
    result = cursor.fetchall()
    if(result[0][0] == None):
        return 0
    return result[0][0]
def isSent(seriesId,cursor):
    return False

def nextEpisodeStored(cursor,seriesName):
    search = "select nextEpisode from series where name='"+seriesName+"';"
    cursor.execute(search)
    result = cursor.fetchall()
    if(len(result) != 0):
        return result[0][0]

    search="select title from nameLinks where name='"+seriesName.lower()+"'";
    cursor.execute(search)
    result = cursor.fetchall()
    if(len(result) == 0):
        return None

    title = result[0][0]
    search = "select nextEpisode from series where name='"+title+"';"
    cursor.execute(search)
    result = cursor.fetchall()
    return result[0][0]

def seriesLinkExists(link,cursor):
    search = "select name from series where link='"+link+"';"
    cursor.execute(search)
    if(len(cursor.fetchall())):
        return True
    return False
def setIsComplete(cursor,seriesId):
    update ="update series set isComplete=1 where id="+str(seriesId);
    cursor.execute(update)
def updateSeriesInfo(cursor,name,link,year,nextEpisodeDate,latestEpisodeDate):
    currentDate = getCurrentDate()
    id = "select id from series where link='"+link+"';"
    cursor.execute(id)
    result = cursor.fetchall()
    if(len(result) != 0):
        id = result[0][0]
        update = "update series set name='"+name+"',"
        update += " year="+str(year)+ ", "
        update += "nextEpisode="+str(nextEpisodeDate)+","
        update += "lastUpdated='"+str(currentDate)+"'where  link='"+link+"';"
        print(update)
        cursor.execute(update)
    else:
        insert = "insert into series (name,link,year,nextEpisode,lastUpdated,latestEpisode) values"
        insert += "('"+name+"','"+link+"',"+str(year)+","+str(nextEpisodeDate)+","+str(currentDate)+","+str(latestEpisodeDate)+");"
        print(insert)
        cursor.execute(insert)
