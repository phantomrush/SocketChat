# Import socket module
import socket

# Create a socket object
s = socket.socket()

# Define the port on which you want to connect
port = 12345

# connect to the server on local computer
s.connect(('127.0.0.1', port))
s.send('Hi! I am client!!!')
toclose = False
while True:
    send_msg = raw_input('Client1 : ')#type in messages to send to server
    s.send(send_msg)
    # close the connection
    if 'bye' in send_msg:
        toclose = True
        s.send('bye')
        s.close()
        break
    if toclose:
        break
s.close()
