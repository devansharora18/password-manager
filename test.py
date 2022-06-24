from cryptography.fernet import Fernet
from passwords import userpass

key = Fernet.generate_key()
cryption = Fernet(key)

print (str(cryption.decrypt(userpass['instagram']), 'utf8'))