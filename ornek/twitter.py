# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 03:29:19 2018

@author: irfan
"""
#pip3 install python-twitter
#https://learnxinyminutes.com/docs/python3/

import twitter

api = twitter.Api(consumer_key='HxYX1P9MS0uxLMl4e3LQaCyEW',
                      consumer_secret='HS8T2ZtkxQHHfiGDxPKWMH3s2SGNpUKSIAijyzqVdIADqN9CxZ',
                      access_token_key='362514116-FiN45pQonlJLWCFl76wObB1GNJEpgxeFG3chsuYQ',
                      access_token_secret='i7LiQ29xw9vaEwQWG2yLWDbTERrIzTsY5MzAoxzL2sQgh')


api.VerifyCredentials()

# Tweet Post
#status = api.PostUpdate('#pwnlydays_python twitter bot !')
#print(status.text)

# Get Users
#users = api.GetFriends()
#print([u.name for u in users])

# Get Timeline
#timeline = api.GetHomeTimeline()
#print([s.text for s in timeline])

# Get post a user
statuses = api.GetUserTimeline(screen_name="bsronn")
print([s.text for s in statuses])
