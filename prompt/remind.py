import sys
sys.path.append("..")
from reminder.remind import remind
from util.fileUtil import readFile
def remindSpoilers():
    inputFile = "../database/input.txt"
    emailList, seriesList = readFile(inputFile)
    remind(emailList,seriesList)
remindSpoilers()
