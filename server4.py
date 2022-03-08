import socket
import datetime

PORT = 50000
BUFFSIZE = 4096

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("",PORT))

server.listen()

while True:
    client, addr = server.accept()
    d = datetime.datetime.now()
    fname = d.strftime("%m%d%H%M%S%f")
    print(fname, "Connection Requests")
    print(client)
    fout = open(fname + ".txt", "wt")

    try:
        while True:
            data = client.recv(BUFFSIZE)
            if not data:
                break
            print(data.decode("UTF-8"))
            print(data.decode("UTF-8"), file=fout)
    except:
        print("Error occurred ""Abnormal end""")
        client.close()
        fout.close()