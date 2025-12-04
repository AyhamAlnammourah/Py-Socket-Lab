# Import the socket module
import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# socket.AF_INET # Address family for IPv4
# socket.AF_INET6 # Address family for IPv6
# socket.SOCK_STREAM # Socket type for TCP
# socket.SOCK_DGRAM # Socket type for UDP

print('Socket  Created!')

# Close the socket
s.close()
print('Socket Closed!')