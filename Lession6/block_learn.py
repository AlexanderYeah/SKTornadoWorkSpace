#coding=utf-8;

import tornado.web
import tornado.ioloop
import tornado.httpserver
import os


class IndexHander(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("index.html");

if __name__ == '__main__':
    app = tornado.web.Application(handlers=[(r"/index",IndexHander)]);
    http_server = tornado.httpserver.HTTPServer(app);
    http_server.listen(8080);
    tornado.ioloop.IOLoop.instance().start();

