# Import socket module
import socket
#import os
import getpass
import threading
# Create a socket object
class client:

    def __init__(self,username,port):
        # Create a socket object
        self.s = socket.socket()
        # Define the port on which you want to connect
        self.port = port
        self.username = username
        self.connecting_message = username
        self.ending_message = 'bye'

    def connect_client(self,token):
        # connect to the server on local computer
        ipconfig = self.connect_token(token)
        #print(ipconfig)
        self.s.connect((ipconfig, self.port))
        self.s.send(self.connecting_message.encode())

    def receive_messages(self):
        while True:
            try:
                receive_data_server = self.s.recv(1024)
                a = receive_data_server.decode("utf-8")
                print(a)
            except:
                #print(end='')
                #sos.system('cls')
                break

    def send_messages(self):
        toclose = False
        while True:
            send_msg = input()  # type in messages to send to server
            #print(end='\r')
            self.s.send(send_msg.encode())
            # close the connection
            if 'bye' == send_msg:
                toclose = True
                self.s.send(self.ending_message.encode())
                self.s.close()
                break
            if toclose:
                break
        self.s.close()

    def connect_token(self,token):
        tok = token[2:]
        l = len(tok)
        ip = ""
        for i in range(0,l,2):
            n = ord(tok[i])-65
            d = ord(tok[i+1])-97
            num = 26*n + d
            ip+=str(num) + '.'
        ip = ip[0:len(ip)-1]
        #print(ip)
        return ip


#self,username,port
USER = getpass.getuser()
token = input("Enter token : ")
meClient = client(USER,12345)
meClient.connect_client(token)
send_thread = threading.Thread(target=meClient.send_messages)
receive_thread = threading.Thread(target=meClient.receive_messages)
threads = [send_thread,receive_thread]
receive_thread.start()
send_thread.start()