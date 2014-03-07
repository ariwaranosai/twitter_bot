#coding=utf-8
from google.appengine.ext import db

class Anime(db.Model):
    name = db.StringProperty(required=True)
    index = db.IntegerProperty(required=True)
    update_time = db.DateProperty(required=True)
