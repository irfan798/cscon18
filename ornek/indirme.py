# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 02:41:15 2018

@author: irfan
"""

import urllib.request

print('Dosya indiriliyor')

url = 'http://www.cekmekoy2023.com/_yuk/haberresim/heykel38.jpg'  
urllib.request.urlretrieve(url, 'heykel.jpg')