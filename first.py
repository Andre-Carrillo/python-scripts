from bs4 import BeautifulSoup
import requests

url='https://coinmarketcap.com/'

doc = requests.get(url)
soup = BeautifulSoup(doc.text, 'lxml')
# coins=soup.tbody.contents[0].find_all('a', class_="cmc-link")[1].text
for node in soup.tbody.children:
    try:
        row = node.find_all('a', class_='cmc-link')[1]
        print(row.text)
    except IndexError:
        print(node)
    # print(node)
