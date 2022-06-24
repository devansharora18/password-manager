# RUN THIS SCRIPT ONLY ONCE OR YOU CAN LOSE YOUR PASSWORDS

from cryptography.fernet import Fernet

key = Fernet.generate_key()
k = open('key.key', 'ab')
k.write(key)
k.close()