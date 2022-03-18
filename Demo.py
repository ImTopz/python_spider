
#coding = utf-8
import requests
import bs4
import re
import pandas as pd


url='http://jwgl.sdust.edu.cn/jsxsd/kscj/cjcx_list'
headers={
'Referer': 'http://jwgl.sdust.edu.cn/jsxsd/xsxj/xjxxgl.do?Ves632DSdyV=NEW_XSD_XJCJ',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39'
}
cookies={'JSESSIONID':'**********************8'}
def login():

    req=requests.get(url,headers=headers,cookies=cookies)
    req.encoding='utf-8'
    soup=bs4.BeautifulSoup(req.text,"html.parser")
    print(soup.find_all('tr'))



if __name__=='__main__':
    login()
