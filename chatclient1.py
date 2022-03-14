import socket
import threading
import sys

"""
Stop at Ctrl+Break
"""

PORT = 50000
BUFFSIZE = 4096

def server_handler(client):
    while True:
        try:
            data = client.recv(BUFFSIZE)
            print(data.decode("utf-8"))
        except:
            sys.exit()
    client.close()

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

host = input("Server to connect to : ")
if host == "":
    host = "localhost"

p = threading.Thread(target=server_handler, args=(client,))
p.setDaemon(True)

while True:
    msg = input("")
    client.sendto(msg.encode("UTF-8"), (host, PORT))
    if msg == "q":
        break

    if not p.is_alive():
        p.start()

client.close()