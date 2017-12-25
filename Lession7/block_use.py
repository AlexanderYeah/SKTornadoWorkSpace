#coding=utf-8;

import tornado.web
import tornado.ioloop
import tornado.httpserver
import os

# 设置信息
setting = dict(

    template_path = os.path.join(os.path.dirname(__file__),"html")
)


# 这是主页面 写好样式 子页面可以直接继承主页面的样式
class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("main.html",header_con = "this is Main Page",footer_con = "this is Main footer");

class FirstSonHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("first_son.html",content = "this is first son page",footer_content = "this is footer");

class SecondSonHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("sec_son.html",content ="this is second page",footer_con = "this is second page");

app = tornado.web.Application([(r"/",IndexHandler),(r"/first",FirstSonHandler),(r"/second",SecondSonHandler)],**setting);




if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(app);
    http_server.listen(8080);
    tornado.ioloop.IOLoop.instance().start();


