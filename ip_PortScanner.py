import socket
import requests
import sys

class PortScanner:
    def __init__(self, hostname, IPAddr, ip, choice, result, port, sock, IP):
        self.hostname = hostname
        self.IPAddr = IPAddr
        self.ip = ip
        self.choice = choice
        self.result = result
        self.port = port
        self.sock = sock
        self.IP = IP
        

    hostname = socket.gethostname()    
    IPAddr = socket.gethostbyname(hostname)    
    ip = requests.get('https://checkip.amazonaws.com').text.strip()
    print("Your Computer's Name is: " + hostname)    
    print("Your Computer's IP Address is: ", IPAddr)    
    print("Your external IP address is: ", ip)

    print("Which IP doe you wanna scan?")
    choice = int(input("Enter '1' for your computer's, enter '2' for your external IP addresss, enter '3' for scanning specific ip. press any other digit to exit:   "))

    if choice == 1:
        IP = IPAddr
        print("Scanning computer's available ports")
    elif choice == 2:
        IP = ip
        print("Scanning your external IP for ports ")
    elif choice == 3:
        IP = input("Enter IP address:  ")
        print("Scanning specified IP for ports   ")
    else:
        print("                      ")
        print('                                 ---------------      EXIT     ----------------')
        sys.exit(0)

    
    for port in range(0, 65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((IP, port))
        if 0 == result:
            print("Port: {} Open 😁 😁".format(port))
        else:
            print("Port: {} CLOSED ☹️☹️".format(port), "----------------------")
        sock.close()