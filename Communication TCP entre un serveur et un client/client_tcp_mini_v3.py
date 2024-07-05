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
txt = input("Message ? ")
try:
    sclient.send(txt.encode())
    donnees = sclient.recv(4096)
except ConnectionResetError as e:
    print(f"Connexion abandonnée par le serveur : {e}")
else:
    print(donnees.decode())
    sclient.close()

print("C'est fini ...")