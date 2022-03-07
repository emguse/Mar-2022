import socket
import datetime
import threading

'''
Implementation with IPv4/TCP
Returns the time to the client when a connection request is made
Stop at Ctrl+Break
'''

PORT = 50000
BUFFSIZE = 4096

def client_handler(client, client_no, msg):
    data = client.recv(BUFFSIZE)
    print("(", client_no, ")", data.decode("UTF-8"))
    client.sendall(msg.encode("UTF-8"))
    client.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("", PORT))

server.listen()

client_no = 0

while True:
    client, addr = server.accept()
    client_no += 1
    msg = str(datetime.datetime.now())
    print(msg, "Connection Requests(", client_no,")")
    print(client)

    p = threading.Thread(target=client_handler, args=(client, client_no, msg))
    p.start()