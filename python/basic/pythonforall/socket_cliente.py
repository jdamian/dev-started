import socket

servidor = socket.socket()
servidor.connect(("localhost",9999))

while True:
    mensaje = raw_input("> ")
    servidor.send(mensaje)
    if mensaje == "quit":
        break
print("adios")
servidor.close