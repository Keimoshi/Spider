import requests, bs4, os, re
import pandas as pd
from lxml import etree


class Universal(object):
    def __init__(self, url):
        self.url = url
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}

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
        print(soup.text)    #soup.text 只获取内容
        content = soup.find_all('p')
#        print(content)
        return

class Read_CSV(object):
    def __init__(self,path):
        self.path = path

    def Read_Content(self):
        fileName = self.path
        patch_Num = open(self.path,'r')
        data = []
        for line in patch_Num:
            data.append(list(line.strip().split(',')))
        print(data)

class write_CSV(object):
    def __init__(self,path):
        self.path = path

    def init_CSV(self):
        out = open('Patch.csv', 'a', newline='')
        csv_writer = csv_writer(out,dialect='excel')


if __name__ == '__main__':
    path = 'Patch-20181228.csv'
    name = 'RHSA-2018:3831'
    Redhat(path).getInfo()
#    Read_CSV(path).Read_Content()