import smtplib
import random
from cryptography.fernet import Fernet
import os

PATH = "E:\\Chat\\ImportantInfo"

file = open('key.key', 'rb')
key = file.read()

cipher = Fernet(key)

password_file = open('Pass_Enc.key', "rb")
data_enc = password_file.read()

password = cipher.decrypt(data_enc)

passwordr = password.decode()

def sendEmail(to, content):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('parthsinghrajput12@gmail.com', passwordr)
    server.sendmail('parthsinghrajput12@gmail.com', to, content)

    server.close()
    print('Check your email to get the OTP')


def get_random():
    global a
    n = random.randint(1000, 9999)

    for i in range(1000, 9999):
        if i == n:
            a = i
    return a


l1 = []
l1.append(get_random())

while True:

    #if os.path.exists(PATH + "email.txt"), :
        

    in_up_input = input("Enter whether you want to sign in or sign up: ")
    if in_up_input.upper() == "I":
        email_input = input('Enter Email: ')
        password_input = input('Enter Password: ')
        email_input = email_input + '\n'
        password_input = password_input + '\n'

        email_file = open('email_file.txt', 'r')
        password_file = open('password_file.txt', 'r')
        username_file = open('username_file.txt', 'r')

        email_list = email_file.readlines()
        password_list = password_file.readlines()
        username_list = username_file.readlines()

        if email_input in email_list:
            if password_list[email_list.index(email_input)] == password_input:
                print(username_list[email_list.index(email_input)])
                in_up_input = input(
                    "Enter whether you want to sign in or sign up: ")
                pass
            else:
                print('Wrong Password')

        else:
            print("Email not found")

    elif in_up_input.upper() == "U":
        email_file = open('email_file.txt', 'a')
        password_file = open('password_file.txt', 'a')
        username_file = open('username_file.txt', 'a')

        email_input = input("Enter your email address: ")
        password_input = input("Enter your password: ")
        username_input = input("Enter your Username: ")

        email_file.write(email_input + '\n')
        password_file.write(password_input + '\n')
        username_file.write(username_input + '\n')

        print("Your Account has been created!")
        sendEmail(email_input, 'You OTP ' + str(l1[0]))
        break
        
bool = True

while bool:
    inpu = input('Enter OTP: ')
    try:
        if int(inpu) == l1[0]:
            print('Valid OTP')
            if os.path.exists(PATH) == True:
                os.chdir(PATH)
                email_txt = open("email.txt", "w")
                password_txt = open("password.txt", "w")
                username_txt = open("username.txt", "w")
                email_txt.write(email_input)
                password_txt.write(password_input)
                username_txt.write(username_input)
            else:
                os.chdir("E:\\")
                os.makedirs("Chat\\ImportantInfo")
                os.chdir(PATH)
                email_txt = open("email.txt", "w")
                password_txt = open("password.txt", "w")
                username_txt = open("username.txt", "w")
                email_txt.write(email_input)
                password_txt.write(password_input)
                username_txt.write(username_input)
                        
            bool = False
        else:
            print('Invalid OTP')
            pass
    except:
        print('Invalid OTP')
        pass       
    




























##################################### Extra Requirements ###########################################################



#The formula for the total surface area of a right cone is T. S. A=πrl+πr2 . here, r is the radius and l is the slant height








