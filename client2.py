import socket

HEADER = 64
PORT = 9998
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECT"
SERVER = "192.168.1.10"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_len = str(msg_length).encode(FORMAT)
    send_len += b' ' * (HEADER - len(send_len))
    client.send(send_len)
    client.send(message)
    print(client.recv(1024).decode(FORMAT))

send("Hello World!")
input()
send("Hello World!")
input()
send("Hello World!")
input()
send(DISCONNECT_MSG)