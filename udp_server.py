import socket
port=2000
host=""
udp_server=socket.socket(type=socket.SOCK_DGRAM)
udp_server.bind((host,port))
while True:
    print("waiting for message")
    data,addr=udp_server.recvfrom(1024)
    print("recived form",data.decode(),"from",addr)
    msg=input("enter messgae")
    udp_server.sendto(msg.encode(),addr)
udp_server.close()
