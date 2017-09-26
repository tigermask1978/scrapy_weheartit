#! /usr/bin/python
# -*- coding: utf8 -*-
from bs4 import BeautifulSoup
import requests
import urllib


url = 'https://weheartit.com/inspirations/taylorswift?scrolling=true&page=1'

wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text, 'lxml')
images = soup.select('img.entry-thumbnail')

'''
for image in images:
    filename = image.get('src').split('/')[-2] + image.get('src').split('/')[-1]
    #print filename,'\n'
    urllib.urlretrieve(image.get('src'), filename)
'''


resource = urllib.urlopen("https://data.whicdn.com/images/297984167/superthumb.webp")
output = open("file01.jpg", "wb")
output.write(resource.read())
output.close()
