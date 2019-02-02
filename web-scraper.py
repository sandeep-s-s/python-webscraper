import requests
import bs4

res = requests.get('https://en.wikipedia.org/wiki/Artificial_intelligence')
soup = bs4.BeautifulSoup(res.text,'lxml')


for x in soup.select('.mw-headline'):
	print(x.text)

	