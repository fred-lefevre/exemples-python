import socket

sserveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sserveur.bind(('127.0.0.1', 54321))
sserveur.listen(1)
while True:
    print(f"Attente d'un client ...")
    (sclient, adclient) = sserveur.accept()
    print(f"Conversation sur le port {adclient[1]}")
    donnees = sclient.recv(4096)
    print(donnees.decode())
    sclient.close()
sserveur.close()
