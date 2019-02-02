import requests
import bs4

res = requests.get('https://en.wikipedia.org/wiki/Artificial_intelligence')
soup = bs4.BeautifulSoup(res.text,'lxml') #parsing is done with with the help of lxml parser


for x in soup.select('.mw-headline'): #iteration based on ".mw-headline"  class , we use id(#) also html tags
	print(x.text)

