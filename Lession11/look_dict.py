#coding=utf-8;

import tornado.web
import tornado.ioloop
import tornado.httpserver
import os
import pymysql

# 单词查询  返回具体的含义 安装pymysql

settings = dict(
    template_path = os.path.join(os.path.dirname(__file__),"templates"),
    static_path = os.path.join(os.path.dirname(__file__),"static")

)

# index handler
class IndexHandelr(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):

        # 获取想要查询的单词

        target_word = self.get_argument("word",default= None);
        print(target_word);
        # 查询apple 的意思 并且返回
        # 获取光标
        cursor = self.application.db.cursor();
        # sql 语句
        sql1 = "SELECT * FROM look_dic WHERE word = '"+target_word+"'"
        # 执行sql语句
        cursor.execute(sql1);
        # 获取结果 一个数组 ((1, 'apple', 'we can eat'),)
        res = cursor.fetchall();
        # 取出对应要输出的结果 第0个元素 第2个
        desc_str = "The "+target_word+ " means----"+res[0][2];

        self.write(desc_str);

# app 初始化的时候 直接进行连接数据库
class Application(tornado.web.Application):
    def __init__(self):
        handers = [(
            (r"/index",IndexHandelr)

        )];

        settings =  dict(
            template_path = os.path.join(os.path.dirname(__file__),"templates"),
            static_path = os.path.join(os.path.dirname(__file__),"static")

        )
        # 直接连接数据库 数据库地址 用户名 密码 哪个数据库
        self.db = pymysql.connect("localhost","root","123456","tornado");

        tornado.web.Application.__init__(self,handers,**settings);



# main
if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(Application());
    http_server.listen(8080);
    tornado.ioloop.IOLoop.instance().start();







