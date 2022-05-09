import socket

min_port = 1
max_port = 65535

# Acquiring IP address
while True:
    try:
        ip = socket.gethostbyname(input('Enter valid IP address: '))
        break
        
    except:
        pass


# Acquiring port range
while True:
    while True:
        try:
            min_port = int(input("Enter start of the port range: "))
            if (min_port > 0 or min_port < 65536):
                break
        except:
            pass

    while True:
        try:
            max_port = int(input("Enter end of the port range: "))
            if (max_port > 0 or max_port < 65536):
                break
        except:
            pass
        
    if (min_port <= max_port):
        break

# Confirmation   
print("\n\nIP address is correct.\nScanning IP: " + ip + " in specified port range\n\n" + "-" * 33 + "+") 

# Scan
try:
    for port in range(min_port, max_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
         
        result = s.connect_ex((ip, port))
        if result == 0:
            print("Port {} is Open \t\t |".format(port))
        s.close()
        
except:
    pass

print("-" * 33 + "+\n\nProgram fnished.\n\n")    

