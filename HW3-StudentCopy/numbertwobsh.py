import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests




base_url = "http://collemc.people.si.umich.edu/data/bshw3StarterFile.html"
r = urllib.request.urlopen(base_url).read()
soup = BeautifulSoup(r, 'lxml')

texty= soup.prettify()
texty = texty.replace("student", "AMAZING Student")

coup = open("steve.html", "w")

coup.write(texty)

coup.close()

tag2 = soup.find_all("div", {"class":"field-item even"})
#This is for the paragraphs inside the body.
for a in tag2:
	# print(a)
	for d in a.find_all('p'):
		for y in d:
			if "student" in y:
				y = y.replace("student", "AMAZING student")
	for z in a.find_all('h3'):
		#This is for finding people in headings
		for n in z:
			if "student" in n:
				#print(y.replace("students", "AMAZING Student"))
				pass

tag3 = soup.find_all("div", {"class":"menu-block-wrapper menu-block-3 menu-name-menu-resource-menu parent-mlid-0 menu-level-1"})
#This is for the Resources part
for t in tag3:
	for i in t.find_all('li'):
		for x in i.find_all('a'):
			for y in x:
				if "student" in y:
					print(y.replace("students", "AMAZING Student"))
				else:
					print(y)


pic = soup.find_all("div", {"class":"field-item even"})
#To replace the image in the front page
for img in pic:
	for im in img.find_all('img'):
		for x in im:
			y = 'https://scontent-ord1-1.xx.fbcdn.net/v/t1.0-1/c0.0.160.160/p160x160/10352379_826280194100725_6321001614695850668_n.jpg?oh=78424c8c9ca0be4cf542522143424889&oe=5896CECC'
			x = x.replace('https://testbed.files.wordpress.com/2012/09/bsi_exposition_041316_192.jpg', y)
		print(x)
# x_title = x.get("title")
# 			print(x_title)

# coup = open("steve.html", "w")

# soup_string = str(soup)

# coup.write(soup_string)

# coup.close()