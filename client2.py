import socket
import sys

HOST = "localhost"
PORT = 50000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    client.connect((HOST, PORT))
except:
    print("Connection failed")
    sys.exit()

while True:
    msg = input("Enter a message to send : ")
    if msg == "q":
        break
    client.sendall(msg.encode("UTF-8"))

client.close()