#coding=utf-8;

import tornado.web
import tornado.httpserver
import tornado.ioloop
import os

from  uuid import uuid4

setting = dict(

    template_path = os.path.join(os.path.dirname(__file__),'templates'),
    static_path = os.path.join(os.path.dirname(__file__),'static')
)

# 购物车

class ShoppingCart(object):
    totalInventory = 10;
    callbacks = [];
    carts = {};


    def register(self,callback):
        self.callbacks.append(callback);

    # 加入购物车
    def moveItemToCart(self,session):
        if session in self.carts:
            return ;
        self.carts[session] = True;
        self.notifyCallBacks()

    # 移除购物车
    def removeItemToCart(self,session):
        if session not in self.carts:
            return ;

        del(self.carts[session]);
        self.notifyCallBacks()

    # 通知
    def notifyCallBacks(self):
        for c in self.callbacks:
            self.callbackHelper(c);

        self.callbacks = [];

    # 处理每一个回调结果
    def callbackHelper(self,callback):
        callback(self.getInventoryCount());

    # getInventoryCount
    def getInventoryCount(self):
        return self.totalInventory - len(self.carts);


# Detail handler  详情
class DetailHandler(tornado.web.RequestHandler):


    def get(self, *args, **kwargs):

        # 商品唯一的标志 传递给前端

        session = uuid4();
        count = self.application.shoppingCart.getInventoryCount();
        # 渲染到页面
        self.render("index.html",session = session,count = count);
        #self.render("index.html");

# CartHandler
# 购物车请求的处理

class CartHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        action = self.get_argument('action');
        session = self.get_argument('session');

        if not session:
            self.set_status(400);
            return ;

        if action == 'add':
            self.application.shoppingCart.moveItemToCart(session);
        elif action == 'remove':
            self.application.shoppingCart.removeItemToCart(session);
        else :
            self.set_status(400);


# 状态 监听
class StatusHandler(tornado.web.RequestHandler):
    # 异步装饰器

    @tornado.web.asynchronous
    def get(self, *args, **kwargs):
        self.application.shoppingCart.register(self.on_message);

    def on_message(self,count):
        self.write('{"inventoryCount":"%d"}' % count);
        # 显式的进行关闭
        self.finish();

class Application(tornado.web.Application):
    def __init__(self):
        self.shoppingCart = ShoppingCart();

        handlers = [(r"/",DetailHandler),(r"/cart",CartHandler),(r"/cart/status",StatusHandler)];
        global  setting;
        settings = setting;

        tornado.web.Application.__init__(self,handlers,**settings);


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write("Hi there");


if __name__ == '__main__':

    app = Application();
    http_server = tornado.httpserver.HTTPServer(app);
    http_server.listen(8080);
    tornado.ioloop.IOLoop.instance().start();
