import socket

#TCP socket
s_tcp=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#UDP socket
s_udp=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(s_tcp)
print(s_udp)

