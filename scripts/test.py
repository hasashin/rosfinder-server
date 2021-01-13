import socket

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
s.sendto('ROS'.encode('ASCII'),('192.168.1.255',21337))
m=s.recvfrom(1024)
message = m[0][0:3].decode('ASCII')
ip = '.'.join([str(int(m[0][3])),str(int(m[0][4])),str(int(m[0][5])),str(int(m[0][6]))])
port = int.from_bytes(m[0][7:], byteorder='big')

print('{} from {}:{}'.format(message, ip, port))