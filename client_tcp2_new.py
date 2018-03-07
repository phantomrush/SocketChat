# Import socket module
import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 12345
ipconfig = socket.gethostbyname(socket.gethostname())

# connect to the server on local computer
username = "Rushali"
connecting_message = username
ending_message = 'Bye'
s.connect((ipconfig, port))
s.send(connecting_message.encode())
toclose = False
while True:
    send_msg = input('Me : ')#type in messages to send to server
    s.send(send_msg.encode())
    # close the connection
    if 'bye' in send_msg:
        toclose = True
        s.send(ending_message.encode())
        s.close()
        break
    if toclose:
        break
s.close()
