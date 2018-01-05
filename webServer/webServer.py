#import socket module
from socket import *

# Create a TCP server socket
# (AF_INET is used for IPv4 protocols)
# (SOCK_STREAM is used for TCP)
serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
serverPort = 6767
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

while True:
    #Establish the connection
    print "Ready to serve..."

    # Set up a new connection from the client
    connectionSocket, addr = serverSocket.accept()

    # If an exception occurs during the execution of try clause
    # the rest of the clause is skipped
    # If the exception type matches the word after except
    # the except clause is executed
    try:
        # Receives the request message from the client
        message = connectionSocket.recv(1024)

        # Extract the path of the requested object from the message
        # The path is the second part of HTTP header, identified by [1]
        filename = message.split()[1]

        # Because the extracted path of the HTTP request includes
        # a character '\', we read the path from the second character
        f = open(filename[1:])

        # Store the entire contenet of the requested file in a temporary buffer
        outputdata = f.read()

        #Send one HTTP header line into socket
        # Reference: https://www.tutorialspoint.com/http/http_responses.htm
        connectionSocket.send('\nHTTP/1.1 200 OK\n\n')

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])

        connectionSocket.close()

    except IOError:
        #Send response message for file not found
        print ("404 Not Found")
        connectionSocket.send('\nHTTP/1.1 404 Not Found\n\n')

        #Close client socket
        connectionSocket.close()

serverSocket.close()
