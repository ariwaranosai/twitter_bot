#coding=utf-8
u"""
twitter_bot conf.py
nks.sai
2013-3-4
配置运行环境以及twitter用户部分
"""

env = 'local'
proxy = '127.0.0.1:8087'

username = ''
passwd = ''

token_url = 'https://twitter.com/login'
login_url = 'https://twitter.com/sessions'
test_url = 'https://twitter.com/i/notifications?oldest_unread_id=0'
send_url = 'https://twitter.com/i/tweet/create'
