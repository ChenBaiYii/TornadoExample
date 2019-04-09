import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # name = self.get_argument("name", None)
        # name = self.get_query_argument("name", None)
        # print(name)

        # names = self.get_query_arguments("names")
        # self.write(str(names))
        pass

    def post(self, *args, **kwargs):
        # body = self.get_body_argument("body")
        # bodys = self.get_body_arguments("mark")
        head = self.request.headers.get("Content-Type")


        # self.write(f"hello {str(bodys)}")
        self.write(head)


if __name__ == '__main__':
    print("http://localhost:8080")
    app = tornado.web.Application(
        [(r"/", IndexHandler)]
    )
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()


