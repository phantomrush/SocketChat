# first of all import the socket library
import socket
import select
import threading

# next create a socket object
s = socket.socket()
c = [] #array of clients
addresses = [] #array of addresses
acceptor = () #accepts the client connections
bufferinglen = 1024
toclose = False
print( "Socket successfully created" )
clients_d = {}
# reserve a port on your computer in our
port = 12345                
numberOfClients = 0
maxClients = 2
clientsLeft = 0
hostName = '0.0.0.0'

def setting_server():
    s.bind((hostName, port))
    print( "socket binded to %s" %(port) )
    # put the socket into listening mode
    s.listen(2)
    print( "socket is listening" )



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
        print( 'Got connection from', addresses[-1] )
        # send a thank you message to the client.
        c[-1].send(('Thank you for connecting').encode())
        numberOfClients+=1
    print( 'All online' )

def send_message(client,message):
    clientMessageSend = clients_d[client.getpeername()[1]] + ' : ' + message
    for j in c:
        if j!=client:
            j.send(clientMessageSend.encode())

def message_receiver():
    global clientsLeft
    lastPeer = ""
    lastMessage = ""
    while True:
        if clientsLeft == maxClients:
            print('Closing chat')
            break
    #receiving messages from client

        ready_to_read, ready_to_write, in_error = select.select(c, [], [])
        for messager in ready_to_read:
            peerName = messager.getpeername()[1]
            try:
                m = messager.recv(bufferinglen).decode()
            except:
                print( clients_d[ peerName],'left')
                c.remove(messager)
                clientsLeft+=1
                continue
            if peerName not in clients_d:
                clients_d[ peerName] = m
            else:
                print( clients_d[ peerName], ' : ', m )
                t = threading.Thread(target=send_message(messager,m))
                t.start()

setting_server()
clients_listener(maxClients)
message_receiver()

for i in range(len(c)):
    c[i].close()

#TODO chat history in clients on new lines