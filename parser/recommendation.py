from scrape import getSeriesPage
from scrape import getSeriesSearchPage
'''
def getRecommendationList(seriesName):
    baseLink = "https://www.imdb.com"
    soup = getSeriesSearchPage(seriesName)
    soup = getSeriesPage(soup,baseLink)
    div = soup.find_all('div',{'id':'titleRecs'})[0]
    #print(div)
    images = div.find_all('img',{'class': 'loadlate hidden rec_poster_img'})
    return images[0:6]'''
