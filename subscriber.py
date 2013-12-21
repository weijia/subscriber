#!/usr/bin/python
import socket
import os
from private import host

SERVER_ADDR = ("%s"%host, 80)

def subscribe():
    sock = socket.create_connection(SERVER_ADDR)
    f = sock.makefile("r+", bufsize=0)

    f.write("GET /sub/my_channel_1 HTTP/1.0\r\n"
          + "Host: %s\r\n"%host    # you can put other headers here too
          + "\r\n")

    # skip headers
    #while f.readline() != "\r\n":
    #    pass

    # keep reading forever
    while True:
        line = f.readline()     # blocks until more data is available
        if not line:
            break               # we ran out of data!

        print line

    sock.close()

    
def del_ch():
    sock = socket.create_connection(SERVER_ADDR)
    f = sock.makefile("r+", bufsize=0)

    f.write('DELETE /pub?id=my_channel_1 HTTP/1.1\r\n'
          + "Host: www.zpadtech.com\r\n"    # you can put other headers here too
          + "\r\n"
          + "Hello World!")

    # skip headers
    #while f.readline() != "\r\n":
    #    pass

    # keep reading forever
    while True:
        line = f.readline()     # blocks until more data is available
        if not line:
            break               # we ran out of data!

        print line

    sock.close()
    
    
flag = False    
while True:
    subscribe()
    if flag:
        flag = False
        os.system('echo "1" > /sys/devices/platform/leds-gpio/leds/tp-link:blue:system/brightness')
    else:
        flag = True
        os.system('echo "0" > /sys/devices/platform/leds-gpio/leds/tp-link:blue:system/brightness')
    