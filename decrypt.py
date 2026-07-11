import base64

def decrypt_pass(encrypted):
    decripted = base64.b64decode(encrypted).decode()
    print("Password: ",decripted)

encrypted = "cm9oaXQ="
decrypt_pass(encrypted)