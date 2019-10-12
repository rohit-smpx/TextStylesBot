import json
from http.server import BaseHTTPRequestHandler
from future.utils import bytes_to_native_str
from telegram import Update

from . import _bot as Bot

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        dispatcher, bot = Bot.get_handler()

        content_len = int(self.headers.get('Content-Length', 0))
        json_string = self.rfile.read(content_len)
        data = json.loads(json_string)
        update = Update.de_json(data, bot)
        dispatcher.process_update(update)

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write("ok".encode("utf-8"))
        return

    def do_GET(self):
        dispatcher, bot = Bot.get_handler()

        data = json.loads('{}')
        update = Update.de_json(data, bot)
        dispatcher.process_update(update)

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write("ok".encode("utf-8"))
        return
