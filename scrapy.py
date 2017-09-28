#! /usr/bin/python
# -*- coding: utf8 -*-
from bs4 import BeautifulSoup
import requests
import urllib


url = 'https://weheartit.com/inspirations/taylorswift?scrolling=true&page=1'
headers = {
    'Accept' : '*/*',
    'Accept-Encoding' : 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Referer' : 'https://weheartit.com/inspirations/taylorswift',
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36HH=9Runtime=fobkjmjepodfhggkgoeackdaihhmeliaALICDN/ DOL/HELLO_GWF_s_3969_r2x9ak474125_35',
}


wb_data = requests.get(url, headers=headers)
soup = BeautifulSoup(wb_data.text, 'lxml')
images = soup.select('img.entry-thumbnail')
print images


for image in images:
    filename = image.get('src').split('/')[-2] + image.get('src').split('/')[-1]
    #print filename,'\n'
    urllib.urlretrieve(image.get('src'), filename)




