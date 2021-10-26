import socket

while 1:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('79.105.253.141', 4545))  # IP, port
    mess = input('Enter message: ').encode('utf-8')
    sock.send(mess)
    sock.close()
    if mess == b'q':
        break
