#!/usr/bin/python
#coding=utf-8
#FILENAME : __tools.py__ 
#DESCRIBE:

import datetime
import time
import urllib, urllib2
import json


def str2datetime(str):
    ti = time.strptime(str, "%Y-%m-%d %H:%M")
    dt = datetime.datetime.fromtimestamp(time.mktime(ti))
    return dt

def short_url(url):
    re_url = 'http://nxy.in/apis/shorten.aspx'
    dict = {'url':url,'user':'0','frame':'false'}
    req = urllib2.Request(re_url, urllib.urlencode(dict))

    ret = urllib2.urlopen(req).read()

    ret_obj = json.loads(ret)
    if ret_obj['Status'] == '200 OK':
        return ret_obj['ShortUrl']
    else:
        return None
