import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options

from tornado.options import define, options

define("port", default=8080, help="run on the given port", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        cookie = self.get_secure_cookie("count")
        count = int(cookie) + 1 if cookie else 1
        count_string = "1 time" if count == 1 else "%d times" % count

        # self.set_secure_cookie("count", str(count), httponly=True, secure=True)
        # self.set_secure_cookie("count", str(count))
        self.set_cookie("count", str(count), httponly=True)
        self.write(
            '<html><head>'
            '<title>Cookie Counter</title>'
            '</head>'
            '<body>'
            '<h1>You’ve viewed this page %s times.</h1>' % count_string +
            '</body></html>'
        )


if __name__ == '__main__':
    print("http://localhost:8080")
    tornado.options.parse_command_line()

    settings = {
        "cookie_secret": "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
        "xsrf_cookies": True
    }

    app = tornado.web.Application([
        (r"/", MainHandler)
    ], **settings
    )

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
