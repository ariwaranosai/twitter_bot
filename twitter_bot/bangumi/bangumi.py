#coding=utf-8
#FILENAME : bangumi.py
#DESCRIBE:


import urllib,urllib2,json,time,StringIO,gzip
import datetime


#---------get data ---------------------


def get_bangumi_b():
    u"""
    从b站的某接口获取当天更新新番情况
    暂时只有当天已经更新的了
    有两个事情需要注意 
    1，服务器的时钟时区问题
    2，b站的数据都是gzip压缩的
    """
    url = 'http://www.bilibili.tv/index/bangumi.json'

    f = urllib2.urlopen(url).read()
    bangumi_str = tran2str(f)
    bangumi_obj = json.loads(bangumi_str)
    now = get_weekday()

    results = []

    for i in bangumi_obj:
        if i['weekday'] == now:
            link = 'http://www.bilibili.tv/sp/' + \
                    urllib.quote(i['title'].encode('utf-8'))
            if i['new'] == True:
                title = i['title']
                bgmcount = i['bgmcount']
                item = {'title':title, 'bgmcount':bgmcount}
                results.append(item)
    return results



#---------- tools -------------------

def get_weekday():
    i = datetime.datetime.now().weekday()
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
