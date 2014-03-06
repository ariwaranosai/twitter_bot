#coding=utf-8
import login
login.init()
f = login.internal_login()
token = login.get_login_token(f)

def sendMessage(msg):
    login.sendMessage(token, msg)