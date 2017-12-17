#coding =utf-8;

import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
import  os


class ControlHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        friut = self.get_argument("firstword",default="nothing");
        food = self.get_argument("secword",default="nothing");
        movie = self.get_argument("movie",default="nothing");

        self.render("control.html",friut=friut,food=food,movie=movie);



if __name__ == '__main__':
    app = tornado.web.Application(handlers=[(r"/favorite",ControlHandler)],template_path=os.path.join(os.path.dirname(__file__),"html"));
    http_server = tornado.httpserver.HTTPServer(app);
    http_server.listen(8012);
    tornado.ioloop.IOLoop.instance().start();





