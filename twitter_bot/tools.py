#!/usr/bin/python
#coding=utf-8
#FILENAME : __tools.py__ 
#DESCRIBE:

import datetime
import time
import urllib, urllib2
import json
import StringIO, gzip


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
    

def get_weekday():
    u"""
    获取今天的星期数，考虑到时区的问题，要加上8个小时
    """
    now = datetime.datetime.now()
    if now.hour + 8 > 23:
        i = now.weekday() + 1
    else:
        i = now.weekday()
    i = (i + 1) % 7
    return i


def tran2str(gzip_str):
    u"""
    呵呵
    """
    data = StringIO.StringIO(gzip_str)
    gzip_s = gzip.GzipFile(fileobj = data)
    actu = gzip_s.read()
    return actu
