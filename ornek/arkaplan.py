# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 01:18:33 2018

@author: irfan
"""
import ctypes

def arkaplan_degistir(path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path , 0)