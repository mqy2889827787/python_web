import socket
import threading
# def handle_client_request(client_socket, ip_port):


def deal_client(client_socket):
    receive_data = client_socket.recv(1000).decode()
    print(receive_data)
    receive_data.split()
    response_line = "HTTP/1.1 200 OK\r\n"
    response_header = "server:py1.0\r\n"
    f = open("./index.html", "rb+")
    responce_body = f.read()
    f.close()
    response_data = (response_line + response_header + "\r\n").encode() + responce_body
    client_socket.send(response_data)
    print("断开连接")
    # client_socket.close()


if __name__ == '__main__':
    sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sever_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, True)
    sever_socket.bind(("", 8998))
    sever_socket.listen(200)
    while True:
        client_socket, address = sever_socket.accept()
        # deal_client(client_socket)
        sub_thread = threading.Thread(target=deal_client, args=(client_socket, ))
        sub_thread.start()
