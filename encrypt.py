import base64

def encrypt_pass(password):
    global encrypted
    encrypted = base64.b64encode(password.encode())
    print("Encrypted password: ",encrypted)

password = input("Enter the password: ")
encrypt_pass(password)


