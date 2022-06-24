# RUN THIS SCRIPT ONLY ONCE

from cryptography.fernet import Fernet

key = Fernet.generate_key()
k = open('key.key', 'wb')
k.write(key)
k.close()