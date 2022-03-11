import socket
import sys
import os
import time

'''
Since getloadavg() is used, it onlu works on Linux system.
'''

PORT = 50000
SLEEPTIME = 10

if os.name != "posix":
    print("It only works on UNIX-like systems.")
    sys.exit()

host = input("Server to connect to : ")

while True:
    client = socket.socket(socket.AF_INET, socket,socket.SOCK_STREAM)
    try:
        client.connect((host, PORT))
    except:
        print("Connection failed")
        sys.exit()
    loadave = os.getloadave()
    print(loadave)
    client.sendall(str(loadave).encode("utf-8"))
    client.close()
    time.sleep(SLEEPTIME)