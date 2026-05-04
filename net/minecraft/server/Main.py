import socket
import sys
import threading

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 5555))
server.listen()

clients=[]

def handle_client(conn):
    while True:
        try:
            msg = conn.recv(1024).decode()
            print("Message received:",msg)
            for c in clients:
                c.send(msg.encode())
        except:
            clients.remove(conn)
            conn.close()
            break

print("Starting net.minecraft.server.Main")
while True:
    conn, addr = server.accept()
    print("Connected to:",addr)
    clients.append(conn)
    thread=threading.Thread(target=handle_client, args=(conn,))
    thread.start()