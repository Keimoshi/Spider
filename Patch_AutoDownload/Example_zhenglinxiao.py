import requests, bs4, os, re


class Universal(object):
    def __init__(self, url):
        self.url = url
        self.headers = {}

    def getSoup(self, encode='utf-8', header=False):
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
    def __init__(self, name, path):
        self.url = 'https://access.redhat.com/errata/'
        self.name = name
        self.path = path
        return

    def getInfo(self):
        self.contentList = []
        pageUrl = self.url + self.name
        soup = Universal(pageUrl).getSoup()
        # Synopsis
        self.Synopsis = '[Synopsis]\n' + soup.select('#overview')[0].p.getText()
        self.contentList.append(self.Synopsis)
        print('[Success] Get Synopsis in ' + self.name)
        # Description
        overview = str(soup.select('#overview')[0])
        pattern = re.compile(r'Description.*\n.*')
        des = pattern.findall(overview)[0].replace('<br/>', '\n').replace('<li>', '').replace('</li>', '').replace(
            '<p>', '').replace('</p>', '').replace('Description</h2>\n', '').replace('</ul>', '').replace('<ul>', '')
        self.Description = '[Description]\n' + des
        self.contentList.append(self.Description)
        print('[Success] Get Description in ' + self.name)
        # Affected Products
        pattern = re.compile(r'<h2>Affected Products</h2>\n(.*\n)+<h2>Fixes</h2>', re.S)
        Products = pattern.findall(overview)[0].replace('<li>\n              ', '').replace('            </li>\n',
                                                                                            '').replace('<ul>\n',
                                                                                                        '').replace(
            '</ul>\n', '').replace('\n\n', '\n')
        self.AP = '[Affected Products]\n' + Products
        self.contentList.append(self.AP)
        print('[Success] Get Affected Products in ' + self.name)
        # Fixes
        ul = soup.select('ul')
        for u in ul:
            p = u.previous_sibling.previous_sibling
            try:
                if p.getText() == 'Fixes':
                    index = ul.index(u)
            except:
                pass
        FixesElements = ul[index].select('li')
        FixesList = []
        for fix in FixesElements:
            FixesList.append(fix.getText())
        self.Fixes = '[Fixes]\n' + '\n'.join(FixesList)
        self.contentList.append(self.Fixes)
        print('[Success] Get Fixes in ' + self.name)
        # Packages
        titleElements = soup.select('#packages')[0].select('h2')
        tableElements = soup.select('#packages')[0].select('table')

        for title in titleElements:
            if title.getText() == 'Red Hat Enterprise Linux Server 7' or title.getText() == 'Red Hat Enterprise Linux Server 6':
                index = titleElements.index(title)
                osType = title.getText()
        table = tableElements[index].getText().split('\n')
        text = []
        for line in table:
            if line.split() != []:
                text.append(' '.join(line.split()))
        self.Packages = '[Packages] ' + osType + '\n' + '\n'.join(text)
        self.contentList.append(self.Packages)
        print('[Success] Get Packages in ' + self.name)
        # Write in
        self.writein()

    def writein(self):
        fileName = self.name.replace(':', '-') + '.txt'
        content = '\n\n'.join(self.contentList).replace('\n\n\n', '\n\n')
        with open(self.path + fileName, 'w') as file:
            file.write(content)
        print('[Success] Write in.')


if __name__ == '__main__':
    name = 'RHSA-2018:3833'
    path = 'E:\Github\Practise\Pycharm\Patch_AutoDownload\Redhat'
    r = Redhat(name, path).getInfo()



