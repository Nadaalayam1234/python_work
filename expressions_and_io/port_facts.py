# Source: RFC 9293 Sec 3.1 - Source and Destination ports are 16 bits
# Source: RFC 791 Sec 2.3 - Addresses are 32 bits

PORT_BITS = 16
IPV4_BITS = 32

num_ports = 2 ** PORT_BITS
highest_port = 2 ** PORT_BITS - 1
num_ipv4 = 2 ** IPV4_BITS

print(f"Number of possible ports: {num_ports}")
print(f"Highest port number: {highest_port}")
print(f"Number of possible IPv4 addresses: {num_ipv4}")