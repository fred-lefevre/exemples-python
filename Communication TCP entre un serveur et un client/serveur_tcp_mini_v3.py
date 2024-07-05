import socket

sserveur = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sserveur.bind(('127.0.0.1', 54321))
sserveur.listen(1)
while True:
    print(f"Attente d'un client ...")
    (sclient, adclient) = sserveur.accept()
    print(f"Conversation sur le port {adclient[1]}")
    try:
        donnees = sclient.recv(4096)
    except ConnectionResetError as e:
        print(f"Connexion abandonnée par le client : {e}")
    else:
        print(donnees.decode())
        reponse = f"{len(donnees)} octets"
        sclient.send(reponse.encode())
        sclient.close()
sserveur.close()
