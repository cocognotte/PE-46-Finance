# code elouan

# import pandas as pd
# from bs4 import  BeautifulSoup as bs
# import urllib.request


# url='https://www.boursorama.com/bourse/indices/cours/1rPCAC/'

# page=urllib.request.urlopen(url,timeout=5)

# soup=bs(page,features="lxml")


import requests
import bs4
import urllib.request

url = 'https://fr.finance.yahoo.com/quote/%5EDJI/history?p=%5EDJI'

request = requests.get(url, headers = {'User-Agent':'Mozilla/.0'})

request_text = request.text
#print(request_text)

page = bs4.BeautifulSoup(request_text , "lxml")
#print(page)

def span_convert(bs):
    a = str(bs)[6:-7]
    if '\u202f' in a:
        a = a.replace('\u202f' , '')
        a = a.replace(',' , '.')
        return float(a)
    else:
        return a

L = []
c = 0

for item in page.find("table" , {'data-test' : "historical-prices"}).findAll('span')[7:-3]:
    if c%7 == 0:
        L.append([span_convert(item)])
    else:
        L[c//7].append(span_convert(item))
    c += 1
    
print(L)
