from cryptography.fernet import Fernet

key = Fernet.generate_key()

cryption = Fernet(key)

proceed = False

def main():
	# Main password to secure the script
	root = input('Enter root password: ')

	# Enter any password of your choice
	root_pass = '0'

	if root == root_pass:
		proceed = True

def prompt():
	 prmpt = input('Press (1) to enter password or (2) to view passwords: ')
