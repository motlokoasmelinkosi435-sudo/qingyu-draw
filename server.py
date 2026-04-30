import http.server
import socketserver
import os

os.chdir(r'd:\360安全浏览器下载\NanoBananaPro-main')

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()
