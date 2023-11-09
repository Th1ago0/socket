import socket

host = 'your host'
port = "your port"

cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente_socket.connect((host, port))

while True:
    msg = input("mensagem: ")
    cliente_socket.send(msg.encode())
    
    resposta = cliente_socket.recv(1024)
    if resposta:
        print(f"Resposta do host receptor: {resposta.decode()}")

cliente_socket.close()
