import threading
import socket
import time


def send():
    udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    udp.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    udp.settimeout(0.2)
    while True:
        message = b"7pm Meet vandhudu. Please don't reply as no."
        udp.sendto(message, ('192.168.43.8', 37020))
        time.sleep(1)


def recieve():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('localhost', 9999))
    s.listen(1)
    while True:
        #port number can be anything between 0-65535(we usually specify non-previleged ports which are > 1023)
        clt, adr = s.accept()
        print(clt.recv(1024))


if __name__ == "__main__":
    # creating thread
    t1 = threading.Thread(target=send)
    t2 = threading.Thread(target=recieve)

    # starting thread 1
    t1.start()
    # starting thread 2
    t2.start()
