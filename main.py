import requests
from bs4 import BeautifulSoup

def site_map(url: str):
    site = requests.get(url).text
    print(site)
    html_parser = BeautifulSoup(site, 'html.parser')
    title = html_parser.find('title').text
    print(title)

site_map('http://0.0.0.0:8000')
