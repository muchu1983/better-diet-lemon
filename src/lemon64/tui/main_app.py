from textual.app import App
from textual.widgets import Label

class Hello(App):
	def compose(self):
		yield Label("Hello lemon64")

if __name__ == "__main__":
	app = Hello(css_path="./main_app.tcss", watch_css=True)
	app.run()
