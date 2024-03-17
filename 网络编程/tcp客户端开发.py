import socket

# 1.创建服务端套接字对象
tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2.和服务端套接字建立连接
tcp_client_socket.connect(('127.0.0.1', 8080))
# 3.发送数据
send_content = "你好，我是小白"
# 对字符串进程编码成为二进制数据
send_data = send_content.encode("utf-8")
tcp_client_socket.send(send_data)
# 4.接收数据
# 表示每次接收的最大字节数
recv_data = tcp_client_socket.recv(1024)
# 对二进程数据进行解码
recv_concat = recv_data.decode("utf-8")
print("接收服务端的数据:",recv_concat)
# 5.关闭套接字
tcp_client_socket.close()
