import socket

sclient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sclient.connect(('127.0.0.1', 54321))

print(f"Serveur @IP = {sclient.getpeername()[0]}", end ='')
print(f" Port = {sclient.getpeername()[1]}")

print(f"Port utilisé = {sclient.getsockname()[1]}")
txt = input("Message ? ")
sclient.send(txt.encode())
donnees = sclient.recv(4096)
print(donnees.decode())
sclient.close()

print("C'est fini ...")