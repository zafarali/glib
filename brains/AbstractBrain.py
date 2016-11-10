# a wireframe for a brain.
from abc import ABCMeta, abstractmethod


class AbstractBrain(object):
	__metaclass__ = ABCMeta
	@abstractmethod
	def __init__(self, params):
		"""
			this method is used to set up the bot
			@params:
				params from a json file
			@returns:
				None
		"""
		pass

	@abstractmethod
	def greeting(self, username):
		""" 
			this method is called after the bot is initialized
			@params: 
				username: the name of the user interacting with the bot

			@returns:
				str: the response that will be echoed

		"""
		pass

	@abstractmethod
	def talk(self, user_input):
		"""
			this method is called with the user input
			@params:
				user_input: the input typed by the user

			@returns:
				str: the response that will be echoed

		"""
		pass

	@abstractmethod
	def end(self):
		"""
			This method is called at the end of the exchange
			@params:
				none
			@returns
				none
		"""
		pass
