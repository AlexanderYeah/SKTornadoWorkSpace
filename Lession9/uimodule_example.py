#coding=utf-8;
import  tornado.web
import tornado.ioloop
import  tornado.httpserver
import os

#设置
settings = dict (
    template_path = os.path.join(os.path.dirname(__file__),"templates"),
    static_path = os.path.join(os.path.dirname(__file__),"static")
)

# 图书模块 将参数传递进去
class BookModule(tornado.web.UIModule):
    def render(self, book):
        return self.render_string('book.html',book=book);

# 准备数据 传递进去数据
class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("index.html",books=[
            {
                "title":"How To Be a Better Man",
                "image":"static/images/1.jpg",
                "desc":"条理清晰,思维敏捷"
            },
            {
                "title": "Work Hard",
                "image": "static/images/2.jpg",
                "desc": "书中自有颜如玉"
            },
            {
                "title": "Listen To me",
                "image": "static/images/3.jpg",
                "desc": "书中自有黄金五"
            },
            {
                "title": "AY Class",
                "image": "static/images/4.jpg",
                "desc": "这是最后一本书"
            }

        ]);

# 实例化 app
app = tornado.web.Application([(r'/index',IndexHandler)],**settings,ui_modules={
    "Book":BookModule
});


if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(app);
    http_server.listen(8080);
    tornado.ioloop.IOLoop.instance().start();
