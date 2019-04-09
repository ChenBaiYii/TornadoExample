import os

import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options


from tornado.options import define, options

define("port", type=int, help="port!", default=8080)


class IndexHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        name = self.get_argument("name", "default")
        # self.write(f"hello {name}!")
        self.render("index.html")


class PoemPageHandler(tornado.web.RequestHandler):
    def post(self, *args, **kwargs):
        noun1 = self.get_argument("noun1")
        noun2 = self.get_argument("noun2")
        verb = self.get_argument("verb")
        noun3 = self.get_argument("noun3")
        self.render("poem.html", roads=noun1, wood=noun2, made=verb,
                    difference=noun3)


if __name__ == '__main__':
    print('http://localhost:8080')

    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[
        (r"/", IndexHandler),
        (r"/poem", PoemPageHandler)],
        template_path=os.path.join(os.path.dirname(__file__), "templates")
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

    a = "The Alpha Munger"


