# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 12:59:31 2018

@author: irfan
"""

import cscon18
import random
import praw

def karikatur_indir(hangi=0, rast=True):
    if rast:
        sayi = random.randint(100,1961)
    else:
        sayi = hangi
        
    site_adresi = "https://xkcd.com/" +str(sayi)+"/info.0.json"
    
    data = cscon18.site_oku(site_adresi)
    url = data["img"]
    resim_ismi = data["safe_title"] + ".png"
    
    cscon18.internetten_indir(url, resim_ismi)
    print(resim_ismi,"ni indirdim")
    
    
    
    
resim_ismi = "reddit_wallpaper.jpg"

reddit = praw.Reddit(client_id='1pb7nMM5hEeZYA',
                     client_secret='wDo_Gd1YgqUQl3Bm9Tq1Lh9hjP4',
                     user_agent='cscon18 / redditBot' )

for submission in reddit.subreddit('wallpapers').hot(limit=1):
    #pprint(vars(submission))
    resim_url = submission.preview["images"][-1]['resolutions'][-1]["url"]
    cscon18.internetten_indir(resim_url, resim_ismi)
    cscon18.arkaplan_degistir(resim_ismi)

#karikatur_indir(0,True)
