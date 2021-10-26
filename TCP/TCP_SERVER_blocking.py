import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('0.0.0.0', 4545))
sock.listen(5)  # Сколько соединения
# sock.setblocking(False)  # True = нет клиента дальше не идем (Всегда блок)
sock.settimeout(5)  # Блок в 5 сек (0) == False (None) == True

while True:
    try:
        client, addr = sock.accept()
    except KeyboardInterrupt:
        sock.close()
        break
    except socket.error:
        print('No client')

    else:
        result = client.recv(1024)
        client.close()
        print('Message: ',  result.decode('utf-8'))
