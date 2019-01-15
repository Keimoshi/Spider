#coding:utf-8
import requests
from lxml import etree
import random

url='http://sz.ziroom.com/z/nl/z2.html'
def getReqHeaders():
    """
    功能：随机获取HTTP_User_Agent
    """
    user_agents=[
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"]
    user_agent = random.choice(user_agents)
    req_headers={
    'User-Agent':user_agent
    }
    return req_headers

html=requests.get(url,headers=getReqHeaders()).content
selector=etree.HTML(html)
infos=selector.xpath('//*[@id="houseList"]/li')
print(infos)



    #item['name']=name
    #item['address']=address
    #item['price']=price
    #list_dict.append(item)
#print list_dict

