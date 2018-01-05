Web server in Python that handles one HTTP request at a
time. This server accepts and parses a single HTTP request, gets
the requested file from the servers file system, creates an HTTP response
message consisting of the requested file preceded by header lines, and then
sends the response directly to the client. If the requested file is not present
in the server, the server sends an HTTP “404 Not Found” message
back to the client.

An incomplete multithreaded server that is capable
of serving multiple requests simultaneously is included as well.
