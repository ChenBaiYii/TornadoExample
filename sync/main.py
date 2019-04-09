import json
import urllib
import datetime
import time

import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.httpclient


from tornado.options import define, options

define("port", default=8080, type=int, help="nothing")


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        # query = self.get_argument('q')
        http_client = tornado.httpclient.HTTPClient()
        response = http_client.fetch("https://www.baidu.com/")
        print(response.body)

        self.write("hello world")


if __name__ == "__main__":
    print('http://localhost:8080')

    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()






