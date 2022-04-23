import socket

def communicate(host, port, request):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.send(bytes(request, encoding='utf-8'))
    response = s.recv(1024)
    s.close()
    return response.decode('utf-8')
