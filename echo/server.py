#!/usr/bin/env python3

#########################################################################
#  Script     : server.py
#  Author     : BrailinsonDisla
#  Date       : July 17th, 2018
#  Last Edited: July 17th, 2018 @ ~ 22:00 , BrailinsonDisla
#########################################################################
# Purpose:
#    --
#
# Requirements:
#    None.
#
# Method:
#    None
#
# Syntax:
#    None
#
# Notes:
#    The program runs infinitely.
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
print ('\tSOCKET TYPE:\t\t' + str(server.type))

# Server's socket protocol.
print ('\tSOCKET PROTOCOL:\t' + str(server.proto))

# Server's socket address family.
print ('\tSOCKET ADDRESS FAMILY:\t' + str(server.family)); sleep(wait)

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
    clientRequest, (clientAddr, clientPort) = server.recvfrom(8000)

    # Decode request.
    clientRequest = clientRequest.decode()
    
    # Record date stamp.
    dateReceived = strftime('%b %dth, %Y', localtime())

    # Record time stamp.
    timeReceived = strftime('%H:%M:%S', localtime())

    # Indicate information about message source.
    print ('\nRECEIVED FROM:'); sleep(wait)
        
    # Client IP Address message was received from.
    print ('\tClient IP:\t\t' + clientAddr)

    # Client port message was received from.
    print ('\tClient Port:\t\t' + str(clientPort))

    # String length of message that was received.
    print ('\tString Length:\t\t' + str(len(clientRequest))); sleep(wait)

    # Sleep.
    sleep(wait)

    # Indicate information about when the message was received.
    print ('\nRECEIVED AT:'); sleep(wait)
        
    # Date on which message was received.
    print ('\tDate:\t\t\t' + dateReceived)

    # Time at which message was sent.
    print ('\tLocal Time:\t\t' + timeReceived); sleep(wait)

    # Sleep.
    sleep(wait)
        
    # Indicate content that was received.
    print ('\nCONTENT RECEIVED:'); sleep(wait)

    # Show content received.
    print ('\t' + clientRequest); sleep(wait)

    # Process received message.
    newMessage = processRequest(clientRequest)

    # Send message from server to client.
    server.sendto(newMessage.encode(), (clientAddr, clientPort))
