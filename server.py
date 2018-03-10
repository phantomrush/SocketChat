# first of all import the socket library
import socket
import select
import threading
import random

class Server:
    c = []
    def __init__(self,maxClients,port,bufferLen):
        # next create a socket object
        self.s = socket.socket()
        self.c = []  # array of clients
        self.addresses = []  # array of addresses
        self.acceptor = ()  # accepts the client connections
        self.bufferinglen = bufferLen
        self.toclose = False
        self.clients_d = {}
        # reserve a port on your computer in our
        self.port = port
        self.numberOfClients = 0
        self.maxClients = maxClients
        self.clientsLeft = 0
        self.hostName = '0.0.0.0'

    def setting_server(self):
        tok = socket.gethostbyname(socket.gethostname())
        print(tok)
        tok = tok.split('.')
        token = self.token_generator(tok)
        print("Token is : ",token)
        self.s.bind((self.hostName, self.port))
        print( "socket binded to %s" %(self.port) )
        # put the socket into listening mode
        self.s.listen(self.maxClients)
        print( "socket is listening" )

    def clients_listener(self,amount):
        # a forever loop until we interrupt it or
        # an error occurs
        while self.numberOfClients < amount:
            # Establish connection with client
            self.acceptor = self.s.accept()
            self.c.append(self.acceptor[0])
            #c[-1].name = 'Client '+str(numberOfClients+1)
            self.addresses.append(self.acceptor[1])
            print( 'Got a connection ' )
            # send a thank you message to the client.
            self.c[-1].send(('Thank you for connecting').encode())
            self.numberOfClients+=1
        print( 'All online' )

    def send_message(self,client,message):
        clientMessageSend = self.clients_d[client.getpeername()[1]] + ' : ' + message
        for j in self.c:
            if j!=client:
                j.send(clientMessageSend.encode())

    def message_receiver(self):
        lastPeer = ""
        lastMessage = ""
        while True:
            if self.clientsLeft == self.maxClients:
                print('Closing chat')
                break
        #receiving messages from client

            ready_to_read, ready_to_write, in_error = select.select(self.c, [], [])
            for messager in ready_to_read:
                peerName = messager.getpeername()[1]
                try:
                    m = messager.recv(self.bufferinglen).decode()
                except:
                    print( self.clients_d[ peerName],'left')
                    self.c.remove(messager)
                    self.clientsLeft+=1
                    continue
                if peerName not in self.clients_d:
                    self.clients_d[ peerName] = m
                else:
                    print( self.clients_d[ peerName], ' : ', m )
                    t = threading.Thread(target=self.send_message(messager,m))
                    t.start()

    def token_generator(self,tok):
        l = len(tok)
        token = ""
        for i in range(l):
            num = int(tok[i])
            n = num//26
            d = num%26
            token+=chr(65+n)+chr(97+d)
        for i in range(1):
            num = random.randint(97, 122)
            n = num // 26
            d = num % 26
            token = chr(65 + n) + chr(97 + d) + token

        return token


myServer = Server(2,12345,1024)
myServer.setting_server()
myServer.clients_listener(2)
myServer.message_receiver()

for i in range(len(Server.c)):
    Server.c[i].close()
