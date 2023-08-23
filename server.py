import socket
llave = 22
def main():
    print("Iniciando el servidor...")
    host = '127.0.0.1'
    port = 12345
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Esperando mensajes entrantes")
    f = open("server-image-rcv.png", "wb")
    while True:
        client_socket, client_address = server_socket.accept()
        print("Conexion establecida desde:", client_address)
        data = client_socket.recv(1024)
        while data:
            print(f"Recibiendo...")
            f.write(data)
            data = client_socket.recv(1024)
        f.write(data)
        f.close()
        rf = open("server-image-rcv.png", "rb")
        recieved_file = rf.read()
        recieved_file = bytearray(recieved_file)
        for index, value in enumerate(recieved_file):
            recieved_file[index] = value ^ llave
        image_generated = open("server-image-rtv.png", "wb")
        image_generated.write(recieved_file)
        f.close()
        response = ":)"
        rf.close()
        client_socket.send(response.encode('utf-8'))
        print("Terminado")
        client_socket.close()

main()