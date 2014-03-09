#!/usr/bin/python
#coding=utf-8
#FILENAME : __speak.py__ 
#DESCRIBE:这个文件来完成说话的逻辑
import logging
import tools



def speak(list):
    u"""
    完成语句生成部分
    """

    lines = []

    for item in list:
        name = item['name']
        index = item['index']
        update_time = item['update_time']
        #link = tools.short_url(item['link'])
        #if link == None:
        #    link = item['link']
        link = item['link']

        logging.log(logging.WARNING, str(type(link)))

        line = u'铛铛裆 《' + name + u'》 第' + str(index) \
                + u'话更新了' + u',想看请戳 ' + link
        lines.append(line)

    return lines
