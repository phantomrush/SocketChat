# first of all import the socket library
import socket
import select

# next create a socket object
s = socket.socket()
c = [] #array of clients
addresses = [] #array of addresses
acceptor = () #accepts the client connections
bufferinglen = 1024
toclose = False
print "Socket successfully created"

# reserve a port on your computer in our
port = 12345                
numberOfClients = 0

def setting_server():
    s.bind(('', port))
    print "socket binded to %s" %(port)

    # put the socket into listening mode
    s.listen(2)
    print "socket is listening"



def clients_listener(amount):
    global acceptor
    global numberOfClients
    # a forever loop until we interrupt it or
    # an error occurs
    while numberOfClients < amount:
        # Establish connection with client
        acceptor = s.accept()
        c.append(acceptor[0])
        #c[-1].name = 'Client '+str(numberOfClients+1)
        addresses.append(acceptor[1])
        print 'Got connection from', addresses[-1]
        # send a thank you message to the client.
        c[-1].send('Thank you for connecting')
        numberOfClients+=1
    print 'All online'

def message_receiver():
    while True:
        #receiving messages from client
        ready_to_read, ready_to_write, in_error = select.select(c, [], [])

        for messager in ready_to_read:
            m = messager.recv(bufferinglen)
            print 'Client ', messager, ' : ', m

setting_server()
clients_listener(2)
message_receiver()

for i in len(c):
    c[i].close()