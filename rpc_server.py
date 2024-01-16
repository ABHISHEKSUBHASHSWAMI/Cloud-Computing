


#Server Side

from xmlrpc.server import SimpleXMLRPCServer
def cube(n):
    return n**3
    
server=SimpleXMLRPCServer(("localhost",3010)) # replace localhost with ip address of system when you are running server.py and client.py on different system in LAN.
server.register_function(cube)
server.serve_forever()
