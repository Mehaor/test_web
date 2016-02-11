import SimpleHTTPServer
import SocketServer

PORT = 8000

handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), handler)

if __name__ == '__main__':
    print 'serving at port %s' % PORT
    httpd.serve_forever()
