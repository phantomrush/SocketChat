# Import socket module
import socket

# Create a socket object
class client:

    def __init__(self,username,port):
        # Create a socket object
        self.s = socket.socket()
        # Define the port on which you want to connect
        self.port = port
        self.username = username
        self.connecting_message = username
        self.ending_message = 'Bye'

    def connect_client(self):
        # connect to the server on local computer
        ipconfig = socket.gethostbyname(socket.gethostname())
        self.s.connect((ipconfig, self.port))
        self.s.send(self.connecting_message.encode())
        toclose = False
        while True:
            send_msg = input('Me : ')  # type in messages to send to server
            self.s.send(send_msg.encode())
            # close the connection
            if 'bye' in send_msg:
                toclose = True
                self.s.send(self.ending_message.encode())
                self.s.close()
                break
            if toclose:
                break
        self.s.close()

#self,username,port
USER = input("Enter username: ")
meClient = client(USER,12345)
meClient.connect_client()
