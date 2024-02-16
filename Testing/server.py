import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind(("localhost",1028))
s.listen(1)

while True:
    server, address = s.accept()
    data = server.recv(1024)
    server.send(data)
    server.close()