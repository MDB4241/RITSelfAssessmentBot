import json

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

	def save(self):
		to_save = json.dumps(self)
		file = open("config.json", "w")
		file.write(to_save)

