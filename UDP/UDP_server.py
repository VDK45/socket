import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # AF_INET IP protocol version 4 / AF_INET6
sock.bind(('0.0.0.0', 4545))  # '127.0.0.1' Резервировать port 4545
result = sock.recv(1024)  # Принять 1024 байт
# print('Message in byte:', result)
# print('Message:', result.decode('utf-8'))
# sock.close()

while True:
    try:
        result = sock.recv(1024)  # Принять 1024 байт
    except KeyboardInterrupt:
        sock.close()
        break
    else:
        print('Message in byte:', result)
        print('Message:', result.decode('utf-8'))


