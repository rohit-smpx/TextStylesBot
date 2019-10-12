import json
from http.server import BaseHTTPRequestHandler
from future.utils import bytes_to_native_str
from telegram import Update

from bot import get_handler

class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        dispatcher = get_handler()

        json_string = bytes_to_native_str(self.request.body)
        data = json.loads(json_string)
        update = Update.de_json(data, bot)
        dispatcher.process_update(update)

        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        self.wfile.write("ok")
        return
