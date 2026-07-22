import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.settimeout(5)

try:
    client.connect(("192.168.1.3", 8080))
    print("Connected!")
except TimeoutError:
    print("Connection timed out.")
except ConnectionRefusedError:
    print("Server isn't accepting connections.")
except socket.gaierror:
    print("Invalid hostname.")
finally:
    client.close()