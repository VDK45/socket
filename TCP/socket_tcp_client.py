import socket


mes = input('Введите сообщение: ').encode('utf-8')  # str -> byte
# mes = b'Hello world'  # send byte
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('79.105.112.50', 4545))

sock.send(mes)  # send byte 'localhost' or '127.0.0.1'

result = sock.recv(1024)
print(f'Responce: {result.decode("utf-8")}')
sock.close()
