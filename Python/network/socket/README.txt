import socket

host_name = socket.gethostname()
ip_address = socket.gethostbyname(HOSTNAME)
service_name = socket.getservbyport(PORT, 'tcp'|'udp')

socket.ntohl(1234) n - 网络 h - 主机 l - 长整型 s - 短整型
socket.htonl(1234)
socket.ntohs(1234)
socket.htons(1234)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.gettimeout()
s.settimeout(100)
