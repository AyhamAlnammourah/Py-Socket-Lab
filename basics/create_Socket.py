# Import the socket module
import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket  Created!')

# Close the socket
s.close()
print('Socket Closed!')