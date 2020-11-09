import socket
import threading
import os

HEADER = 64
PORT = 9998
FORMAT = 'utf-8'
SERVER = "192.168.1.10"
ADDR = (SERVER, PORT)

PATH = "C:\\Chat\\lib\\info"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

msg = client.recv(1024).decode()

print(msg)

if os.path.exists(PATH + "\\email.txt") and os.path.exists(PATH + "\\username.txt") and os.path.exists(PATH + "\\password.txt"):

    bool = 'True'
    client.send(bool.encode(FORMAT))
    
    file = open(PATH + '\\username.txt', 'r')
    name = file.read()
    client.send(name.encode(FORMAT))
    print("You can messages:- ")

else:
    bool = 'False'
    client.send(bool.encode(FORMAT))
    
    sign_in_up = input("Enter whether you want to sign in or sign up(I/U resp.): ").upper()
    client.send(sign_in_up.encode(FORMAT))
    
    if sign_in_up == 'I':
        pass
    
    elif sign_in_up == 'U':
        os.chdir('C:\\')
        os.makedirs('Chat\\lib\\info')
        os.chdir(PATH)
        
        email_file = open('email.txt', 'w')
        password_file = open('password.txt', 'w')
        username_file = open('username.txt', 'w')
        
        email_input = input("Enter your email id: ")
        password_input = input("Enter your password: ")
        username_input = input("Enter your username: ")
        
        email_file.write(email_input)
        password_file.write(password_input)
        username_file.write(username_input)
        
        email_file.close()
        password_file.close()
        username_file.close()
        
        email_file = open('email.txt', 'r')
        password_file = open('password.txt', 'r')
        username_file = open('username.txt', 'r')
        
        name = username_file.read()
        client.send(name.encode(FORMAT))
    
    
    """
        file = open('name.txt', 'w')
        file.write("CLIENT")
        file.close()
        file = open('name.txt', 'r')
        name = file.read()
        client.send(name.encode(FORMAT))"""

    
#name = input("Enter your Username: ")
#client.send(name.encode(FORMAT))


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
