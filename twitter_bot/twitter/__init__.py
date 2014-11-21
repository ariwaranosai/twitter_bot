#coding=utf-8
import login
import logging
login.init()
f = login.internal_login()
token = login.get_login_token(f)

logging.log(logging.WARNING, "token is" + str(token))

def sendMessage(msg):
    login.sendMessage(token, msg)
