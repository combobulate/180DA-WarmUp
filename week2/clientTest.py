import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
<<<<<<< HEAD
client.connect(('192.168.1.100', 8080))
client.send(b"I am CLIENT\n")
=======
client.connect(('192.168.1.128', 8080))
client.send("I am CLIENT\n")
>>>>>>> a439f07a480ae948354f11f0cdf720bcdf150262
from_server = client.recv(4096)
client.close()
print(from_server)
