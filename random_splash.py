#! /usr/bin/python2

import urllib2
import json


CLIENT_ID = "" # Insert your Client ID HERE
COLLECTION_IDS = "145,658265,332,821,147,148,306253,142,855072,168631,256443,208422"  # Choose a random photo from a collection
URL = "https://api.unsplash.com//photos/random?client_id={}&collections={}".format(CLIENT_ID, COLLECTION_IDS)

r = urllib2.urlopen(URL)
r = json.load(r)   

print(r["urls"]["full"])
