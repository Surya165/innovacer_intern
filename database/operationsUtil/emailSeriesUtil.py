def getEmailId(email,cursor):
    select = "select id from emails where lower(emails)='"+email+"';"

    cursor.execute(select)
    result = cursor.fetchall()
    if(len(result) != 1):
        print("Multiple or None")
    return result[0][0]
def getSeriesId(seriesLink,cursor):
    select = "select id from series where link='"+seriesLink+"'";
    #print(select)
    cursor.execute(select)
    result = cursor.fetchall()
    #print(result)
    if(len(result) != 0):
        return result[0][0]
    return -1
def emailSeriesExists(emailId,seriesId,cursor):
    select = "select * from emailSeries where emailId="+emailId+" and seriesId="+seriesId;
    #print(select)
    cursor.execute(select)
    result = cursor.fetchall()
    if(len(result) == 0):
        return False
    return True
