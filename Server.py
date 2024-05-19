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
print("Socket is listening")# Generate encryption key
    key1 = hashlib.sha256()
    key1.update(soct.gethostname().encode('utf-8'))
    key2 = key1.hexdigest()[:32]
    key3 = base64.b64encode(key2.encode('utf-8'))
    cipher_suite = Fernet(key3)

    while True:
        # Receive and decrypt message from client
        received = sslClientSocket.recv(1024)
        if not received:
            break
        decrypted = cipher_suite.decrypt(received)
        print("\n>> Message sent from client (encrypted):", received)
        print(">> Decrypted message sent from client:", decrypted.decode('utf-8'))
