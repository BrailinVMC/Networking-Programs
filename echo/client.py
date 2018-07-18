#!/usr/bin/env python3

#########################################################################
#  Script     : client.py
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
#    If arguments are given:
#      # The 1st argument is considered as the server's IP Address.
#      # The 2nd argument is considered as the port.
#      # The 3rd argument is considered as the string length for the message.
#
# Syntax:
#    # 1. UDP-Echo-Client.py
#    # 2. UDP-Echo-Client.py <IP Address>
#    # 3. UDP-Echo-Client.py <IP Address> <Port Number> 
#    # 4. UDP-Echo-Client.py <IP Address> <Port Number> <String Length>
#
# Notes: None.
#########################################################################
# Import the system module.
import sys

# Import the socket module.
import socket

# Import sleep, localtime and strftime from the time module.
from time import sleep, localtime, strftime

# Import the echoRequired module.
from echoRequired import verify_IPv4

# Set short sleep time.
wait = 0.250

#########################################################################
# DEFAULT SERVER ADDRESS INFO
#########################################################################
# Print header to inform the user of the default settings.
print ('DEFAULT SETTINGS FOR SERVER:'); sleep(wait)

# Set the default server IP Address to localhost and inform the user.
server_ip = '127.0.0.1'
print ('\tServer IP:\t\t' + server_ip)

# Set the default server port and inform the user.
server_port = 1543
print ('\tServer Port:\t\t' + str(server_port))

# Set the default string length and inform the user.
str_len = 8000
print ('\tString Length:\t\t' + str(str_len) + '\n'); sleep(wait)

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

# Set string for changes.
changes = ''

# Check if arguments have been provided - for IP Address.
if argsLength > 1:
    # Set the error.
    error = 'IP ADDR ARG ERROR' # IP Address provided is invalid.
    
    # Set temp_ip to first argument.
    temp_ip = args[1]
    
    # Verify if IP Address provided is valid.
    if verify_IPv4(temp_ip):
        # Inform user that IP Address has been chaned by argument.
        changes += 'IP ADDRESS CHANGED\n'

        # Change server_ip.
        server_ip = temp_ip

        # Change argsBool status.
        argsBool = True
    else:
        # Print error if IP Address is invalid.
        print (error)

        # Exit program.
        exit()

# Checks if arguments have been provided - for port.
if argsLength > 2:
    # Set the error.
    error = 'PORT NUMBER ERROR' # Port provided is invalid.

    # Set temp_port to second argument.
    temp_port = args[2]
    
    # Verify if port provided is valid.
    try:
        temp_port = int(temp_port)

        if temp_port >= 0 and temp_port <= 65536:
            # Inform user that port has been chaned by argument.
            changes += 'PORT NUMBER CHANGED\n'

            # Change server_port.
            server_port = temp_port

            # Change argsBool status.
            argsBool = True
        else:
            # Raise error to execute the except block if port is not in range.
            int ('raise')
    except:
        # Print changes.
        print (changes)

        # Print error if port is invalid.
        print (error)

        # Exit program.
        exit()

# Checks if arguments have been provided - for string length.
if argsLength > 3:
    # Set the error.
    error = 'STRING LENGTH ERROR\n' # String length provided is invalid.

    # Set temp_str_length to third argument.
    temp_str_length = args[3]
    
    # Verify if string length provided is valid.
    try:
        temp_str_length = int(temp_str_length)

        if temp_str_length >= 0 and temp_str_length <= 65536:
            # Inform user that string length has been chaned by argument.
            changes += 'STRING LENGTH CHANGED.\n'

            # Change str_len.
            str_len = temp_str_length

            # Change argsBool status.
            argsBool = True
        else:
            # Raise error to execute the except block if string length is not in range.
            int ('raise')

    except:
        # Print changes.
        print (changes)

        # Print error if port is invalid.
        print (error); sleep(wait)

        # Exit program.
        exit()

# Print changes.
print (changes)
#########################################################################
# ARGS MODIFIED ADDRESS SERVER INFO
#########################################################################
# Check if settings were changed by arguments.
if argsBool:
    # Print header to inform the user of new settings.
    print ('NEW SERVER SETTINGS:'); sleep(wait)

    # Print the new server IP Address and inform the user.
    print ('\tServer IP:\t\t' + server_ip)

    # Print the new server port and inform the user.
    print ('\tServer Port:\t\t' + str(server_port))

    # Print the new string length and inform the user.
    print ('\tString Length:\t\t' + str(str_len) + '\n'); sleep(wait)

#########################################################################
# ADDRESS INFO FOR SERVER
#########################################################################
# Check if settings were changed by arguments.
if not argsBool:
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
                        # Break out of the while loop.
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

            # Request string length.
            print ('Enter String Length: ')

            # Check if string length provided is invalid, if so ask again.
            while True:
                # Check if the string length provided is an integer.
                try:
                    # Store the string length provided.
                    temp_str_len = input()
                    
                    # Skip if user presses enter.
                    if len(temp_str_len) == 0:
                        break
                    
                    # Parse the string length provided to an integer.
                    temp_str_len = int(temp_str_len)
                    
                    # Set String Length to a valid length obtained from the user.
                    str_len = temp_str_len

                    # Change argsBool status.
                    argsBool = True

                    # Break out of the while loop if string length provided is valid.
                    break
                except:
                    # Request, read and store string length again.
                    print ('Enter a valid String Length: ')
                    
                    continue

#########################################################################
# FINAL ADDRESS SERVER INFO
#########################################################################
# Check if user changed settings.
if argsBool:
    # Print header to inform the user of the final settings.
    print ('\nFINAL SERVER SETTINGS:'); sleep(wait)

    # Inform the user of final server ip address.
    print ('\tServer IP:\t\t' + server_ip)

    # Inform the user of the final server port.
    print ('\tServer Port:\t\t' + str(server_port))

    # Inform the user of final string length.
    print ('\tString Length:\t\t' + str(str_len) + '\n'); sleep(wait)

# Inform the user of that client is ready.
print ('READY FOR USE'); sleep(wait)

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
client.settimeout(3)

#########################################################################
# SEND MSG TO SERVER
#########################################################################
# Create variable to track tries.
tries = 0

# Create variable to check if response was received.
response = True
    
# Continous Loop for Sending Messages to Server.
while True:
    if response:
        # Read message from client.
        print ('------------------------------------------------------'); sleep(wait)
        message = input('Enter Message -- or $quit to exit:\n')

        # Check if user responds '$quit'
        if message == '$quit':
            break

    # Send message from client to serverIPv4 at port serverPort.
    client.sendto(message.encode(), (serverIPv4, serverPort))

    if response:
        # Record date stamp.
        dateSent = strftime('%b %dth, %Y', localtime())

        # Record time stamp.
        timeSent = strftime('%H:%M:%S', localtime())

        # Indicate information about destination of message was sent.
        print ('\nSENT TO:'); sleep(wait)
        
        # Server IP Address message was sent to.
        print ('\tServer IP:\t\t' + server_ip)

        # Server port message was sent to.
        print ('\tServer Port:\t\t' + str(server_port))

        # String length of message that was sent.
        print ('\tString Length:\t\t' + str(len(message)))

        # Sleep.
        sleep(wait)
        
        # Indicate information about when the message was sent.
        print ('\nSENT AT:'); sleep(wait)
        
        # Date on which message was sent.
        print ('\tDate:\t\t\t' + dateSent)

        # Time at which message was sent.
        print ('\tLocal Time:\t\t' + timeSent)

        # Sleep.
        sleep(wait)
        
        # Indicate content that was sent.
        print ('\nCONTENT SENT:'); sleep(wait)

        # Show content sent.
        print ('\t\'' + message + '\''); sleep(wait)

        # Display a divider.
        print ('------------------------------------------------------')

    # Handle response from the server.
    try:
        # Update response status.
        response = False
        
        # Receive response from server.
        serverResponse, (serverAddr, serverPort) = client.recvfrom(str_len)

        # Update response status.
        response = True

        # Update number of tries.
        tries = tries + 1
        
        # Decode response.
        serverResponse = serverResponse.decode()
        
        # Record date stamp.
        dateReceived = strftime('%b %dth, %Y', localtime())

        # Record time stamp.
        timeReceived  = strftime('%H:%M:%S', localtime())

        # Sleep.
        sleep(wait)
        
        # Indicate information about message source.
        print ('RECEIVED FROM:'); sleep(wait)
        
        # Server IP Address message was received from.
        print ('\tServer IP:\t\t' + serverAddr)

        # Server port message was received from.
        print ('\tServer Port:\t\t' + str(serverPort))

        # String length of message that was received.
        print ('\tString Length:\t\t' + str(len(serverResponse)))

        # Sleep.
        sleep(wait)

        # Indicate information about when the message was received.
        print ('\nRECEIVED AT:'); sleep(wait)
        
        # Date on which message was received.
        print ('\tDate:\t\t\t' + dateReceived)

        # Time at which message was sent.
        print ('\tLocal Time:\t\t' + timeReceived)

        # Sleep.
        sleep(wait)
        
        # Indicate content that was received.
        print ('\nCONTENT RECEIVED:'); sleep(wait)

        # Show content received.
        print ('\t' + serverResponse + '\n')
    
    except:
        # Update number of tries.
        tries = tries + 1
        
        # Indicate try number.
        print ('\nTry ' + str(tries) + ': Timed Out.\n'); sleep(wait)
        
        # Break out of the loop if the user gets no response three times.
        if tries >= 3:
            response = True
        
        continue
    
client.close()
