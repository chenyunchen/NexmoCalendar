#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3 as lite
import sys
import datetime
import time
import requests
import urllib

con = lite.connect('/tmp/flaskr.db')

i = 1
while True:
    with con:

        cur = con.cursor()
        cur.execute("SELECT * FROM entries")

        rows = cur.fetchall()
        i=i+1
        print i

        for row in rows:
            DB_Time = row[2]+' '+row[3]
            Event = row[1]
            STime = row[3]
            api_key = ""
            api_secret = ""
            to = "+"
            lg = "zh-cn"
            urlencodetext =  urllib.urlencode({STime.encode('utf-8')+'有': Event.encode('utf-8')})
            print urlencodetext

            print STime
            print DB_Time
            LO_Time = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))
            print LO_Time

            if DB_Time == LO_Time:
                print 'OK'
                requests.post('https://rest.nexmo.com/tts/json?api_key='+api_key+'&api_secret='+api_secret+'&to='+to+'&text=%E6%82%A8%E5%A5%BD%EF%BC%8C%E5%9C%A8%E6%AD%A4%E6%8F%90%E9%86%92%E6%82%A8%EF%BC%8C%E6%82%A8%E5%B0%87%E5%9C%A8'+urlencodetext+'%E9%80%99%E5%80%8B%E4%BA%8B%E6%83%85%EF%BC%8C%E8%AC%9D%E8%AC%9D&lg='+lg)

            else:
                print 'Error'
        time.sleep(5)
