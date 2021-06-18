import autopep8
import requests
import re
import csv
import pandas as pd
import os

from bs4 import BeautifulSoup
from getCategory import getCategoryBooks


	try:
		os.mkdir(os.path.join(folder,''))
	except:
		print('dossier exsiste déja')
	
	

	for book in varBooks:
		
		imglink=book[9]
		imgUpc=book[1]
		imgArray=imglink.split('/')
		imgName=imgArray[len(imgArray)-1]
		imgNameArray=imgName.split('.')
		imgNameArray[0]=imgUpc
	
		imgName=imgNameArray[0]+'.'+ imgNameArray[1]
		
		response = requests.get(imglink)
		imgName=folder+ "/"+ imgName
		
		if response.ok:
		    with open(imgName, 'wb') as f:
		    	f.write(response.content)