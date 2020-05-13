from urllib.request import urlopen
from bs4 import BeautifulSoup
import datetime
import random
import re


random.seed(datetime.datetime.now())

def get_links(articleUrl):
        html = urlopen("https://en.wikipedia.org{}".format(articleUrl))
        bs = BeautifulSoup(html, 'html.parser')
        return bs.find('div', {'id': 'bodyContent'}).find_all('a', href= re.compile('^(/wiki/)((?!:).)*$'))

links = get_links('/wiki/Ozon.ru')
while len(links) >0:
        newArticle = links[random.randint(0, len(links)-1)].attrs['href']
        print(newArticle)
        print("https://en.wikipedia.org/"+ newArticle)
        links = get_links(newArticle)
