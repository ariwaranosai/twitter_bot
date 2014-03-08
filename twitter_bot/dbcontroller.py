#coding=utf-8
u"""

"""
import models
from google.appengine.ext import db
import datetime,time
from bangumi import bangumi
import logging
import tools


#这里要注意一个问题，为了避免刷新时间过12点，导致的漏刷的现象，再起cron的进程的时候，要在12之前强刷一次.
def refresh():
    u"""
    刷新db中的anime数据
    """
    #获得今天已经更新的anime的list
    b_list = bangumi.get_bangumi_b()


    logging.log(logging.WARNING, "get b_list")

    result = []

    for anime in b_list:
        if not models.Anime.check_used(anime['name']):
            #如果已经有了
            anime_db = models.Anime(anime['name'],\
                    anime['index'], \
                    tools.str2datetime(anime['update_time']))
            anime_db.update()
            result.append(anime)

        else:
            anime_db = models.Anime(name=anime['name'])
            new_time = tools.str2datetime(anime['update_time'])
            if anime_db.get_update() < new_time:
                anime_db.update_time = new_time
                anime_db.update()
                result.append(anime)

    return result
























