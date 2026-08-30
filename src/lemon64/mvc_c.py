class Controller:
	
	def __init__(self):
		pass

	def call_notify(self, app, text):
		app.notify(f"{text}")
