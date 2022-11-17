

#client side 

from xmlrpc import client

proxy=client.ServerProxy("http://localhost:3010")
num=int(input("Enter a number : "))
print("Cube is {}".format(proxy.cube(num)))
