import requests
from bs4 import BeautifulSoup
arquivo = 'trashisfor.txt'
number = 1
headers= {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
print ('let the scraping beggin')

for page in range(0, 3433):
    number = number + 1
    url = 'https://www.planetizen.com/news?_wrapper_format=html&page=' + str(number)
    html_page = requests.get(url, headers = headers)
    soup = BeautifulSoup(html_page.content, 'lxml')
    titles = soup.findAll('h3')
        for title in titles:
            print(title.text)
print ('end of scraping')