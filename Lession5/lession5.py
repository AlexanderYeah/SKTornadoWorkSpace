#coding=utf-8;

import tornado.web
import os
import tornado.httpserver
import tornado.ioloop


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        path = self.get_argument("path",default=None);
        self.render("index.html");


"""
    提供静态文件 样式表 js 和图像不需要为每个文件编写独立的处理函数的静态内容。
    设置了 static_path 直接在html 中使用即可 如下：
    <link rel="stylesheet" href="{{static_url('index.css')}}">
"""
if __name__ == '__main__':
    app = tornado.web.Application(handlers=[(r"/index",IndexHandler)],
                                  template_path = os.path.join(os.path.dirname(__file__),'html'),
                                  static_path= os.path.join(os.path.dirname(__file__),'static'),
                                  debug = True,

                                  );

    http_server =  tornado.httpserver.HTTPServer(app);
    http_server.listen(8080);
    tornado.ioloop.IOLoop.instance().start();






