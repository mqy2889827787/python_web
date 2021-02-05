import socket
import multiprocessing
import sys

def deal_client(client_socket, address):
    print("用户IP地址为：", address)
    receive_data = client_socket.recv(100000)
    receive_data = receive_data.decode()
    print("报文：", receive_data)
    receive_list = receive_data.split()
    print("目标路径：", receive_list[1])
    target_path = receive_list[1]
    if target_path == "/":
        target_path = "/index.html"
    try:
        f = open("." + target_path, "rb+")
        file_data = f.read()
        f.close()
    except Exception as e:
        print("异常信息：", e)
        response_line = "HTTP/1.1 404 NOT FOUND\r\n"
        response_header = "Content-Type: text/html; charset=UTF-8\r\n"
        response_body = "对不起 你访问的页面不存在!!!"
        # 把没有找到相应的文件的这个信息发给浏览器
        response_data = response_line + response_header + "\r\n" + response_body
        client_socket.send(response_data.encode())
        client_socket.close()
    else:
        responce_line = "HTTP/1.1 200 OK\r\n"
        responce_head = "hello"
        f = open("." + target_path, "rb+")
        responce_body = file_data
        responce_data = (responce_line + responce_head + "\r\n").encode() + responce_body
        client_socket.send(responce_data)


def main():
    sever_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sever_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    sever_socket.bind(("", 8787))
    sever_socket.listen(100)
    while True:
        client_socket, address = sever_socket.accept()
        sub_mul = multiprocessing.Process(target=deal_client, args=(client_socket, address))
        sub_mul.start()


if __name__ == '__main__':
    main()
