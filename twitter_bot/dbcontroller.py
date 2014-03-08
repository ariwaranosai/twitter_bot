#coding=utf-8
u"""

"""
import models
from google.appengine.ext import db
import datetime,time
from bangumi import bangumi


#这里要注意一个问题，为了避免刷新时间过12点，导致的漏刷的现象，再起cron的进程的时候，要在12之前强刷一次.
def Refresh():
    u"""
    刷新db中的anime数据
    """
    #获得今天已经更新的anime的list
    b_list = bangumi.get_bangumi_b()

    result = []

    for anime in b_list:
        if model.get_update_time(anime["title"]) \
            < str2datetime(anime['update_time']):
            result.append(anime)






















#--------------------------------这里往下是工具函数--------------------------
def str2datetime(str):
    ti = time.strptime(str, "%Y-%m-%d %H:%M")
    dt = datetime.datetime.fromtimestamp(time.mktime(ti))
    return dt