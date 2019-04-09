import tornado.httpserver
import tornado.web
import tornado.ioloop
import tornado.httpclient
import tornado.options


from tornado.options import define, options
define("port", type=int, default=8081)


class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self, *args, **kwargs):

        client = tornado.httpclient.AsyncHTTPClient()
        url = "https://www.baidu.com/"
        client.fetch(url, callback=self.on_response)



    def on_response(self, response):
        print(response.code)
        print('ok')
        self.write("over")
        self.finish()





if __name__ == '__main__':
    print('http://localhost:8081')
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r"/", IndexHandler)])

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()




