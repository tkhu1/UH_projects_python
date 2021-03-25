Implemented a web server that handles one HTTP request at a time. The server accepts
and parses the HTTP request, gets the requested file from the server’s file system, creates an HTTP response
message consisting of the requested file preceded by header lines, and then sends the response directly to
the client. If the requested file is not present in the server, the server sends an HTTP “404 Not
Found” message back to the client.

Included an HTML file (e.g., HelloWorld.html) in the same directory that the server is in. 

‘HelloWorld.html’ is the name of the file placed in the server directory. 