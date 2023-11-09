import socket

host = 'your host'
port = "your port"

servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor_socket.bind((host, port))

servidor_socket.listen(1)
print(f"Servidor escutando em {host}:{port}")
cliente_socket, cliente_endereco = servidor_socket.accept()
print(f"Conexão de {cliente_endereco}")

while True:
    msg = cliente_socket.recv(1024).decode()
    if msg:
        print(f"Mensagem recebida do cliente: {msg}")
    
    response = input("mensagem: ")
    cliente_socket.send(response.encode())

cliente_socket.close()
servidor_socket.close()
