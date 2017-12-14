#coding=utf-8;

import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
import os

from tornado.options import define,options

define("port",default=8000,help="run on given port",type=int);

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # 渲染HTML
        self.render('index.html');

"""
render 函数传递关键字参数代替HTML 中 占位符
"""
class PoemPageHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        noun1 = self.get_argument("noun1");
        noun2 = self.get_argument("noun2");
        verb = self.get_argument("verb");
        noun3 = self.get_argument("noun3");
        self.render('poem.html',roads=noun1,wood=noun2,made=verb,difference=noun3);


if __name__ == '__main__':
    tornado.options.parse_command_line();

    """
    模板渲染 template_path 是告诉tornado 去哪里寻找模板文件。
    os.path.join(os.path.dirname(__file__),"html") 就是告诉tornado 去当前文件夹下面的html文件夹下面去寻找模板文件

    """

    app= tornado.web.Application(handlers=[(r'/',IndexHandler),
                                           (r'/poem',PoemPageHandler)
                                           ], template_path= os.path.join(os.path.dirname(__file__),"html"));
    http_server = tornado.httpserver.HTTPServer(app);
    http_server.listen(options.port);
    tornado.ioloop.IOLoop.instance().start();

