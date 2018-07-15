#!/usr/bin/python

#########################################################################
#  Script: UDP-Echo-Server.py
#  Author: BrailinVMC
#  Created On: September 14th, 2017
#  Last Edited: October 29th, 2017 @ --:--:--, BrailinVMC
#  Description: This program is a server that allows a client to ping it over the network by. The server
#  decides whether to respond to the ping request or drop the packet. In case of response, the server
# responds with the client's sequence number and with the ping packets reception time.
#########################################################################
# Purpose: Serves as a server in a client-server architecture program for over the network pinging.
# Requirements: None.
# Method:
# Syntax:
# Notes: The program runs infinitely.
#########################################################################
# Import the socket module.
import socket

# Import the struct module.
import struct

# Import the random module.
import random

# Import time, sleep, localtime and strftime from the time module.
from time import time, sleep, localtime, strftime

# Set short sleep time.
wait = 0.25

#########################################################################
# CREATE A SERVER SOCKET
#########################################################################
# Create the server socket.
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set hostname.
serverName = ''

# Reserved port for the service.
port = 1543

# Bind the server socket at port <port>.
server.bind(('', port))

# Indicate server information.
print ('\nSERVER INFORMATION:'); sleep(wait)

# Server's socket type.
print ('\tSOCKET TYPE:\t\t\t' + str(server.type))

# Server's socket protocol.
print ('\tSOCKET PROTOCOL:\t\t' + str(server.proto))

# Server's socket address family.
print ('\tSOCKET ADDRESS FAMILY:\t\t' + str(server.family)); sleep(wait)

#########################################################################
# FUNCTION TO PROCESS REQUEST
#########################################################################
# Function to process a request.
''' def processRequest(request):
           return request '''
        
#########################################################################
# RECEIVE AND PROCESS REQUEST
#########################################################################
# Inform the user of that server is ready.
print ('\nService Ready to Receive on Port: '+ str(port));
print ('-----------------------------------------------'); sleep(wait)
    
# Continous Loop for Incoming Client Requests.
while True:
    # Receive request from clients.
    (clientMessage, (clientAddr, clientPort)) = server.recvfrom(8000)

    # Get the ping number -- 4-byte sequence number that identifies packet from client.
    unpackedSeqNum = struct.unpack('i', clientMessage)[0]

    # Create variable to store time when packet is received.
    receivedTime = time()

    # Create random number between 0 and 10.
    randNum = random.randint(0, 10)

    # Indicate client's IP Address from which request was received.
    print ('Client IP:\t\t\t' + clientAddr);
        
    # Drop request packet if random number generated in less than 4.
    if randNum < 4:
        print ('\tDropped ping request with sequence number ' + str(unpackedSeqNum) + ' received at '
                    + str(receivedTime))
          
        continue
    else:
        # Indicate the request being serviced.
        print ('\tResponding to ping request with sequence number ' + str(unpackedSeqNum) + ' received at '
                    + str(receivedTime))

        # Pack client's sequence number and time packet was received -- 4-byte + 8-byte.
        requestResp = struct.pack('id', unpackedSeqNum, receivedTime)

        # Respond to request from client.
        server.sendto(requestResp, (clientAddr, clientPort))
