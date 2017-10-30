#!/usr/bin/python

#########################################################################
#  Script: UDP-Echo-Server.py
#  Author: BrailinVMC
#  Created On: September 14th, 2017
#  Last Edited: October 30th, 2017 @ --:--:--, BrailinVMC
#  Description: This program is a server that allows a client to communicate to it over the network. The
#  server reads the request as a sting and it's response is a string returned by the processRequest function.
#########################################################################
# Purpose: Serves as a server in a client-server architecture program for over the network communication.
# Requirements: None.
# Method:
# Syntax:
# Notes: The program runs infinitely.
#########################################################################
# Import the socket module.
import socket

# Import sleep, localtime and strftime from the time module.
from time import sleep, localtime, strftime

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
# Function to process a message.
def processRequest(request):
           return request.upper()
        
#########################################################################
# RECEIVE AND PROCESS REQUESTS
#########################################################################
# Continous Loop for Incoming Client Requests.
while True:

    # Inform the user of that server is ready.
    print ('\nREADY FOR USE');
    print ('------------------------------------------------------'); sleep(wait)

    # Indicate that the server is waiting for requests.
    print ('Waiting for request...\n')

    # Receive request from clients.
    (clientRequest, (clientAddr, clientPort)) = server.recvfrom(8000)

    # Decode request.
    clientRequest = clientRequest.decode()
    
    # Record date stamp.
    dateReceived = strftime('%b %dth, %Y', localtime())

    # Record time stamp.
    timeReceived = strftime('%H:%M:%S', localtime())

    # Indicate information about message source.
    print ('\nRECEIVED FROM:'); sleep(wait)
        
    # Client IP Address message was received from.
    print ('\tClient IP:\t\t\t' + clientAddr)

    # Client port message was received from.
    print ('\tClient Port:\t\t\t' + str(clientPort))

    # String length of message that was received.
    print ('\tString Length:\t\t\t' + str(len(clientRequest))); sleep(wait)

    # Sleep.
    sleep(wait)

    # Indicate information about when the message was received.
    print ('\nRECEIVED AT:'); sleep(wait)
        
    # Date on which message was received.
    print ('\tDate:\t\t\t\t' + dateReceived)

    # Time at which message was sent.
    print ('\tLocal Time:\t\t\t' + timeReceived); sleep(wait)

    # Sleep.
    sleep(wait)
        
    # Indicate content that was received.
    print ('\nCONTENT RECEIVED:'); sleep(wait)

    # Show content received.
    print ('\t' + clientRequest + '\n'); sleep(wait)

    # Process received message.
    newMessage = processRequest(clientRequest)

    # Send message from server to client.
    server.sendto(newMessage.encode(), (clientAddr, clientPort))
