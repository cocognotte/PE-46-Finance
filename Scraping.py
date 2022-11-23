# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 15:16:20 2022

@author: eloua
"""

import pandas as pd
from bs4 import  BeautifulSoup as bs
import urllib.request


url='https://www.boursorama.com/bourse/indices/cours/1rPCAC/'

page=urllib.request.urlopen(url,timeout=5)

soup=bs(page,features="lxml")

soup

#test