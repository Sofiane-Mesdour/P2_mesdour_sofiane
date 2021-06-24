# -*- coding: utf-8 -*-

import autopep8
import requests
import re
import csv
import pandas as pd
import os

from bs4 import BeautifulSoup
from getCategory import getCategoryBooks
from getImages import saveImages

print ('Veuillez entrer une url')
url = str(input())
imageFolder='/images'
books = []
headers = ['product_page_url', 'universal_ product_code (upc)', 'title', 'price_including_tax', 'price_excluding_tax',
           'number_available', 'product_description', 'category', 'review_rating', 'image_url']


response = requests.get(url)
response.encoding='UTF-8'


if response.ok:
    categoriesHtml=BeautifulSoup(response.text ,'lxml')
    
    uls=categoriesHtml.findAll('ul')
    ul=str(uls[2])
    ul=BeautifulSoup(ul,'lxml')
    lis2=ul.findAll('li')
    #print(lis2)
    # correction en tableau lis=[lis]  
    #lis2=lis2[5]
    """
    try:
        os.mkdir(imageFolder)
    except:
        print('dossier exsiste déja')
        """

    for li in lis2:
            
            link=li.find('a')
            ahref=link['href']

            category=link.text
            category=category.strip()
            category=category.lower()
            categoryFolder= './output/'+category
            try:
                os.mkdir(categoryFolder)
            except:
                print('dossier exsiste déja')


   
            ahref='https://books.toscrape.com/'+ahref
            books=getCategoryBooks(ahref,False)


            categoryImageFolder=categoryFolder+imageFolder

            saveImages(books,categoryImageFolder)

            print(category,'........................................',' '+ str(len(books)),' Livres.')
            

            with open(categoryFolder +'/'+ category +'.csv', 'w', newline='' , encoding='utf-8' ) as books_file:
                writer = csv.writer(books_file, quoting=csv.QUOTE_ALL,delimiter=';')
                writer.writerow(headers)
                writer.writerows(books)

