import requests
import re
import pandas as pd

from bs4 import BeautifulSoup

dataBook =[]
response = requests.get(url)
response.encoding='UTF-8'

if response.ok:
   html =BeautifulSoup(response.text ,'lxml',)
   tabs= html.find('table')
   tabs=BeautifulSoup(str(tabs),'lxml')
   tds=tabs.findAll('td')

   title=html.find('h1')
       
   ps=html.findAll('p')

   imgs=html.find('img')
   imgString=str(imgs['src'])
   imgString=imgString[5:]
   imgString='https://books.toscrape.com'+imgString
