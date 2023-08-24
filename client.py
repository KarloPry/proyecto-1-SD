import socket
from encryption import Encryption
llave = 22
host = '127.0.0.1'
port = 12345
original_image = "original_image.png"
encrypted_image_path = Encryption(original_image).encrypt_image(llave)
with open(encrypted_image_path, "rb") as encrypted_image:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.sendfile(encrypted_image)
    client_socket.shutdown(socket.SHUT_WR)
    response = client_socket.recv(1024)
    print(f"Respuesta del servidor: {response}")
    client_socket.close()

