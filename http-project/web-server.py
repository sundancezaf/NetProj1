
'''

(i) create a connection socket when contacted by an http client
(ii) accept and parse the http request from that connection
(iii) get the requested file from the server’s file system
(iv) create an http response message consisting of the requested file preceded by header lines
(v) send the response back to the client. If the requested file is not present in the server,
 the server should send an http “404 Not Found” message to the client.


--- Testing ---
Running the server: Determine the IP address of the machine running the server, and select a
non-standard port number for it. Then, run the web server after binding it to that port. Make sure
to place a simple html file in the same directory as the server.
From another machine, open a web browser and type in the URL http://<server-ip-addr>:<server-
port-number>/<file-name>. Make sure the web browser is able to display the file. Then, repeat
the testing with a non-existent file. The browser should display “404 Not Found” message


'''

import errno
import socket
import sys 
import os
 
#Create a TCP server socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

#Prepare the sever socket

#FillInStart
serverSocket.bind(('0.0.0.0',18880))
serverSocket.listen()


#FillInEnd 

while True:    
    print('Ready to serve...') 
    #Set up a new connection from the client
    connectionSocket, addr = serverSocket.accept()

    #If an exception occurs during the execution of try clause
    #the rest of the clause is skipped
    #If the exception type matches the word after except
    #the except clause is executed
    try: 
        #Receive the request message from the client
        message = connectionSocket.recv(4096)
        #FillInStart #FillInEnd 
        
        #Extract the path of the requested object from the message
        #The path is the second part of HTTP header, identified by [1]
        filename = message.split()[1]
        #Because the extracted path of the HTTP request includes 
        #a character '\', we read the path from the second character 
        f = open(filename[1:])     
        #Store the entire content of the requested file in a buffer
        outputdata = f.read()
        
        #Send the HTTP response header line to the connection socket
        #FillInStart       
        connectionSocket.send('HTTP/1.1 200 OK \r\n\r\n'.encode())
        #FillInEnd

        #Send the content of the requested file to the client 
        for i in range(0, len(outputdata)): 
            connectionSocket.send(outputdata[i].encode())               
        
        connectionSocket.send("\r\n".encode()) 
        connectionSocket.close() 
    
    except IOError:
        connectionSocket.send('\nHTTP/1.1 404 Not Found\r\n\r\n'.encode())
        connectionSocket.send(b'<html><body><h1>Error 404: File Not Found</h1> Do not come around here no more</body></html>')
        connectionSocket.send("\r\n".encode())
        
        #Close client socket 
        connectionSocket.close()

#Terminate the program
serverSocket.close()
sys.exit()
