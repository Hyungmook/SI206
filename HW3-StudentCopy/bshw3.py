import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests


coup = open("steve.html", "w")

base_url = "http://collemc.people.si.umich.edu/data/bshw3StarterFile.html"
r = urllib.request.urlopen(base_url).read()
soup = BeautifulSoup(r, 'lxml')


soup_string = str(soup)

coup = coup.write(soup_string)

tags = soup.find_all("div", {"class":"menu-block-wrapper menu-block-1 menu-name-main-menu parent-mlid-0 menu-level-2"})

for t in tags:
	for i in t.find_all('li'):
		for x in i.find_all('a'):
			x_href = x.get("href")
			if "student" in x_href:
				print(x_href.replace("students", "AMAZING Student"))


				

