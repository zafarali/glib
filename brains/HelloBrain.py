from AbstractBrain import AbstractBrain

class HelloBrain(AbstractBrain):
	def __init__(self, params):
		self.myname = params.get('name', 'myname')

	def greeting(self, username):
		self.username = username
		return 'Hey '+self.username+'! My name is '+self.myname+' :)'

	def talk(self, user_input):
		return 'Unfortunately, I don\'t know how to do anything yet...'

	def end(self):
		return 'Goodbye!'