import cloudscraper
import requests
from bs4 import BeautifulSoup

codes= [ "5505767",
        "5859445",
        "5487058",
        "4899724",
        "5459525",
        "5148091",
        "5861560",
        "5495348",
        "5893884",
        "5635685",
        "5635686",
        "5459044",
        "5466482",
        "5874390",
        "5895918",
        "5582473",
        "5844758",
        "5455924"]


scraper = cloudscraper.create_scraper()  

def scrap(code):       
        html_text=scraper.get("https://danbooru.donmai.us/posts/" + code).text 
        soup = BeautifulSoup(html_text, 'html.parser')
        imgEl=soup.find(id='image')
        response = scraper.get(imgEl['src'])
        if response.status_code:
                print(response.status_code)
                fileName = getFileName(code,imgEl['src'])
                fp = open(fileName, 'wb')
                fp.write(response.content)
                fp.close()
                
def getFileName(code, url):
        url1 = url.split("/")
        return code+"_"+ url1[-1]

for c in codes:
  scrap(c)