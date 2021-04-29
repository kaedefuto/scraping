#classは予約語なのでclass_を使うこと

import requests
from bs4 import BeautifulSoup
r = requests.get ("https://xxxxxxxxxxxxxx")
soup = BeautifulSoup(r.content,"html.parser")
title = soup.title
#print(title)
#print(title.text)

div = soup.find("div",class_="readingContent01")
li = div.find("li")
#print(li.a["href"])
#print(li.a.text)


#全データを取得
"""
for li in div.find_all("li"):
  url = li.a["href"]
  date,text = li.a.text.split(maxsplit=1)
  print("{},{},{}".format(date,text,url))
"""

#タグの情報を取得する
"""
print(type(div))
print(div.name)#タグの名前を取得
class_=div["class"]#class属性の値を取得
print(class_)
"""

#キーワード引数での属性指定
tag = soup.find(id = "categoryNavigation")#id属性を指定して検索
print(tag.name)
tags = soup.find_all(id = True)#id属性があるタグを全て検索
print(tag.name)
