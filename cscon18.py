# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 12:50:14 2018

@author: irfan
"""
import urllib.request
import ctypes
import os
import json

def internetten_indir(url, dosya_adi):
    print("indiriyorum")
    urllib.request.urlretrieve(url, dosya_adi)
    
def arkaplan_degistir(path):
    path = os.path.abspath(path)
    print(path)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)
    
def site_oku(url):
    with urllib.request.urlopen(url) as response:
        sonuc = response.read()
        return json.loads(sonuc.decode())