# Import socket module
import socket
import os
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
        self.ending_message = ''

    def connect_client(self):
        # connect to the server on local computer
        ipconfig = socket.gethostbyname(socket.gethostname())
        self.s.connect((ipconfig, self.port))
        self.s.send(self.connecting_message.encode())

    def receive_messages(self):
        while True:
            try:
                receive_data_server = self.s.recv(1024)
                a = receive_data_server.decode("utf-8")
                print(a)
            except:
                print(1)
                print(end='')
                break

    def send_messages(self):
        toclose = False
        while True:
            send_msg = input('Me : ')  # type in messages to send to server
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


#self,username,port
USER = 'User2'
meClient = client(USER,12345)
meClient.connect_client()
send_thread = threading.Thread(target=meClient.send_messages)
receive_thread = threading.Thread(target=meClient.receive_messages)
threads = [send_thread,receive_thread]
receive_thread.start()
send_thread.start()