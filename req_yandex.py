import requests
from bs4 import BeautifulSoup #просто парсер

payloads = {'text':'чайник', 'lr': 149}
r = requests.get('https://yandex.ru/search/', params=payloads)
soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())

with open("result.txt", 'a') as file:
    for link in soup.find_all("a"):
        file.write(link.get('href')+'\n')