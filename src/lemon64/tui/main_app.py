from textual.app import App
from textual.widgets import Label, Button

class Hello(App):
	def compose(self):
		yield Label("Hello lemon64")
		yield Button("按我", id="btn")

	def on_button_pressed(self, event:Button.Pressed):
		if event.button.id == "btn":
			self.notify("Hello lemon64")

if __name__ == "__main__":
	app = Hello(css_path="./main_app.tcss", watch_css=True)
	app.run()
