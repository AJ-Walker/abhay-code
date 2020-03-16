import socket

# creating a socket object

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name

host = socket.gethostname()
port = 9999

# connection to hostname on the port

serv.connect((host, port))

# receive no more than 1024 bytes

msg = serv.recv(1024)
serv.close()
print (msg.decode('ascii'))
