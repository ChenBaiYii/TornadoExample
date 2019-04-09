import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
from uuid import uuid4

from tornado.options import define, options
define("port", default=8080, type=int, help='some help document!')


class ShoppingCart(object):
    total_inventory = 10
    callbacks = []
    carts = {}

    def register(self, callback):
        self.callbacks.append(callback)

    def move_item_to_cart(self, session):
        if session in self.carts:
            return
        self.carts[session] = True
        self.notify_callbacks()

    def remove_item_from_carts(self, session):
        if session not in self.carts:
            return
        del (self.carts[session])
        self.notify_callbacks()

    def notify_callbacks(self):
        for c in self.callbacks:
            self.callback_helper(c)
        self.callbacks = []

    def callback_helper(self, callback):
        callback(self.get_inventory_count())

    def get_inventory_count(self):
        return self.total_inventory - len(self.carts)


class DetailHandler(tornado.web.RequestHandler):
    def get(self):
        session = uuid4()
        count = self.application.shopping_cart.get_inventory_count()
        self.render("index.html", session=session, count=count)


class CartHandler(tornado.web.RequestHandler):
    def post(self):
        action = self.get_argument("action")
        session = self.get_argument("session")
        if not session:
            self.set_status(400)
            return
        if action == "add":
            self.application.shopping_cart.move_item_to_cart(session)
        elif action == "remove":
            self.application.shopping_cart.remove_item_from_carts(session)
        else:
            self.set_status(400)


class StatusHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.application.shopping_cart.register(self.on_message)

    def on_message(self, count):
        self.write('{"inventory_count": "%d"}' % count)
        self.finish()


class Application(tornado.web.Application):
    def __init__(self):
        self.shopping_cart = ShoppingCart()
        handlers = [
            (r"/", DetailHandler),
            (r"/cart", CartHandler),
            (r"/cart/status", StatusHandler)
        ]

        settings = {
            "template_path": "templates",
            'static_path': 'static'
        }

        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == '__main__':
    print("http://localhost:8080")
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


