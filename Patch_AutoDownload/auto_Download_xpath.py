
import requests
import lxml.html


class ParseXpath:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
        }
        self.request = requests.get('https://access.redhat.com/errata/RHSA-2018:3833', headers=self.headers)

    def parse_xpath(self):
        content = self.request
        print(content)

if __name__ == '__main__':
    ParseXpath().parse_xpath()