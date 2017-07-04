#! /usr/bin/python2

import urllib2
import json
import random

def getRandomcollection(collections):
    return random.choice(collections)

CLIENT_ID = "" # Insert your Client ID HERE
COLLECTION_IDS = ["306253,208422"]  # Choose a random photo from a list of collections
URL = "https://api.unsplash.com//photos/random?client_id={}&collections={}".format(CLIENT_ID, getRandomcollection(COLLECTION_IDS))


r = urllib2.urlopen(URL)
r = json.load(r)   

print(r["urls"]["full"])
