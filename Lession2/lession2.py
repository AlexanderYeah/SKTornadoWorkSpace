#coding=utf-8;

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web


from tornado.options import define,options
define("port",default=12356,help="run on given port",type=int)
"""
    以上四个模块
    tornado.options 是从命令行读取设置
    如果一个与define语句中同名的设置在命令行中被给出，那么它将成为全局options的一个属性。
    如果用户运行程序时使用了--help选项
    程序将打印出所有你定义的选项以及你在define函数的help参数中指定的文本。
    如果用户没有为这个选项指定值，则使用default的值进行代替。
    Tornado使用type参数进行基本的参数类型验证，当不合适的类型被给出时抛出一个异常
    因此，我们允许一个整数的port参数作为options.port来访问程序。
    如果用户没有指定值，则默认为8000。

"""

# 1 就是讲 用户输入的字符串进行翻转 返回给用户就可以了
class ReverseHandler(tornado.web.RequestHandler):
    def get(self,input):
        # 对用户的输入 做一个 翻转操作 直接进行返回
        self.write(input[::-1])


# Toonado 支持任何合法的HTTP 请求 （GET POST PUT DELETE HEAD OPTIONS）

# 可以根据用户的输入，显性的设置状态码 set_status

"""
    输入 http://localhost:8084/index


    返回 ：my friend!!!,you caused a 405 error

"""

class WrapHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        text = self.get_argument('text',default=None);
        width = self.get_argument('width',default=40);

        if text is not None:
            # 如果传递参数 设置状态码为200
            self.set_status(200);
        else:
            # 不设置text 参数，直接返回404
            self.set_status(404);


# 当HTTP 请求错误发生的时候，Tornado 会向客户端发送一个状态码和错误信息的简短的片段
# 也可以使用write_error 方法在RequestHandler 中
class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        greeting = self.get_argument("greeting",default="Hello");
        self.write(greeting + "hello world");
    def write_error(self, status_code, **kwargs):
        self.write("my friend!!!,you caused a %d error" % status_code);





"""
    下面的代码是真正使得Tornado 运行起来的语句
    1> 第一步创建了一个Tornado 对的Application 类的实例，传递给类__init__方法最重要的参数handles
    它告诉了哪个类响应对应的请求
    2> 将App 对象 传递给HTTPServer 对象，对指定的端口进行监听
    3> 创建一个IOLoop 的实例
"""

if __name__ == '__main__':
    # 解析命令行的输入
    tornado.options.parse_command_line();
    app = tornado.web.Application(handlers=[(r"/reverse/(\w+)",ReverseHandler),
                                            (r"/wrap",WrapHandler),
                                            (r"/index",IndexHandler),
                                            ]);
    http_server = tornado.httpserver.HTTPServer(app);
    # 监听从命令行中输入的端口
    http_server.listen(options.port);
    tornado.ioloop.IOLoop.instance().start();




