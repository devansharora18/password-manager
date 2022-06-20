from cryptography.fernet import Fernet

class PasswordManager:
	def __init__(self):
		self.key = None
		self.password = None
		self.dict = {}

		