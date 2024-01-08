import socket
import os
import time
import threading  # Add this line for threading support

import sys, errno  

print_lock = threading.Lock()


def handle_connection(c, addr):
    times = 10
    while times>0:
        try:  
            data = c.recv(1024)
        except IOError as e:  
            if e.errno == errno.EPIPE:  
                c.close()
                print("Pipe Error Address:", addr)
                return

        time.sleep(10)

        try:  
             c.send(data)
        except IOError as e:  
            if e.errno == errno.EPIPE:  
                c.close()
                print("Pipe Error Address:", addr)
                return
        
        times -= 1

    # connection closed
    c.close()
    print("Connection corresponding to address closed:", addr)


def Main():
    host = ""
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    print("socket bound to port", port)

    s.listen(5)
    print("socket is listening")
    while True:
        c, addr = s.accept()
        is_forked = os.fork()

        if is_forked == 0:
            s.close()
            handle_connection(c, addr)
            os._exit(0)

    s.close()


if __name__ == '__main__':
    Main()
