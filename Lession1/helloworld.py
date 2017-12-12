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

"""
    下面的类是在tornado中应用最为广泛的继承与Tornado的RequestHandler 的类
    1> 该类中定义的get 方法 ，就是对HTTP的get 请求作出响应
    2> get_argument 即使查询字符串中取得参数greeting 的值，如果没有，返回第二个参数为默认的值
    3> write 方法 写到HTTP 的响应中去
    4> 参数handler 非常重要，是由元组组成的列表，每个元组的第一个元素是用来匹配正则表达式的
    第二个元素是是RequestHandler 的一个类
"""
class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # 如果参数中 有greeting 参数的话 会返回 用户输入的参数 否则返回Hello
        # http://localhost:8080/?greeting=fuck
        # 则 返回  fuckhello world
        greeting = self.get_argument('greeting','Hello');
        self.write(greeting + 'hello world');

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
    app = tornado.web.Application(handlers=[(r"/",IndexHandler)]);
    http_server = tornado.httpserver.HTTPServer(app);
    # 监听从命令行中输入的端口
    http_server.listen(options.port);
    tornado.ioloop.IOLoop.instance().start();




