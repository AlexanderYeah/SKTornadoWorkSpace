#coding=utf-8;

import tornado.web
import tornado.httpserver
import tornado.ioloop
import os
import tornado.gen



import time

"""
    先访问sleep，sleep 会阻塞now
    使用异步装饰器 和 异步生成器 解决此问题
    1> @tornado.web.asynchronous 是异步装饰器，可以在向改变其行为的方法上面加上装饰器
    使用异步装饰器的时候，tornado 不会自己关闭连接 需要显式的调用self.finish

    2> tornado.gen 模块,提供一个更为整洁的方式进行异步请求

    如下的方式，就不会进行阻塞

"""


class SleepHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self, *args, **kwargs):
        yield tornado.gen.Task(tornado.ioloop.IOLoop.instance().add_timeout,time.time()+5);
        self.write("when i sleep 5s");


class NowHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("i hope you see me now");


app = tornado.web.Application([("/sleep",SleepHandler),(r"/now",NowHandler)]);


if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(app);
    http_server.listen(8080);
    tornado.ioloop.IOLoop.instance().start();


