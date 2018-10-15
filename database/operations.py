import mysql.connector
import sys
sys.path.append("..")
from operationsUtil.emailUtil import emailExists
from operationsUtil.seriesUtil import seriesLinkExists
from operationsUtil.emailSeriesUtil import getEmailId,getSeriesId,emailSeriesExists
##
##Don't
##         Forget
##                  To Write
##                              seriesLinkExists()

def insertEmail(email,cursor):
    insert = "insert into emails(emails) values('"+email+"');"
    if(emailExists(email,cursor)):
        #print("Email "+email+" alreadyExists")
        return
    cursor.execute(insert)
    return

def insertSeries(name,link,year,cursor):
    insert ="insert into series(name,link,year) values";
    insert += "('"+name+"',"
    insert += "'"+link+"',"
    insert += str(year) +");"
    if(seriesLinkExists(link,cursor)):
        #print("Series already exists")
        return
    #print(insert)
    cursor.execute(insert)



def insertEmailSeries(email,seriesName,seriesLink,cursor):
    emailId = str(getEmailId(email,cursor))
    #print(emailId)
    seriesId = str(getSeriesId(seriesLink,cursor))
    #print(seriesId)
    if(emailSeriesExists(emailId,seriesId,cursor)):
        #print("email series exists")
        return
    insert = "insert into emailSeries(emailId,seriesId) values('"+emailId+"','"+seriesId+"');"
    cursor.execute(insert)
def showEmails(cursor):
    select = "select * from emails;"
    cursor.execute(select)
    result = cursor.fetchall()
    for x in result:
        print(x)
def showSeries(cursor):
    select = "select * from series;"
    cursor.execute(select)
    result = cursor.fetchall()
    for x in result:
        print(x)
def showEmailSeries(cursor):
    select = "select * from emailSeries;"
    cursor.execute(select)
    result = cursor.fetchall()
    for x in result:
        print(x)

def showDatabase(cursor):
    breakLine = "\n##########################"
    print(breakLine)
    print("Emails:")
    showEmails(cursor)

    print(breakLine)
    print("Series:")
    showSeries(cursor)

    print(breakLine)
    print("emailSeries:")
    showEmailSeries(cursor)
