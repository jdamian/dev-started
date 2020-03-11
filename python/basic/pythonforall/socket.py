# socket.SOCK_STREAM
# socket.SOCK_DGRAM

# socket.AF_UNIX, socket.AF_INET, socket.AF_INET6 

import socket

servidor = socket.socket()
servidor.bind(("localhost", 9999))
servidor.listen(10)
# cliente, (host_c, puerto_c) = servidor.accept()
cliente, addr = servidor.accept()

while True:
    recibido = cliente.recv(1024)
    if recibido == "quit":
        break
    print("Recibido: ", recibido)
    cliente.send(recbido)

print("adios")

cliente.close
servidor.close
