from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import requests

url  = "https://www.wikipedia.com"

#With urllib 

req = Request(url)
response = urlopen(req)
html = response.read()
print(html)
response.close()

#with requests

req = requests.get(url)
print(req.text)

#Extracting data with BeautifulSoup

url = 'https://www.python.org/~guido/'
soup = BeautifulSoup(requests.get(url).text)
print(soup.title)

#Importing from pokeapi
raw_url = "https://pokeapi.co/api/v2/pokemon/"
pokemon = "ditto"

url = raw_url+pokemon

r = requests.get(url)
pokedata = r.json()
print(pokedata['abilities'])

