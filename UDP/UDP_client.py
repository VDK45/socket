import socket

mes = 'Привет! Hello world!'.encode('utf-8')  # str -> byte
# mes = b'Hello world'  # send byte
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(mes, ('79.105.253.141', 4545))  # send byte 'localhost' or '127.0.0.1'

x = 1
while x < 10:
    mes = input('Enter messenger: ').encode('utf-8')  # str -> byte
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(mes, ('localhost', 4545))  # send byte 'localhost' or '127.0.0.1'
    x += 1
