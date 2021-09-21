# First client server program
# what to use:
# socket.socket(socket_family, type_socket, protocol=value)
# listen()
# bind()
# accept
# connect
# send
# recv
# sendto
# close()

import socket

# port > 1024
host = '127.0.0.1'
port = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print("connection done", addr)
        while True:
            data = conn.recv(1024)
            print("received....at server", repr(data))
            if not data:
                break
            conn.sendall(b'hello from server')
