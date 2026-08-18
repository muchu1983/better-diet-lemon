from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Header, Footer, Static, Label, Button, Input

class MainApp(App):
	def compose(self) -> ComposeResult:
		yield Header()
		yield Footer()

	def on_button_pressed(self, event:Button.Pressed):
		pass

if __name__ == "__main__":
	app = MainApp(css_path="./main_app.tcss", watch_css=True)
	app.run()
