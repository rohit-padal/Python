import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("0.0.0.0", 8080))

s.listen(5)
print("Waiting for client...")

client_soc, client_addr = s.accept()
print(f"Connected to {client_addr}")

msg = "Hello Windows!"
client_soc.sendall(msg.encode())

c_msg = client_soc.recv(1024).decode()
print("Client: ", c_msg)

sec_msg = input("You: ")
client_soc.sendall(sec_msg.encode())

client_soc.close()

s.close()