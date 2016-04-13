#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Twitter Bot Starter Kit: Bot 1

# This bot tweets three times, waiting 15 seconds between tweets.

# If you haven't changed credentials.py yet with your own Twitter
# account settings, this script will tweet at twitter.com/lacunybot

# Housekeeping: do not edit
import tweepy, time
from credentials import *
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)


# What the bot will tweet

tweetlist = ['Good Morning!', 'Started cold, but supposed to warm up as the day goes on.', 'Looking forward to learning more python today!']

for line in tweetlist: 
    api.update_status(line)
    print (line)
    print ('...')
    time.sleep(60) # Sleep for 60 seconds

print ("All done!")


