import json
from crypto import Crypto

class ConfigData:
	def __init__(self, username, password):
		self._username = username
		self._password = password

	@property
	def username(self):
		return self._username

	@username.setter
	def username(self, value):
		self._username = value
		self.save()

	@property
	def password(self):
		return self._password

	@password.setter
	def password(self, password):
		self._password = password
		self.save()

	def save(self):
		crypto = Crypto(self._password)
		to_save = json.dumps(self.__dict__)
		with open("config.json", "wb") as config:
			config.write(crypto.encrypt(to_save.encode()))