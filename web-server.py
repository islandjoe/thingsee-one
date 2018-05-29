#!/usr/bin/env python3
"""
Very simple HTTP server in python.

Usage::
    ./web-server.py
    
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
import simplejson

import datetime
import dropbox
import base64

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_POST(self):
        self._set_headers()
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))
        
        self.send_response(200)
        self.end_headers()
        
        dropbox_access_token = "0NjyWU0eglkAAAAAAAAdi_BBUnA0DCG5YmxTmJjrxyLDsjpOb_0V9f7R3v0uEwA0"
        client = dropbox.Dropbox(dropbox_access_token)
        timestamp = datetime.datetime.now()
        ts = timestamp.strftime("%y%m%d-%H%M%S")
        
        print("[UPLOAD] {}.json".format(ts))
        dropbox_base = "Thingsee_data"
        path = "/{base_path}/{timestamp}.json".format(base_path=dropbox_base, timestamp=ts)

        client.files_upload(self.data_string, path)
        
        return
        
def run(server_class=HTTPServer, handler_class=S, port=8082):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print('Starting httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
        
