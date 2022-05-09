import sys
import socket

# Acquiring IP address
while True:
    try:
        ip = socket.gethostbyname(sys.argv[1])
        break
    except:
        try:
            ip = socket.gethostbyname(input('Enter valid IP: '))
            break
        except:
            pass
        pass
        
# Acquiring port
while True:
    try:
        port = int(sys.argv[2])
        break
    except:
        try:
            port = int(input("Enter port: "))
            break            
        except:
            pass            
        pass 
        
print("\n\nScanning port " + str(port) + " on host: " + str(ip) + "\n")



# Scan
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((ip, port))
    if result == 0:
        print("Port {} is open\n".format(port))
    s.close()
except:
    pass

print("Program fnished\n\n")    

