# coding=utf-8
__author__ = 'g7842'

#IP包的特点是按块发送，途径多个路由，但不保证能到达，也不保证顺序到达。
#TCP协议则是建立在IP协议之上的。TCP协议负责在两台计算机之间建立可靠连接，保证数据包按顺序到达。TCP协议会通过握手建立连接，然后，对每个IP包编号，确保对方按顺序收到，如果包丢掉了，就自动重发。

#客户端
import socket, time
#AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('www.sina.com.cn', 80))
# 发送数据:
s.send('GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
# 接收数据:
buffer = []
while True:
    # 每次最多接收1k字节:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = ''.join(buffer)

header, html = data.split('\r\n\r\n', 1)
print header
# 把接收的数据写入文件:
with open('_files/sina.html', 'wb') as f:
    f.write(html)

# 关闭连接:
s.close()

# 服务器
# 服务器进程首先要绑定一个端口并监听来自其他客户端的连接
# 如果某个客户端连接过来了，服务器就分配一个随机端口号与该客户端建立连接，随后的通信就靠这个端口了。服务器会打开固定端口（比如80）监听
# 但是服务器还需要同时响应多个客户端的请求，所以，每个连接都需要一个新的进程或者新的线程来处理，否则，服务器一次就只能服务一个客户端了。

import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口:
s.bind(('127.0.0.1', 9999))
s.listen(5)
print 'Waiting for connection...'


def tcplink(sock, addr):
    print 'Accept new connection from %s:%s...' % addr
    sock.send('Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if data == 'exit' or not data:
            break
        sock.send('Hello, %s!' % data)
    sock.close()
    print 'Connection from %s:%s closed.' % addr

while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()




# UDP
# 使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发数据包。但是，能不能到达就不知道了。
# 优点是和TCP比，速度快，对于不要求可靠到达的数据，就可以使用UDP协议


#服务端
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 绑定端口:
s.bind(('127.0.0.1', 9999)) #SOCK_DGRAM指定了这个Socket的类型是UDP

#绑定端口和TCP一样，但是不需要调用listen()方法，而是直接接收来自任何客户端的数据：
print 'Bind UDP on 9999...'
while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    print 'Received from %s:%s.' % addr
    s.sendto('Hello, %s!' % data, addr)


#客户端
#不需要调用connect()，直接通过sendto()给服务器发数据：
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in ['Michael', 'Tracy', 'Sarah']:
    # 发送数据:
    s.sendto(data, ('127.0.0.1', 9999))
    # 接收数据:
    print s.recv(1024)
s.close()
