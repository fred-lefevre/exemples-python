import socket

IP_SERVEUR, PORT = '127.0.0.1', 54321

sserveur = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sserveur.bind((IP_SERVEUR, PORT))

while True:
    print(f"Attente d'information ...")
    (donnees, adclient) = sserveur.recvfrom(4096)
    donnees = donnees.decode()
    print(f"Conversation sur le port {adclient[1]} : {donnees}")
    reponse = f"{len(donnees)} octets"
    sserveur.sendto(reponse.encode(), adclient)

sserveur.close()
