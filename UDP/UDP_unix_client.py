import socket

sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)  # For unix
sock.sendto(b'Hello world!',  'unix.sock')
