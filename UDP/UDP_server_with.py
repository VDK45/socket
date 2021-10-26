import socket
'''
    Автоматом порт закрывается
'''
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    print('4545 is bind')
    sock.bind(('0.0.0.0', 4545))

    while True:
        result = sock.recv(1024)
        print('Message: ', result.decode('utf-8'))



