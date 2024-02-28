import socket

sock = socket.socket(socket.AF_INET, socket.SOC_STREAM)
sock.bind(('192.168.1.12', 5555))
print('[+] Listening For The Incoming Connections')
sock.listen(5)
target, ip = sock.accept()
print('[+] Target Connected From: ' + str(ip))
target_communication()

