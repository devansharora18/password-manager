from cryptography.fernet import Fernet
import os

if os.stat('key.key').st_size == 0:
	key = Fernet.generate_key()
	k = open('key.key', 'ab')
	k.write(key)
	k.close()

else:
	pass

if os.stat('password.txt').st_size == 0:
	password = input('Create root password: ')
	f = open('password.txt', 'a')
	f.write(password)
	f.close

else:
	pass