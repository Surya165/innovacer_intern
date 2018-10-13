from bs4 import BeautifulSoup
import requests
def getSoup(link):
    data = requests.get(link)
    soup = BeautifulSoup(data.text,"lxml")
    return soup
