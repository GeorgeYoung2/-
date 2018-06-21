from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

#####html = urlopen('http://pythonscraping.com/pages/page1.html')
#####print(html.read())
#####bsobj = BeautifulSoup(html.read(),'html.parser')
#####print(bsobj.h1)
#####print(bsobj.title)
#避免因为错误导致程序崩溃
def getTitle(url):
	try:
		html = urlopen(url)
	except HTTPError as e:
		#error = 'HTTP NOT FOUND'
		return None

	try:
		bsobj = BeautifulSoup(html.read(),'html.parser')
		title = bsobj.body.h1
		#title = bsobj.title
	except AttributeError as ae:
		return None
	return title

url = "http://www.pythonscraping.com/pages/page1.html"
title = getTitle(url)
if title == None:
	print('Title is not exist.')
else:
	print(title)
