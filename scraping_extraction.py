# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 15:03:27 2022

@author: eloua
"""

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
    
#print(L)

def csv_write(TN,nom_fichier,separateur=';',decimal=','):
    '''Ecriture des données d'une liste de listes dans un fichier au format
    .csv pour utiliser dans un tableur.

    Paramètres d'entrée :
        - TN : liste de listes contenant des nombres. Chaque liste sera une
         ligne du tableur et chaque élément de chaque liste est une cellule du
         tableur
        - nom_fichier : chaine de caractère contenant le nom complet du fichier csv
        - separateur : séparateur entre les données numériques, par défaut ';'
        - decimal : caractère pour les décimaux dans le tableau, par défaut ','
    '''

    f=open(nom_fichier,'w')
    for S in TN:
        for N in S:
            N=str(N)
            N=N.replace('.',decimal)  #remplacement de '.' par ','
            f.write(N+separateur)
        f.write('\n') #fin de ligne après chaque liste
    f.close()

csv_write(L,"scrape1.csv")