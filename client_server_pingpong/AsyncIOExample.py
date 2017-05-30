import socket


serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serversocket.bind(('0.0.0.0', 2632))

serversocket.listen()

while True:
    try:
        (clientsocket, address) = serversocket.accept()
        ip = clientsocket.recv(1024)
        recvd_number = int(str(ip.decode('utf-8')))
        clientsocket.send(bytes('{}'.format(recvd_number**2).encode('utf-8')))
        print("Sent message :: {}".format(recvd_number**2))
    except Exception as e:
        print(e)