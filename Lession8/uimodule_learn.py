#coding=utf-8;
import tornado.web
import tornado.ioloop
import tornado.httpserver
import os


settings = dict(

    template_path = os.path.join(os.path.dirname(__file__),'template')
)

class HelloHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("hello.html");

# 创建一个模块 供模板使用

class HelloModule(tornado.web.UIModule):
    def render(self, *args, **kwargs):

        return '<h1 style = "background-color: chocolate" >Hello,this is Alexander Yeah ! ! !</h1>'

# ui_module 字典中放对应的module
app = tornado.web.Application([(r"/hello",HelloHandler)],**settings,ui_modules={
    'Hello':HelloModule
});

if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(app);
    http_server.listen(8080);
    tornado.ioloop.IOLoop.instance().start();


