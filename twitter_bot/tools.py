#!/usr/bin/python
#coding=utf-8
#FILENAME : __tools.py__ 
#DESCRIBE:

import datetime
import time

def str2datetime(str):
    ti = time.strptime(str, "%Y-%m-%d %H:%M")
    dt = datetime.datetime.fromtimestamp(time.mktime(ti))
    return dt
