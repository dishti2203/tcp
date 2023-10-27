import socket
port=2000
host="localhost"
udp_client=socket.socket(type=socket.SOCK_DGRAM)
while True:
    data=input("enter data to be send:")
    if not data:
        break
    udp_client.sendto(data.encode(),(host,port))
    data,addr=udp_client.recvfrom(1024)
    if not data:
        break
    print("recived from:",data.decode())
udp_client.close()
