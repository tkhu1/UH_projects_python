# -*- coding: utf-8 -*-

#COSC4377 - Socket 1 Assignment in KC3 ||| Tyler Hu, UH ID: 0276538

#imports socket module
from socket import *
import sys

#prepares socket
servSocket = socket(AF_INET, SOCK_STREAM)
servPort = 1111

#binds port to the socket
servSocket.bind(('',servPort)) #NOTE: server IP is blank (own client IP)

#sets socket to accept requests
servSocket.listen(1)

#if request is received
while True:
    print('Ready to serve...')
    
    #accepts request
    connectSocket, addr = servSocket.accept()
    print("Connection request accepted from:", addr)
    
    #checks if requested file exists
    try:
        message = connectSocket.recv(2048).decode()
        
        #parses file name
        fileName = message.split()[1]
        file = open(fileName[1:], 'r')
        fileOutput = file.read()
        
        print("Requested file found...")
        #sends HTTP header into socket
        headerFileOK = "HTTP/1.1 200 OK\r\n"
        connectSocket.send(headerFileOK.encode())
        connectSocket.send("\r\n".encode())
        
        #sends the requested file to the client
        for i in range(0, len(fileOutput)):
            connectSocket.send(fileOutput[i].encode())
        connectSocket.send("\r\n".encode())
        print("Requested file sent.")
        
        #terminates connection to client
        connectSocket.close()
        
    #sends message to client if file not found
    except IOError:
        print("ERROR: Requested file not found...")
        
        #sends error header to the client
        headerFileError = "HTTP/1.1 404 Not Found\r\n"
        connectSocket.send(headerFileError.encode())
        connectSocket.send("\r\n".encode())
        print("Error message sent to client.")

        #terminates connection to client
        connectSocket.close()

    #terminates the program
    servSocket.close()
    sys.exit()