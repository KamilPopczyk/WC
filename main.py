import requests
from bs4 import BeautifulSoup


def site_map(url: str):
    site = requests.get(url).text
    html_parser = BeautifulSoup(site, 'html.parser')
    site_domain = url.split('//')[-1].split('//')[0]    # separate domain from url

    print(site_domain)
    title = html_parser.find('title').text
    print(title)
    links = html_parser.find_all('a')
    print(links)
    links_set = set()   # storage for links
    for link in links:
        new_link = link.get('href')     # cut only links
        if new_link.startswith('/') \
                or new_link.startswith('http://' + site_domain) \
                or new_link.startswith('https://' + site_domain):    # filter links with domain

            links_set.add(new_link)

    # debuging print ;)
    print(links_set)


if __name__ == '__main__':
    site_map('http://0.0.0.0:8000')
