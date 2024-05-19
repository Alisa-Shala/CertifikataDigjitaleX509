import OpenSSL
import socket as soct
import ssl
import hashlib
import base64
from cryptography.fernet import Fernet

# Load SSL certificate and key
openssl = OpenSSL.crypto
certiFile = open("/Users/anditernava/server.crt").read()
keyFile = open("/Users/anditernava/server.key").read()

x509 = openssl.load_certificate(openssl.FILETYPE_PEM, certiFile)
key = openssl.load_privatekey(openssl.FILETYPE_PEM, keyFile)
# Create server socket
try:
    serverSocket = soct.socket(soct.AF_INET, soct.SOCK_STREAM)
    print("Socket successfully created")
except soct.error as err:
    print("Socket creation failed with error", err)

serverPort = 8000
serverSocket.bind(('127.0.0.1', serverPort))
serverSocket.listen(5)
# Wrap socket with SSL
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="/Users/anditernava/server.crt", keyfile="/Users/anditernava/server.key")

# Accept client connection
while True:
    clientSocket, addr = serverSocket.accept()
    print('Received connection from:', addr)
    sslClientSocket = context.wrap_socket(clientSocket, server_side=True)
print("Socket is listening")
