import main

def test_encrypt():
	assert main.encrypt('password') != 'password'