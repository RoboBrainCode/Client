from RoboBrainClient.RoboBrainAPI import RoboBrainAPI
import json

import re
import glob
import pprint


RoboAPIUserName = 'Robot Learning Member'
RoboAPIPass = 'PASS'
S3KEY = 'S3_KEY'
S3SECRET = 'S3_SECRET'

URL = "http://robobrain.me:3000/api/feeds/"


#Please change your user name
userHandle = 'userName'


# Login to API
rC = RoboBrainAPI(RoboAPIUserName ,RoboAPIPass,S3KEY,S3SECRET,userHandle)

#Populate feeds
for result in YourResults:
	rC.addFeed(data)

#Push Everything
rC.push2Brain(URL)

