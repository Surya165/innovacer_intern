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

def nextEpisodeStored(cursor,seriesId):

    #for unrecognisedTag
    search = "select nextEpisode from series where id="+str(seriesId)+";"
    cursor.execute(search)
    result = cursor.fetchall()
    if(len(result) != 0):
        return result[0][0]
    #end for unrecognisedTag

    '''
    #for unrecognisedTag
    #get title from the tag name
    search="select title from nameLinks where name='"+seriesName.lower()+"'";
    cursor.execute(search)
    result = cursor.fetchall()
    if(len(result) == 0):
        return None
    #end get title from tag name

    title = result[0][0]
    search = "select nextEpisode from series where name='"+title+"';"
    cursor.execute(search)
    result = cursor.fetchall()
    return result[0][0]
    #end for unrecognisedTag'''

def seriesLinkExists(link,cursor):
    search = "select name from series where link='"+link+"';"
    cursor.execute(search)
    if(len(cursor.fetchall())):
        return True
    return False
def setIsComplete(cursor,seriesId):
    update ="update series set isComplete=1 where id="+str(seriesId);
    cursor.execute(update)
def updateNextEpisodeDate(cursor,seriesId,nextEpisodeDate):
    #nextEpisode = getData("got",returnDate=True)
    #print(nextEpisode)
    return
