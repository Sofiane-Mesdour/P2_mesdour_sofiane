import requests
import re
import pandas as pd

from bs4 import BeautifulSoup

#url='https://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html'

def getBookDetails(url):
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
       
       numAvailableStr=str(tds[5])
       num=([int(s) for s in re.findall(r'-?\d+\.?\d*', numAvailableStr)])
       numAvailable=num[0]
       
       prod=str(ps[3].text)


       
       upc=tds[0].text
       
       cat=tds[1].text
       
       prixH=tds[2].text
       
       prixT=tds[3].text
       
       rating=str(ps[2]['class'][1])
       
       
      
       dataBook.append (url)
       dataBook.append (upc)
       dataBook.append (title.text)
       dataBook.append (prixH)
       dataBook.append (prixT)
       dataBook.append (numAvailable)
       dataBook.append (prod)
       dataBook.append (cat)
       dataBook.append (rating)
       dataBook.append(imgString)

       return dataBook
   

#fin de Fonction




# test de la fonction print(print(getBookDetails('https://books.toscrape.com/catalogue/the-mysterious-affair-at-styles-hercule-poirot-1_452/index.html'))