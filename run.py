import sys
import importlib
import json

try:
	brain_name = sys.argv[1]
	brain = getattr(importlib.import_module('brains.'+str(brain_name)), str(brain_name))

except Exception as e:
	print('Could not load brain:')
	print(str(e))
	sys.exit()


params_filename = sys.argv[2] if len(sys.argv) > 2 else 'params.json'
print('Loading parameters from: '+params_filename)
try:
	with open(params_filename, 'r') as params_file:
		params = json.load(params_file)
except Exception as e:
	print('Could not load parameters:')
	print(str(e))
	sys.exit()

username = sys.argv[3] if len(sys.argv) > 3 else 'You'

bot = brain(params)
print('Brain loaded. Starting conversation...')
print(bot.greeting(username))

while True:
	user_prompt = raw_input('You: ')
	if user_prompt == 'exit':
		print('Ending conversation...')
		print(bot.end())
		break
	print(bot.talk(user_prompt))

print('Conversation ended.')
