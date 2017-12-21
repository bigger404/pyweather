#!/usr/bin/python3
#Scrape the hi and low temps from https://www.wunderground.com/ and beautifulsoup

from urllib.request import urlopen
from bs4 import BeautifulSoup
url = "https://www.wunderground.com/weather/us/ca/castro-valley/94546"
html = urlopen(url)
soup = BeautifulSoup(html,'lxml')

print("hi "+soup.find("span",{"class":"hi"}).text)
print("lo "+soup.find("span",{"class":"lo"}).text)
