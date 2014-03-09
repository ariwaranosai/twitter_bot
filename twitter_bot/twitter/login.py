#coding=utf-8
import urllib,urllib2
import cookielib
import re
import conf,user_conf
import logging
import json

def init():
    u"""
    用来初始化 urllib2，添加cookie以及可能的代理
    """
    cookie = cookielib.LWPCookieJar()
    cookie_handler = urllib2.HTTPCookieProcessor(cookie)

    opener = urllib2.build_opener(cookie_handler)
    #如果是本地话要挂代理
    if conf.env == 'local':
        proxy_handler = urllib2.ProxyHandler({'http':conf.proxy, 'https':conf.proxy})
        opener.add_handler(proxy_handler)
        logging.log(logging.WARNING, "proxy init")
        
    urllib2.install_opener(opener)
    logging.log(logging.WARNING, "init success")


def proxy_setting(proxy):
    u"""
    添加代理
    """
    proxy_opener = urllib2.build_opener( \
        urllib2.ProxyHandler({'http':proxy,'https':proxy}))

    urllib2.install_opener(proxy_opener)
    logging.log(logging.WARNING, "proxy init success")

def get_token(twitter_url = conf.token_url):
    u"""
    因为twiter在验证时，使用authenticity_token来验证浏览器行为
    ，所以要在login之前取到一个token
    """
    login_page = urllib2.urlopen(twitter_url).read()

    #现在观察到有两个authenticity_token，没发现区别，就直接用一个好了
    #TODO 正则匹配的方式可以改进
    re_str = ur'<input type="hidden" value="(?P<token>[0-9a-zA-Z]+)"'
    token_re = re.compile(re_str)
    l = token_re.findall(login_page)
    if len(l) > 0:
        return l[0]
    else:
        raise AttributeError

def internal_login(username = user_conf.username, passwd = user_conf.passwd):
    u"""
    真正的login函数 需要已经获取的token以及相应的POST结构
    POST结构
    session[username_or_email]:{username}
    session[password]:{passwd}
    authenticity_token:{token}
    scribe_log:
    redirect_after_login:
    authenticity_token:{token}
    remember_me:1
    """

    authenticity_token = get_token(conf.token_url)

    post = {
            'session[username_or_email]':username,
            'session[password]':passwd,
            'authenticity_token':authenticity_token,
            'scribe_log':'',
            'redirect_after_login':'',
            'remember_me':0
            }

    #TODO 伪装成浏览器
    request = urllib2.Request(conf.login_url, urllib.urlencode(post))
    login_html = urllib2.urlopen(request).read()

    return login_html

def get_login_token(html):
    u"""
    从登陆的页面中获得token
    """
    re_str = '<input type="hidden" value="(?P<token>[0-9a-zA-Z]+)" name="authenticity_token" class="authenticity_token">'
    token_re = re.compile(re_str)
    l  = token_re.findall(html)
    if len(l) > 0:
        return l[0]
    else:
        raise AttributeError

def sendMessage(token, str):
    u"""
    发送一条消息
    POST 格式
    authenticity_token:1845544c4cf766151440621c2bc0ba66c41a6622
    place_id:
    status:test
    """
    post = {
            'authenticity_token':token,
            'place_id':'',
            'status':unicode(str).encode('utf-8')
            }

    request = urllib2.Request(conf.send_url,urllib.urlencode(post))
    ret_json = urllib2.urlopen(request).read()

    #从返回的json中取出'message'
    json_obj = json.loads(ret_json)
    try:
        if json_obj['tweet_id'] != None:
            return True
        else:
            return False
    except:
        return False
