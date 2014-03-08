#coding=utf-8
from google.appengine.ext import db
import logging

#这里还是使用我之前的方式
#使用models代表数据库的内容
#用cmodels代表ORM模型

class Anime(db.Model):
    name = db.StringProperty(required=True)
    index = db.IntegerProperty(required=True)
    update_time = db.DateProperty(required=True)


class Model():
    u"""
    ORM模型
    """

    def __init__(self, thisdb = None):
        self.read_db = thisdb

    def insert(self):
        if not self.read_db:
            logging.log(logging.ERROR, self.__class__.__name__ + " is None")
            raise UnboundLocalError("db is None")
        read_db.put()

    def store(self):
        raise NotImplementedError("store not implement")

    def delete(self):
        if self.read_db:
            self.read_db.delete()
        else:
            raise UnboundLocalError("db is not implement")
