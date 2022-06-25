from cryptography.fernet import Fernet
from passwords import userpass
import sys
import os
import pyperclip

k = open('key.key', 'rb')
key = k.read()
k.close()
cryption = Fernet(key)
proceed = False
curly = '}'

def main():
	# Deletes setup.py
	try:
		os.remove('setup.py')
	except:
		pass

	# Main password to secure the script
	root = input('Enter root password: ')

	# Enter any password of your choice
	root_pass = ''

	if root == root_pass:
		proceed = True
	
	else:
		sys.exit('Wrong password')

	if proceed == True:
		prompt()

def prompt():
	# Prompts the user for entering password or viewing them
	prmpt = input('Press (1) to enter password or (2) to view passwords: ')
	try:
		assert prmpt == '1' or prmpt == '2'
	
	except:
		sys.exit('invalid request')
	
	if prmpt == '1':
		new_pass()

	elif prmpt == '2':
		view_pass()

def encrypt(a):
	# Encrypts password
	return cryption.encrypt(a)

def decrypt(a):
	# Decrypts password
	return str(cryption.decrypt(a), 'utf8')

'''
password = encrypt(b'password')

print (password)

print (decrypt(password))
'''

def new_pass():
	# It opens a file to store passwords and encrypts it
	service = input('Enter service name: ')
	if service not in userpass:
		password = input('Enter password: ').encode()
		password = encrypt(password)
		f = open('passwords.py', 'ab+')
		f1 = open('passwords.py', 'a+')
		f.seek(-1, os.SEEK_END)
		f.truncate()
		f1.write(f'	\'{service}\' : {password}, \n{curly}')
		f.flush()
		f1.flush()
		f.close()
		f1.close()
	else:
		sys.exit('Try a different name foe the service')

def view_pass():
	# Decrypts the passwords and displays it
	for key in userpass.keys():
		print(key)

	service = input('Enter service name: ')
	try:
		print ('password:' , decrypt(userpass[service]))
		pyperclip.copy(decrypt(userpass[service]))
		print('Passwprd copied to clipboard')
	except:
		sys.exit('no service found')

if __name__ == '__main__':
	main()