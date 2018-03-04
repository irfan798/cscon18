# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 01:52:45 2018

@author: irfan
"""
#https://praw.readthedocs.io/en/latest/getting_started/quick_start.html

import praw
from pprint import pprint

reddit = praw.Reddit(client_id='1pb7nMM5hEeZYA',
                     client_secret='wDo_Gd1YgqUQl3Bm9Tq1Lh9hjP4',
                     user_agent='cscon18 / redditBot' )
                     
for submission in reddit.subreddit('wallpaper').hot(limit=1):
    #pprint(vars(submission))
    print(submission.preview["images"][-1]['resolutions'][-1]["url"])