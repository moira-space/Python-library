import socket
# 1.创建服务端套接字对象
# AF_INET:IPV4
# STREAM:tcp协议
tcp_server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2.绑定端口号
# 第一个参数表示ip地址，第二个参数表示端口号
tcp_server_socket.bind(("",8080))
# 3.设置监听
# 128表示最大等待连接数
tcp_server_socket.listen(128)
# 4.等待接受客户端的请求
# 注意点：当客户端和服务端建立连接成功都会返回一个新的套接字
# tcp_server_socket：只负责等待接收客户端的连接请求，收发消息不使用该套接字
new_clent,ip_port=tcp_server_socket.accept()
print("客户端的ip和端口号：",ip_port)
# 5.接收数据
# 收发消息都使用返回的这个新的套接字
recv_data=new_clent.recv(1024)
recv_content=recv_data.decode("utf-8")
print("接收客户端的数据为",recv_content)
# 6.发送数据
send_content="问题正在处理中。。。"
# 对字符串进行编码
send_data=send_content.encode("utf-8")
new_clent.send(send_data)
# 关闭服务与客户端套接字，表示和客户端终止通信
new_clent.close()
# 7.关闭套接字，表示服务端以后不再等待接收客户端的连接请求
tcp_server_socket.close()