def getFormattedDate(date):
    monthNames = ['Jan','Feb','Mar','Jun','Jul','Aug','Feb','Aug','Sep','Oct','Nov','Dec']
    if(date % 10000 == 0):
        return str(date / 10000)
    year = str(int(date / 10000))
    date %= 10000
    month = int(date / 100)
    date %= 100
    day = str(date)
    monthName = monthNames[month - 1]
    return day + " " + monthName + " " + year
def getNumberedDate(date):
    datesDict = {'Jan':1,
    'Feb':2,
    'Mar':3,
    'Apr':4,
    'May':5,
    'Jun':6,
    'Jul':7,
    'Aug':8,
    'Sep':9,
    'Oct':10,
    'Nov':11,
    'Dec':12
    }
    numberedDate = 1
    if(len(date) == 4):
        numberedDate = int(date) * 10000
        return numberedDate
    splits = date.split(" ")
    date,month,year = splits
    month = datesDict[month[:-1]]
    numberedDate = int(year)
    numberedDate *= 100
    numberedDate += int(month)
    numberedDate *= 100
    numberedDate += int(date)
    return numberedDate
