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
