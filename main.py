from bs4 import BeautifulSoup
import requests

# w3schools python history url
url = requests.get('https://www.w3schools.com/python/python_intro.asp')

soup = BeautifulSoup(url.content, 'lxml')

text = soup.find('div', class_='w3-col l10 m12')

t_text = text.text

with open('history.html', 'w',encoding='utf-8') as file:
    file.write(str(t_text))