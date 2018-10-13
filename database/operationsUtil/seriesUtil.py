def seriesLinkExists(link,cursor):
    search = "select name from series where link='"+link+"';"
    cursor.execute(search)
    if(len(cursor.fetchall())):
        return True
    return False

def insertNameLink(name,title,link,year,cursor):
    insert = "insert into nameLinks(name,link,title,year) values"
    insert += "('"+name+"',"
    insert += "'"+link+"',"
    insert += "\""+title+"\","
    insert += year +");"
    cursor.execute(insert)
    print(cursor)

    return
def isSent(seriesId,cursor):
    return False
def getEmailListForSeries(seriesId,cursor):
    select = "select emails from emails where id in "
    select +="(select emailId from emailSeries where seriesId="+str(seriesId)+");"
    print(select)
    return
    cursor.execute(select)
    resultList = cursor.fetchall()
    emailList = [x[0] for x in resultList]
    return emailList
