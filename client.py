import socket
llave = 22
with open("image-removebg-preview.png", mode="rb") as image:
    image_content = image.read(1024)
    image_content = bytearray(image_content)
    # for index, value in enumerate(image_content):
    #     image_content[index] = value ^ llave
    host = '127.0.0.1'
    port = 12345
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    message = [str(value) for value in image_content]
    client_socket.sendfile(image)
    client_socket.shutdown(socket.SHUT_WR)
    response = client_socket.recv(1024)
    print(f"Respuesta del servidor: {response}")
    client_socket.close()

