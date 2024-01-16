 

#client side 

from xmlrpc import client

proxy=client.ServerProxy("http://localhost:3010") # replace localhost with server ip address when you are running server.py and client.py on different systems in LAN.
num=int(input("Enter a number : "))
print("Cube is {}".format(proxy.cube(num)))
