import requests
import re
from bs4 import BeautifulSoup
from getBook import getBookDetails

#url =('https://books.toscrape.com/catalogue/category/books/mystery_3/page-2.html')

	pageBooks=[]

	response = requests.get(url)

	if response.ok:
	    
	    html =BeautifulSoup(response.text ,'lxml')
	    ol=html.findAll('ol')
	    ol=BeautifulSoup(str(ol),'lxml')
	    lis=ol.findAll('li')
	    n=len(lis)

	    for li in lis:
	    	
	    	link=li.find('a')
	    	ahref=link['href']
	    	    	
	    	if not root:
	    		ahref=ahref[8:]
	    	else:
	    		ahref=ahref[5:]
	    	
	    	ahref='https://books.toscrape.com/catalogue'+ahref