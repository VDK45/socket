import socket


mes = input('Введите сообщение: ').encode('utf-8')  # str -> byte
# mes = b'Hello world'  # send byte
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(mes, ('79.105.46.244', 4545))  # send byte 'localhost' or '127.0.0.1'