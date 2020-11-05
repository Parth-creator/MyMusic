import socket
import threading

HEADER = 64
PORT = 9998
FORMAT = 'utf-8'
DISCONNECT_MSG = "!DISCONNECT"
SERVER = "192.168.1.10"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

msg = client.recv(1024).decode()

print(msg)

def input_msg():
    while True:
        i = input()
        client.send(i.encode(FORMAT))

thread = threading.Thread(target=input_msg)
thread.start()

def get_msg():
    while True:
        msg2 = client.recv(1024).decode()
        print(msg2)
    
thread2 = threading.Thread(target=get_msg)
thread2.start()