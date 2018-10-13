def emailExists(email,cursor):
    searchTerm = email.lower()
    search = "select emails from emails where lower(emails)='"+searchTerm+"'"
    cursor.execute(search)
    if(len(cursor.fetchall())):
        return True
    return False
