import tornado.web
import tornado.options
import tornado.ioloop
import tornado.httpserver
import tornado.httpclient

from tornado.options import define, options

define("port", default=8080, type=int, help="nothing")


class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.web.gen.engine
    def get(self):
        # url = "https://www.baidu.com"
        url = "http://www.56.com/"
        client = tornado.httpclient.AsyncHTTPClient()

        response = yield tornado.httpclient.gen.Task(client.fetch, url)
        print(response)
        self.write("over")
        self.finish()


if __name__ == '__main__':
    print("http://localhost:8080")
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r"/", IndexHandler)]
    )

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
