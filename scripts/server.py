import socket
#import rospy
rosbridge_port = 9090
local_ips = socket.gethostbyname_ex(socket.gethostname())
local_ip = local_ips[2][0]
for ip in local_ips[2]:
    if ip.startswith('192.'):
        local_ip = ip
        break
bcast_ip = local_ip[0:local_ip.rindex('.')+1]+'255'
print('local: ', local_ip)
print('bcast: ', bcast_ip)
bcast_socket=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bcast_socket.bind((bcast_ip,12345))
reply_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
reply_socket.bind((local_ip,12345))

local_ip_bytes = bytes(0)
for segment in local_ip.split('.'):
    local_ip_bytes = local_ip_bytes + int(segment).to_bytes(1,'big')

while True:
    m=bcast_socket.recvfrom(1024)
    if m[0].decode('ASCII') == 'ROS':
        reply_socket.sendto('ACK'.encode('ASCII')+local_ip_bytes+rosbridge_port.to_bytes(2,'big'),m[1])
