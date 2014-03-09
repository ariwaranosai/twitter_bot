#!/usr/bin/python
#coding=utf-8
#FILENAME : __models.py__ 
#DESCRIBE:

import google_models as gdb
from google.appengine.ext import db
import logging
import tools

class Anime(gdb.Model):
    u"""
    用来记录动漫更新信息
    """

    #TODO把real_db的验证改成装饰器算了 

    def __init__(self, name = None, index = None, update_time = None, thisdb = None):
        self.real_db = thisdb
        self.name = name
        self.index = index
        self.update_time = update_time

    @staticmethod
    def check_used(name):
        query = gdb.Anime.all()
        query.filter('name =', name)
        result = query.fetch(5)
        if len(result) > 0:
            return True
        else:
            return False

    def store(self):
        if self.real_db:
            self.name = self.real_db.name
            self.index = self.real_db.index
            self.update_time = self.real_db.update_time
        
        query = gdb.Anime.all()
        if not self.name:
            raise NotImplementedError("do not have a name")

        query.filter('name =', self.name)
        result = query.fetch(5)

        if len(result) > 0:
            self.real_db = result[0]
            self.name = self.real_db.name
            self.index = self.real_db.index
            self.update_time = self.real_db.update_time

    def update(self):
        if self.real_db == None:
            self.store()
        
        if self.real_db == None:
            ani = gdb.Anime(name = self.name, index = self.index, \
                    update_time = self.update_time)
            ani.put()
            return


        self.real_db.name = self.name
        self.real_db.index = self.index
        self.real_db.update_time = self.update_time

        self.real_db.put()


    def get_update(self):
        if self.real_db == None:
            self.store()
        return self.update_time
