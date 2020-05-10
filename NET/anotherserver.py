'''
    Simple socket server using threads
'''

import socket
import sys
from thread import *

HOST = '' # Sybolic name, meaning all available interfaces
PORT = 8888   # Arbitrary no   n-privileged port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'

#Bind socket to local host and port
try:
        s.bind((HOST, PORT))
except socket.error as msg:
        print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()

print 'Socket bind complete'

#Start listening on socket
s.listen(10)
print 'Socket now listening'

# Function for handling connections, used to create threads
def clientthread(conn):
        # Send message to client
        conn.send('WE ARE THE FUN SERVER, HIT ENTER OR DIE\n')  # send only takes string

        while True:

            # receive from client
            data = conn.recv(1024)
            reply ='OK...' + data
            if not data:
                break

            conn.sendall(reply)

         # out of loop
        conn.close()


#now keep talking with the client
while 1:
        #wait to accept a connection - blocking call
        conn, addr = s.accept()
        print 'Connected with ' + addr[0] + ':' + str(addr[1])

        #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
        start_new_thread(clientthread ,(conn,))

s.close()
