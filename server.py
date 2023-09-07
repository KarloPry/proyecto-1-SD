import socket

llave = 22
host = '148.220.209.32'
port = 12345

def main():
    print("Iniciando el servidor...")

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Esperando mensajes entrantes")
    while True:
        file_recieved = open("server-image-rcv.png", "wb")
        client_socket, client_address = server_socket.accept()
        print("Conexion establecida desde:", client_address)
        data = client_socket.recv(1024)
        while data:
            print(f"Recibiendo...") #Recibe los datos de la imagen mientras sigan existiendo
            file_recieved.write(data)
            data = client_socket.recv(1024)
        file_recieved.write(data) # Escribe los datos de la imagen encriptada en un archivo
        file_recieved.close()
        rf = open("server-image-rcv.png", "rb")
        recieved_file_content = rf.read() # Lee los contenidos del la imagen encriptada
        recieved_file_content = bytearray(recieved_file_content)
        for index, value in enumerate(recieved_file_content):
            recieved_file_content[index] = value ^ llave # Desencripta la imagen
        image_generated = open("server-image-rtv.png", "wb")
        image_generated.write(recieved_file_content) # Escribe la imagen desencriptada
        file_recieved.close()
        rf.close()
        image_generated.close()
        with open("server-image-rtv.png", "rb") as image_decrypted:
            client_socket.sendfile(image_decrypted) # Envia la imagen desencriptada de vuelta
        client_socket.shutdown(socket.SHUT_WR)
        client_socket.close()
        image_generated.close()


main()
