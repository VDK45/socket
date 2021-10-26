import socketserver


class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


class EchoTCPHandler(socketserver.BaseRequestHandler):

    def setup(self):  # есть в socketserver
        pass

    def handle(self):  # метод переопределен из socketserver
        data = self.request.recv(1024).strip()
        print(f'Address: {self.client_address[0]}')
        print(f'Data: {data.decode()}')
        self.request.sendall(data)

    def finish(self):  # есть в socketserver
        pass


if __name__ == '__main__':
    with ThreadingTCPServer(('0.0.0.0', 4545), EchoTCPHandler) as server:
        server.serve_forever()
