#!/usr/bin/python

#########################################################################
#  Script: UDP-Ping-Client.py
#  Author: BrailinVMC
#  Created On: October 29th, 2017
#  Last Edited: October 30th, 2017 @ --:--:--, BrailinVMC
#  Description: This program is a client that pings a sever at a specified IP Address and port over UDP.  The
#  client sends the server its sequence number and uses response to calculate OTT and RTT.
#########################################################################
# Purpose: Serves as a client in a client-server architecture program for over the network pinging.
# Requirements: None.
# Method: If arguments are given:
#                                                               # The first argument is considered as the server's IP Address.
#                                                               # The second argument is considered as the port.
# Syntax:
#                                                               # 1. UDP-Ping-Client.py
#                                                               # 2. UDP-Ping-Client.py <IP Address>
#                                                               # 3. UDP-Ping-Client.py <IP Address> <Port Number> 
# Notes: None.
#########################################################################
# Import the sys module.
import sys

# Import the socket module.
import socket

# Import the struct module.
import struct

# Import time, sleep, localtime and strftime from the time module.
from time import time, sleep, localtime, strftime

# Set short sleep time.
wait = 0.50

#########################################################################
# VERIFY FUNCTIONS
#########################################################################
# Check if the string provided is a valid IPv4 Address.
def verify_IPv4(ipv4):
    # Convert ipv4 to a string if possible.
    try:
        ipv4 = str(ipv4)
    except:
        # Return false if not possible.
        return False
    
    # Split the ipv4 string using '.' as the delimiter.
    ip_octet_list = ipv4.split('.')

    # Check the size of the ip_octet_list.
    if len(ip_octet_list) != 4:
        # Return false if there are not 4 octets.
        return False
    
    # Check that each octet is valid.
    else:
        for octet in ip_octet_list:
            # Check that each octet is an integer between 0 and 255.
            try:
                # Check if the octet is an integer.
                check = int(octet)

                # Check if octet is between 0 and 255.
                if (check < 0 or check > 255):
                    # Return false for octets out of range.
                    return False
            except:
                # Return false if an octet is not an integer.
                return False
    # Return true if the string defines a valid IPv4 Address.
    return True

#########################################################################
# DEFAULT ADDRESS SERVER INFO
#########################################################################
# Print header to inform the user of the default settings.
print ('DEFAULT SETTINGS FOR SERVER:'); sleep(wait)

# Set the default server IP Address and inform the user.
server_ip = '127.0.0.1'
print ('\tServer IP:\t\t\t' + server_ip)

# Set the default server port and inform the user.
server_port = 1543
print ('\tServer Port:\t\t' + str(server_port)); sleep(wait)

#########################################################################
# CHECK FOR SYSTEM ARGUMENTS
#########################################################################
# Store bool for args.
argsBool = False

# Store command line arguments.
args = sys.argv

# Store length of arguments list.
argsLength = len(args)

# Reserve variable for error message.
error = ''

# Check if arguments have been provided - for IP Address.
if argsLength > 1:
    # Change argsBool status.
    argsBool = True
    
    # Set the error.
    error = 'IP ADDR ARG ERROR' # The IP Address provided in the arguments is invalid.
    
    # Set temp_ip to first argument.
    temp_ip = args[1]
    
    # Verify if IP Address provided is valid.
    if verify_IPv4(temp_ip):
        # Inform user that IP Address has been chaned by argument.
        print ('IP ADDR CHANGED by ARG')

        # Change server_ip.
        server_ip = temp_ip

        # Change argsBool status.
        argsBool = True
    else:
        # Print error if IP Address is invalid.
        print (error)

# Checks if arguments have been provided - for port.
if argsLength > 2:
    # Set the error.
    error = 'PORT ARG ERROR' # The port provided in the arguments is invalid.

    # Set temp_port to second argument.
    temp_port = args[2]
    
    # Verify if port provided is valid.
    try:
        temp_port = int(temp_port)

        if temp_port >= 0 and temp_port <= 65536:
            # Inform user that port has been chaned by argument.
            print ('PORT CHANGED by ARG')

            # Change server_port.
            server_port = temp_port

            # Change argsBool status.
            argsBool = True
        else:
            # Raise error to execute the except block if port is not in range.
            int ('raise')
    except:
        # Print error if port is invalid.
        print (error); sleep(wait)

#########################################################################
# ARGS MODIFIED ADDRESS SERVER INFO
#########################################################################
# Check if settings were changed by arguments.
if argsBool:
    # Print header to inform the user of new settings.
    print ('ARGUMENTS PASSED: NEW SETTINGS FOR SERVER:'); sleep(wait)

    # Print the new server IP Address and inform the user.
    print ('\tServer IP:\t\t\t' + server_ip)

    # Print the new server port and inform the user.
    print ('\tServer Port:\t\t\t' + str(server_port)); sleep(wait)

#########################################################################
# ADDRESS INFO FOR SERVER
#########################################################################
# Store bool for settings change request.
argsBool = False

# Ask the user about changing settings.
print ('Do you wish to change default settings? [Yes/No]')

# Read user response.
prompt = input().lower()

# Check if user provided an invalid response, if so ask again.
while prompt not in ['yes', 'no', 'y', 'n']:
    # Ask the user again.
    print ('Please answer Yes or No | Y or N.')

    # Read response.
    prompt = input().lower()

# Request information.
if prompt in ['yes', 'y']:
    # Request, read and store ip address.
    print ('Enter Server IP Address in IPv4 format: ')
    temp_server_ip = input()

    # Check if user omitted to setting the IP Address.
    if len(temp_server_ip) != 0:
        # Vefiry IP Address provided is an valid IPv4.
        ipv4_verification = verify_IPv4(temp_server_ip)
                                        
        # Check if IP Address provided is invalid, if so ask again.
        while not ipv4_verification:
            # Check if user omitted to setting the IP Address.
            if len(temp_server_ip) == 0:
                # Break out of the while loop
                break
            
            # Request, read and store ip address again.
            print ('Enter a valid IP Address in IPv4 format: ')
            temp_server_ip = input()

            # Vefiry IP Address provided is an valid IPv4.
            ipv4_verification = verify_IPv4(temp_server_ip)

        # Change server_ip if address provided is valid.
        if ipv4_verification:
            # Set Server IP Address to a valid IPv4 obtained from user.
            server_ip = temp_server_ip

            # Change argsBool status.
            argsBool = True

    # Request port.
    print ('Enter Server Port: ')
    
    # Check if port provided is invalid, if so ask again.
    while True:
        # Check if the port string provided is an integer.
        try:
            # Store the port string provided.
            temp_server_port = input()
            
            # Skip if user presses enter.
            if len(temp_server_port) == 0:
                break
            
            # Parse the port string provided to an integer.
            temp_server_port = int(temp_server_port)

            # Set Server Port to a valid port obtained from the user.
            server_port = temp_server_port

            # Change argsBool status.
            argsBool = True
            
            # Break out of the while loop if port provided is valid.
            break
        except:
            # Request, read and store port again.
            print ('Enter a valid Port: ')
            
            continue

#########################################################################
# FINAL ADDRESS SERVER INFO
#########################################################################
# Check if user changed settings.
if argsBool:
    # Print header to inform the user of the final settings.
    print ('\nFINAL SETTINGS FOR SERVER:'); sleep(wait)

    # Inform the user of final server ip address.
    print ('\tServer IP:\t\t\t' + server_ip)

    # Inform the user of the final server port.
    print ('\tServer Port:\t\t' + str(server_port)); sleep(wait)
    
# Indicate the server being pinged and port.
print ('\nPinging ' + server_ip + ' on port ' + str(server_port)); sleep(wait)

print ('--------------------------------------')

#########################################################################
# CREATE A CLIENT SOCKET
#########################################################################
# Create the client socket.
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set server address.
serverIPv4 = server_ip

# Set port for the service.
serverPort = server_port

# Set a timeout for the client socket.
client.settimeout(1)

#########################################################################
# PING SERVER
#########################################################################
# Create variable to set maximun number of pings.
maxPings = 10

# Create variable to track pings.
currentPing = 1

# Loop for pinging to server a certain amount of times.
while currentPing <= maxPings:
    # Create variable to store time when packet is sent.
    sentTime = ''

    # Create variable to store time when packet is received.
    receivedTime = ''

    # Pack the current ping number -- 4-byte sequence number that identifies packet.
    packedSeqNum = struct.pack('i', currentPing)

    # Record time stamp in seconds.
    sentTime = time()
    
    # Send message (sequence number) from client to serverIPv4 at port serverPort.
    client.sendto(packedSeqNum, (serverIPv4, serverPort))

    # Handle response from the server.
    try:
        # Receive response from server.
        serverResp, (serverAddr, serverPort) = client.recvfrom(8000)

        # Record time stamp in seconds.
        receivedTime = time()

        # Unpack client's sequence number and time packet was received by server -- 4-byte + 8-byte.
        pingSeqNum, serverReceiveTime = struct.unpack('id', serverResp)[0:2]
        
        # Calculate OTT.
        ott = serverReceiveTime - sentTime
        
        # Calculate RTT.
        rtt = ott + (receivedTime - serverReceiveTime)

        # Indicate ping message number, ott and rtt.
        print ('Pinging Message ' + str(currentPing )+ ': OTT: ' + str(ott) + 'secs and RTT: ' + str(rtt) + 'secs'); sleep(wait)

        # Update the currentPing count.
        currentPing += 1

        continue
        
    except:
        # Indicate ping message number, timed out.
        print ('Pinging Message ' + str(currentPing) + ': Request Timed Out'); sleep(wait)

        # Update the currentPing count.
        currentPing += 1
        
        continue
    
client.close()
