#coding=utf-8;

import tornado.web
import tornado.httpserver
import tornado.ioloop
import os

import tornado.httpclient
import urllib.parse
import urllib.request
import json
import datetime
import time



http_headers = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:57.0) Gecko/20100101 Firefox/57.0'}

"""
    下面的请求就是同步的,怎么理解
    当客户端先访问sleep 的时候，同时再有一个客户端访问now的话，那么第二个就要等待15s中，
    第一个客户端访问服务器就会挂起，等待访问完成，再去响应另外一个客户端的访问
"""

# 服务器收到客户端的请求之后 睡10秒 之后再去响应客户端
class SleepHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        time.sleep(10);
        self.write("i have to sleep 5s");

# 收到响应就立即反馈客户端
class NowHander(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("now you see me now now now");


app = tornado.web.Application([(r"/now",NowHander),(r"/sleep",SleepHandler)]);


if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(app);
    http_server.listen(8080);
    tornado.ioloop.IOLoop.instance().start();

