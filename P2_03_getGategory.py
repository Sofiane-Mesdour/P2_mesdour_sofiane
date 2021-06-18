import requests
import re
from bs4 import BeautifulSoup
from getBooksInPage import getPage
#url ='https://books.toscrape.com/catalogue/category/books/default_15/index.html'

def getCategoryBooks (url,root):
	
	urlBase=url[8:]

	categoryBooks=[]

	i=2
	j=5
	if root:
		j=2

	response = requests.get(url)
	
	while response.ok:
		books=getPage(url,root)
		categoryBooks= categoryBooks+getPage(url,root)
		url2=urlBase.split('/')
		url2[j]='page-'+str(i)+'.html'
		i=i+1
		url='https://'+ '/'.join(url2)
		response = requests.get(url)
		pass

	return (categoryBooks)

# test getCategoryBooks('https://books.toscrape.com/catalogue/category/books/travel_2/index.html',False)	
