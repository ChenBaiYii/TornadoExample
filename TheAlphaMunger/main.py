import os
import random

import tornado.web
import tornado.ioloop
import tornado.httpserver
import tornado.options

from tornado.options import define, options

define("port", default=8080, help="run on the given port", type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("index.html")
        # self.write("hello world")


class MungedPageHandler(tornado.web.RequestHandler):
    @staticmethod
    def map_by_first_letter(text):
        mapped = dict()
        for line in text.split('\r\n'):
            for word in [x for x in line.split(' ') if len(x) > 0]:
                if word[0] not in mapped:
                    mapped[word[0]] = []
                mapped[word[0]].append(word)
        return mapped

    def post(self, *args, **kwargs):
        source_text = self.get_argument("source")
        text_to_change = self.get_argument("change")
        source_map = self.map_by_first_letter(source_text)
        change_line = text_to_change.split('\r\n')
        self.render("munged.html", source_map=source_map,
                    change_lines=change_line, choice=random.choice)


if __name__ == '__main__':
    print("http://localhost:8080")
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r"/", IndexHandler),
                  (r"/poem", MungedPageHandler)],
        template_path=os.path.join(os.path.dirname(__file__), "templates"),
        static_path=os.path.join(os.path.dirname(__file__), "static"),
        debug=True
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


