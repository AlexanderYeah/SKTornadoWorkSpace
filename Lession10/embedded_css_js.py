#coding=utf-8;

import tornado.web
import tornado.ioloop
import tornado.httpserver
import os


#setting
settings = dict(
    template_path = os.path.join(os.path.dirname(__file__),"templates"),
    static_path = os.path.join(os.path.dirname(__file__),"static"),
)

# module
class SampleModule(tornado.web.UIModule):
    def render(self, sample):
        return self.render_string("modules/sample.html",sample = sample);
    # 嵌入css
    # 方式一 ：额外加载css 样式 直接返回css 字符串的形式
    def embedded_css(self):
        return ".sample {background-color:red}";
    # 方式二 : 加载本地文件
    def css_files(self):
        return "sam_module.css";

    # 嵌入js
    # 方式一： 返回字符串 如下 在html 中 直接写入 div 标签
    def embedded_javascript(self):
        return "document.write(\"<div class='sample2'> 使用 embedded_javascript()方法写入 </div>\")";
    # 方式二: 在线引入js 做事情 例如jQuery
    def javascript_files(self):
        return "jquery-1.12.2.js";





# handler
class IndexHander(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("index.html",sample = "Happy New Year !!!");

#app
app = tornado.web.Application([(r"/index",IndexHander)],**settings,ui_modules={
    'Sample':SampleModule,
})


# server
if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(app);
    http_server.listen(8080);
    tornado.ioloop.IOLoop.instance().start();

