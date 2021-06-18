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
    