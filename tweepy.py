# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 15:22:36 2020

@author: tharu
"""

import tweepy
import time
#api key for twitter
def create_api():
    consumer_key = 'vvcJAGeurNsZRJC1rBkb7fT6U'
    consumer_secret = 'UfHfLU526sJwy1cgKX8hHr3i2tENZQA1rAp26lL4lewNB4ZDM7'
    access_token = '1283413173941399558-9LF5XD0ON00e1xVkqnUHF6ksOsMXRR'
    access_secret = 'S26YeK0dWboNeEoSq5MKFsKXNy8HcxxF0pkrQdP1dDJPf'
    
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
    time.sleep(5)

public_tweets = api.home_timeline()#thsi will take the first few tweets in your account 
for tweet in public_tweets:#and this will loop over the above tweets
    print(tweet.text)#and display the text


