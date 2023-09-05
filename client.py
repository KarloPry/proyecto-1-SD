import socket
from encryption import Encryption
from pprint import pprint
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
    with open("retrieved_image.png", "wb") as retrieved_image:
        data = client_socket.recv(1024)
        while data:
            print(f"Recibiendo...")
            retrieved_image.write(data)
            data = client_socket.recv(1024)
    client_socket.close()
with open(original_image, "rb") as original_image_file:
    with open("retrieved_image.png", "rb") as retrieved_image_file:
        if original_image_file.read() == retrieved_image_file.read():
            print("Se regresó la misma imagen")
        else:
            print("La imagen no es la misma")

