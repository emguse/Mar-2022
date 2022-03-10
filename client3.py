import socket
import sys

HOST = 'localhost'
PORT = 50000
PATH = "data.txt"

fin = open(PATH, "rt")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((HOST, PORT))
except:
    print("Connection failed")
    sys.exit()

msg = fin.read()
client.sendall(msg.encode("utf-8"))

client.close()