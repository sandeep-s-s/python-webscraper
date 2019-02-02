import requests
import bs4

res = requests.get('https://en.wikipedia.org/wiki/Artificial_intelligence')
soup = bs4.BeautifulSoup(res.text,'lxml') #parsing is done with with the help of lxml parser


for x in soup.find_all('a', href=True): #find_all is bs4 method , "a": anchor tag
	print(x['href'])

