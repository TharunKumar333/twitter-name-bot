# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 15:22:36 2020

@author: tharu
"""

import tweepy
import time
import os
#api key for twitter
def create_api():
    consumer_key = os.getenv('consumer_key')
    consumer_secret = os.getenv('consumer_secret')
    access_token = os.getenv('access_token')
    access_secret = os.getenv('access_secret')
    
    #simple code for tweeting
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    
    api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
    api.verify_credentials()
    print("API created")
    return api


def follower_count(users):
    emoji_number = {0:'0️⃣',1:'1️⃣',2:'2️⃣',3:'3️⃣',4:'4️⃣',5:'5️⃣',6:'6️⃣',7:'7️⃣',8:'8️⃣',9:'9️⃣'}
    uf_split = [int(j) for j in str(users.followers_count)]
    uf_emoji = ''.join([emoji_number[i] for i in uf_split if i in emoji_number.keys()])
    return uf_emoji

api = create_api()

while True:
    users = api.get_user('tharunk83794553')
    api.update_profile(name=f'Tharun Kumar|{follower_count(users)}')
    print(f'updating the profile name : Tharun Kumar {follower_count(users)} Followers')
    print('waiting to refresh')
    time.sleep(60)#refreshing for every 60 seconds



