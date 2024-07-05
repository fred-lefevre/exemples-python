import socket
import sys

sclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sclient.connect(('127.0.0.1', 54321))
except ConnectionRefusedError as e:
    print(f"Connexion refusée : {e}")
    sys.exit(1)

print(f"Serveur @IP = {sclient.getpeername()[0]}", end ='')
print(f" Port = {sclient.getpeername()[1]}")

print(f"Port utilisé = {sclient.getsockname()[1]}")

while True:
    try:
        txt = input("Message ? ")
        sclient.send(txt.encode())
        if txt.upper() == "FIN":
            break
        donnees = sclient.recv(4096)
        print(donnees.decode())
    except ConnectionResetError as e:
        print(f"Connexion abandonnée par le serveur : {e}")
        sys.exit(1)
sclient.close()

print("C'est fini ...")