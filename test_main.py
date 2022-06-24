import main

def test_encrypt():
	assert main.encrypt('password') != 'password'

def test_decrypt():
	password = main.encrypt('password')
	assert main.decrypt(password) == 'password'