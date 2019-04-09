import tornado.web
import tornado.ioloop


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # name = self.get_argument("name")
        self.get_body_argument()
        name = "world!"
        self.write(f"hello {name}")





if __name__ == '__main__':

    print("http://localhost:8080")
    app = tornado.web.Application(
        [(r"/", IndexHandler)]
    )
    app.listen(8080)
    tornado.ioloop.IOLoop.current().start()
