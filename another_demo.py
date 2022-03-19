#coding = utf-8
import json

import requests
import bs4
import re
import pandas as pd
import csv


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
    # req.encoding='utf-8'
    # soup=bs4.BeautifulSoup(req.text,"html.parser")
    # table=soup.find("table")
    # results=table.find_all('tr')
    # rows=[]
    # rows.append(["课程","成绩","绩点"])
    # for  result in results:
    #     data=result.find_all("td")
    #     if(len(data)==0):
    #         continue
    #     class_name=data[3].getText()
    #     grade=data[4].getText()
    #     grade_s=data[8].getText()
    #     rows.append([class_name,grade,grade_s])
    # print(rows)
    # with open('grade.csv', 'w', newline='', encoding="utf-8") as f_output:
    #     csv_output = csv.writer(f_output)
    #     csv_output.writerows(rows)
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


if __name__=='__main__':
    a=input("请输入你的学号\n")
    b=input("请输入你的密码\n")
    login(a,b)
    get_grade(a,"")
