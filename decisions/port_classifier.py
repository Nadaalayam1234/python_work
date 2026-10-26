# port_classifier.py - checks port range and service
port = int(input("Port: "))

if port < 0 or port > 65535:
    print("Invalid port: use a number from 0 to 65535.")
else:
    # check range
    if port >= 0 and port <= 1023:
        print("Range: system")
    elif port >= 1024 and port <= 49151:
        print("Range: user")
    else:
        print("Range: dynamic or private")

    # check known services
    if port == 22:
        print("Service: ssh")
    elif port == 80:
        print("Service: http")
    elif port == 443:
        print("Service: https")