import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 4545))
sock.listen(5)  # Сколько соединения
sock.setblocking(False)  # True = нет клиента дальше не идем
while True:
    try:
        client, addr = sock.accept()
    except KeyboardInterrupt:
        sock.close()
        break
    except socket.error:
        print('No client')

    else:
        client.setblocking(True)  # С клиентом в блок-ре:име
        result = client.recv(1024)
        client.close()
        print('Message: ',  result.decode('utf-8'))
