import http.server
import socketserver
import os

#搭建http简易服务
PORT = 80  #本地端口
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("正在运行--------")
    httpd.serve_forever()