import socket

sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sever_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
sever_socket.bind(("", 9989))
sever_socket.listen(80)
while True:
    client_socket, client_address = sever_socket.accept()
    receive_data = client_socket.recv(1024).decode()
    print(receive_data)
    client_socket.send("71253735127".encode())
    # client_socket.close()
