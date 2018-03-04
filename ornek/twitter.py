# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 03:29:19 2018

@author: irfan
"""
#pip3 install python-twitter
#https://learnxinyminutes.com/docs/python3/

import twitter

api = twitter.Api(consumer_key='Consumer Key',
                      consumer_secret='Consumer Secret',
                      access_token_key='Access Token Key',
                      access_token_secret='Access Token Secret')


print(api.VerifyCredentials())

# Tweet Post
status = api.PostUpdate('#pwnlydays_python twitter bot !')
print(status.text)

# Get Users
users = api.GetFriends()
print([u.name for u in users])

# Get Timeline
timeline = api.GetHomeTimeline()
print([s.text for s in timeline])

# Get post a user
statuses = api.GetUserTimeline(screen_name="binitamshah")
print([s.text for s in statuses])