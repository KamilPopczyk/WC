import requests
from bs4 import BeautifulSoup


def site_map(main_url: str) -> dict:

    def site_parser(url: str):
        try:
            site = requests.get(url).text
        except requests.exceptions.RequestException as err:
            print('Error url: ', err)
            exit()

        html_parser = BeautifulSoup(site, 'html.parser')
        title = html_parser.find('title').text
        links = html_parser.find_all('a')
        links_set = set()   # storage for links
        for link in links:
            new_link = link.get('href')     # cut only links
            if new_link.startswith('/'):    # filter links with domain
                links_set.add('http://' + site_domain + new_link)   # make correct url
            if new_link.startswith('http://' + site_domain) or new_link.startswith('https://' + site_domain):
                links_set.add(new_link)

        site_map_dict[url] = {'title': title,
                              'links': links_set}

        for link in links_set:  # "We have to go deeper"
            if not site_map_dict.get(link):
                site_parser(link)

    # "global" variables
    site_domain = main_url.split('//')[-1].split('//')[0]  # separate domain from url
    site_map_dict = dict()
    site_parser(main_url)

    return site_map_dict



if __name__ == '__main__':
    answer = site_map('http://0.0.0.0:8000')
    print(answer)

