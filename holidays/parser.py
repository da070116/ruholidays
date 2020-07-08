import requests
from bs4 import BeautifulSoup


def find_holidays(source):
    soup = BeautifulSoup(source, 'lxml')
    days = soup.find_all('li', class_='full')
    for d in days:
        print(d.findChild('span', class_="dataNum").findChild('span', class_="number").text,
              d.findChild('span', class_="dataNum").findChild('span', class_="title").text,
              d.findChild('span', class_="caption").findChild('a').text
              )


class SiteParser:
    HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    }

    def __init__(self):
        self.holidays_list = []
        self.URL_ADDRESS = f'https://www.calend.ru/holidays/russtate/'
        try:
            _index_page = self.get_html(self.URL_ADDRESS)
            if 200 == _index_page.status_code:
                find_holidays(_index_page.text)
            else:
                print(f"Can't parse this page due to {_index_page.status_code}")
        except requests.exceptions.ConnectionError:
            print('An error with connection')

    def get_html(self, url: str, params=None) -> requests.models.Response:
        return requests.get(url, headers=self.HEADERS, params=params)
