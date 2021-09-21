#based on code from Meenakshi Agarwal - https://www.techbeamers.com/create-python-irc-bot/
#shortlink: https://archive.st/ef60


from time import sleep

import feedparser

from irc_class import *
import os
import random
from datetime import datetime
from datetime import timedelta

from time import mktime



## IRC Config
server = ""  # Provide a valid server IP/Hostname
port = 6697
channel = "#test"
botnick = "testbot"
botnickpass = "guido"
botpass = "<%= @guido_password %>"
irc = IRC()
irc.connect(server, port, channel, botnick, botpass, botnickpass)

startdate = None
pollinterval = 5
currenttime = datetime.now()
nextpoll = datetime.now()+ timedelta(seconds=20)
hoursback = pollinterval

while True:
    currenttime = datetime.now()
    if currenttime > nextpoll:
        nextpoll = currenttime + timedelta(hours=pollinterval)
        print("whee")
        urls = ['https://example.com/feed',
                ]

        feeddata = {}
        for url in urls:
            feeddata[url] = feedparser.parse(url)
        feeds = {}

        for feed in feeddata:
            for post in feeddata[feed]['entries']:
                print(feeddata[feed]['feed']["title"])
                print(post["title"])
                print(post["published"])
                print(post["link"])
                posttime = datetime.fromtimestamp(mktime(post["published_parsed"]))
                if posttime > currenttime - timedelta(hours=pollinterval):
                    irc.send(channel, post["title"] + " - " + post["link"])


    try:
        text = irc.get_response()
        print(text)

      
        sleep(2)
    except KeyboardInterrupt:
        print("Ok ok, quitting")
        sys.exit(1)
    except:
        print("Something else went wrong")
