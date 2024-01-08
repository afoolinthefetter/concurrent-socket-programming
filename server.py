import socket
from _thread import *
import threading
import time

print_lock = threading.Lock()


def threaded(c):
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
    print("socket binded to port", port)
 
    s.listen(5)
    print("socket is listening")
    while True:
 
        c, addr = s.accept()
 
        # lock acquired by client
        #print_lock.acquire()
        print('Connected to :', addr[0], ':', addr[1])
 
        # Start a new thread and return its identifier
        start_new_thread(threaded, (c,))
    s.close()

if __name__ == '__main__':
    Main()
