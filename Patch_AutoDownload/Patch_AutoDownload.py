import requests, bs4, os, re
import pandas as pd


class Universal(object):
    def __init__(self, url):
        self.url = url
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

    def getSoup(self, encode='utf-8', header=True):
        if header:
            res = requests.get(self.url, headers=self.headers)
        else:
            res = requests.get(self.url)
        res.raise_for_status()
        if encode != 'utf-8':
            try:
                res.encoding = encode
            except:
                print('[ERROR] fail to encoding.')
        theSoup = bs4.BeautifulSoup(res.text, 'html.parser')
        return theSoup

class Redhat(object):
    def __init__(self,name):
        self.name = name
        self.url = 'https://access.redhat.com/errata/'
#        self.path = path
        return

    def getInfo(self):
        self.contentList = []
        pageUrl = self.url + self.name
        soup = Universal(pageUrl).getSoup()
        print(soup)                                    #soup.text 只获取内容
        return

class Read_CSV(object):
    def __init__(self):
        self.path = path

    def Read_Content(self):
        csv_data = pd.read_csv(self.path)
        Advisory =


if __name__ == '__main__':
    name = 'RHSA-2018:3833'
    Redhat(name).getInfo()