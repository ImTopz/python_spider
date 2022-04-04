#coding = utf-8
import json

import requests
import bs4
import re
import pandas as pd
import csv
import datetime

url='http://jwgl.sdust.edu.cn/app.do'
headers={
'Referer': 'http://jwgl.sdust.edu.cn/jsxsd/xsxj/xjxxgl.do?Ves632DSdyV=NEW_XSD_XJCJ',
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39'
}

def login(ac,pwd):
    post_data={
        "method" : "authUser",
        "xh" : ac,
        "pwd": pwd,
        "token":""
    }
    session=requests.session()
    req=session.get(url,headers=headers,params=post_data, timeout = 5)
    s=json.loads(req.text)
    headers["token"]=s["token"]
def get_grade(xh,sy=""):
    params = {
        "method": "getCjcx",
        "xh": xh,
        "xnxqid": sy
    }
    session=requests.session()
    req = session.get(url, params=params, timeout=5, headers=headers)
    print("全部成绩" if sy == "" else sy)
    s=json.loads(req.text)
    if s[0] != None:
        s = json.loads(req.text)
        for x in s:
            print("%s   %d   %s" % (str(x["zcj"]), x["xf"], x["kcmc"]))
    else:
        print("空")
def get_handle(params):
        session=requests.session()
        req = session.get(url, params = params ,timeout = 5 ,headers = headers)
        return req
def get_current_time():
    params = {
            "method" : "getCurrentTime",
            "currDate" : datetime.datetime.now().strftime("%Y-%m-%d")
        }
    req = get_handle(params)
    print(req.text)
    return req.text

def get_class_info(zc = -1,xh=""):
    s = json.loads(get_current_time())
    params={
            "method" : "getKbcxAzc",
            "xnxqid" : s["xnxqh"],
            "zc" : s["zc"] if zc == -1 else zc,
            "xh" : xh
        }
    req = get_handle(params)
    w=json.loads(req.text)
    for x in w:
        print("%s   %s   %s" % (str(x["jsmc"]), x["kssj"], x["kcmc"]))

def Server():
    print("您好")

if __name__=='__main__':
    a=input("请输入你的学号\n")
    b=input("请输入你的密码\n")
    login(a,b)
    get_grade(a,"")
    get_class_info(-1,a)

