import socket


def start_server():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind(('127.0.0.1', 4000))
        server.listen(100)

        while True:
            client_socket, address = server.accept()
            data = client_socket.recv(1024).decode('utf-8')

            content = load_page_from_request(data)
            client_socket.send(content)
            client_socket.shutdown(socket.SHUT_WR)

    except KeyboardInterrupt:
        server.close()


def load_page_from_request(request_data):
    HDRS = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset = utf-8\r\n\r\n'
    HDRS_404 = 'HTTP/1.1 404 OK\r\nContent-Type: text/html; charset = utf-8\r\n\r\n'
    path = request_data.split(' ')[1]

    try:
        with open('views' + path, 'rb') as file:
            response = file.read()
        return HDRS.encode('utf-8') + response

    except FileNotFoundError:
        return (HDRS_404 + 'Error 404. Page not found').encode('utf-8')


if __name__ == '__main__':
    start_server()
