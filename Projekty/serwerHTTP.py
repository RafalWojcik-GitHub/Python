from BaseHTTPServer import HTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import os

os.chdir("sciezka/do_katalogu/z_danymi")
serv = HTTPServer(("",8888), SimpleHTTPRequestHandler)
serv.serve_forever()
