# Import the socket module
import socket

try:
    # Get the hostname of the current machine
    ip = socket.gethostbyname('google.com')

    # The functions translates a hostname to an IPv4 address
    # The IP address is returned as a string
    # It does not support IPv6

    # Print the IP address
    print(f'IP address of Domain is {ip}')

except socket.gaierror:
    # Get Address Info error
    print('There was an error resolving the host')

try:
    # Get the hostname of the IP address
    hostname = socket.gethostbyaddr(ip)

    # The functions translates an ip address into (hostname, aliaslist, ipaddrlist)
    # Hostname is the primary host name responding to the given ip_address
    # Aliaslist is a list of alternative host names for the same address
    # Ipaddrlist is a list of IPv4/v6 addresss for the same interface on the same host

    # Print the hostname
    print(f'Hostname for IP address {ip} is {hostname}')

except socket.herror:
    # Host error
    print('There was an error resolving the IP address')
