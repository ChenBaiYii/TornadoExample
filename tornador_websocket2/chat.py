import os
import tornado.web
import tornado.options
import tornado.ioloop
import tornado.httpserver
from tornado.websocket import WebSocketHandler


class ChatHandler(WebSocketHandler):
    users = []

    def open(self):
        for user in self.users:
            user.write_message(f" {self.request.remote_ip} 上线")
        self.users.append(self)

    def on_message(self, message):
        for user in self.users:
            user.write_message(f"{self.request.remote_ip} 说: {message}")
            print(self.request.remote_ip)

    def on_close(self):
        self.users.remove(self)
        for user in self.users:
            user.write_message(f"{user} 下线 ")

    def check_origin(self, origin):
        return True


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("message.html")


if __name__ == '__main__':
    print("http://localhost:8080")
    tornado.options.parse_command_line()
    settings = dict(debug=True,
                    template_path=os.path.join(os.path.dirname(__file__), "templates"),
                    static_path=os.path.join(os.path.dirname(__file__), "static"),
                    auto_reload=True
                    )

    app = tornado.web.Application([
        (r"/", IndexHandler),
        (r"/chat", ChatHandler)],
        **settings)

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(8080)
    tornado.ioloop.IOLoop.current().start()
