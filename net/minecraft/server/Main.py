print("Starting net.minecraft.server.Main")
import socket
import threading
import net.minecraft.util.logger.Logger as logger

HOST = "0.0.0.0"
PORT = 9999

logger.set_environment("Server thread")

clients = {}
lock = threading.Lock()


def broadcast(msg, exclude=None):
    dead_clients = []
    for client in list(clients):
        if client == exclude:
            continue
        try:
            if msg.endswith("/leave"):
                disconnect_client(client)
            else:
                client.sendall((msg + "\n").encode())
                logger.info(str(msg))
        except:
            dead_clients.append(client)
    for c in dead_clients:
        disconnect_client(c)

def disconnect_client(client):
    with lock:
        if client in clients:
            name = clients[client]
            broadcast(f"{name} left the game")
            del clients[client]
            try:
                client.close()
            except:
                pass

def handle_client(client):
    buffer = ""
    try:
        name = client.recv(1024).decode().strip()
        if not name:
            client.close()
            return
        with lock:
            clients[client] = name
        broadcast(f"{name} joined the game")
        while True:
            data = client.recv(1024)
            if not data:
                break
            buffer += data.decode()
            while "\n" in buffer:
                line, buffer = buffer.split("\n", 1)
                msg = line.strip()
                broadcast(msg)
    except:
        pass
    finally:
        disconnect_client(client)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((HOST, PORT))
    server.listen()
    while True:
        client, addr = server.accept()
        threading.Thread(target=handle_client, args=(client,), daemon=True).start()

start_server()