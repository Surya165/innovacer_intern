import mysql.connector
def insertEntry(email,seriesNames):
    return


#This function is to "dump" the database with the given information
#The inputs are :
#1.The list of emails
#2.The list of seriesNames
#This function reads the lists and modifies the databse appropriately
def dumpDatabase(emails,seriesNames):
    mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    passwd="yourpassword"
    )
    for i in range(len(emails)):
        insertEntry(emails[i],seriesNames[i])



#This function Reads the input file and parses it into the two lists: emails and seriesNames
#emails is the list of emails
#seriesNames is the list of the list of serieses corresponding to the emails
def readFile(filename):
    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    emails =[]
    seriesNames = []
    for i in range(int(len(content) / 2)):
        emails.append(content[2*i].replace("Email address:","").strip())

        content[2*i+1] = content[2*i+1].replace("Tv series:","")
        #print(2*i+1,content[2*i+1])
        seriesNames.append(content[2*i+1].split(","))
    return (emails,seriesNames)


#this function is the driver function to test with the input file
def testWithInputFile(inputFile):
    emails,seriesNames = readFile(inputFile)
    dumpDatabase(emails,seriesNames)
testWithInputFile('input.txt')
