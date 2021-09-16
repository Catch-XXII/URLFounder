from bs4 import BeautifulSoup
import requests


class URLFounder(object):
    urls = set()  # Sets are unordered. Set elements are unique. Duplicate elements are not allowed.

    def __init__(self, url='https://www.nytimes.com/'):
        self.url = url
        self.start()

    def start(self):
        request = requests.get(self.url)
        soup = BeautifulSoup(request.text, "html.parser")
        for link in soup.find_all('a'):
            self.urls.add(link.get('href'))
        self.is_valid()

    def is_valid(self):
        for url in self.urls:
            if url.startswith('http'):
                request_response = requests.head(url)
                code = request_response.status_code
                up = code == 200
                if up:
                    print(f"Given {url} is {up} with status: {code}")
                else:
                    print(request_response, url)


if __name__ == '__main__':
    ny_times = URLFounder()
