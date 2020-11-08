import socket
import threading

SERVER = '192.168.1.10'
PORT = 9998
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECT"

clients = []

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    name = conn.recv(1024).decode(FORMAT)

    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True

    while connected:
        msg = conn.recv(1024).decode()

        if msg == DISCONNECT_MSG:
            connected = False

        for i in clients:
            if i != conn:
                i.send(f"{name}: ".encode(FORMAT) + msg.encode(FORMAT))

    conn.close()


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        clients.insert(0, conn)
        clients[0].send("Welcome to the server".encode(FORMAT))
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


print("[STARTING] server is starting...")
start()
