import socket

"""
Stop at Ctrl+Break
"""

PORT = 8080
BUFFSIZE = 4096
INDEX_HTML = "index.html"

fin = open(INDEX_HTML, "rt")
msg = fin.read()
fin.close()
msg = "HTTP/1.0 200 OK\n\n" + msg

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("", PORT))
server.listen()

while True:
    client, addr = server.accept()
    data = client.recv(BUFFSIZE)
    print(data.decode("UTF-8"))
    client.sendall(msg.encode("utf-8"))
    client.close()