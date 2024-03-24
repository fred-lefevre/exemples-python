import socket

IP_SERVEUR, PORT = '127.0.0.1', 54321

sclient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f"Serveur @IP = {IP_SERVEUR}", end ='')
print(f" Port = {PORT}")

txt = input("Message ? ")
sclient.sendto(txt.encode(), (IP_SERVEUR, PORT))

sclient.close()

print("C'est fini ...")