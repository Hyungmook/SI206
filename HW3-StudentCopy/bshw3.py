import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup



coup = open("steve.html", "w")

base_url = "http://collemc.people.si.umich.edu/data/bshw3StarterFile.html"
r = urllib.request.urlopen(base_url).read()
soup = BeautifulSoup(r, 'lxml')


soup_string = str(soup)
print(soup_string)
coup = coup.write(soup_string)

