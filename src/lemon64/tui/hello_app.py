from textual.app import App, ComposeResult
from textual.containers import Horizontal, Vertical
from textual.widgets import Header, Footer, Static, Label, Button, Input

class Hello(App):
	def compose(self) -> ComposeResult:
		yield Header()
		with Vertical():
			yield Static("柠檬64 App", id="result")
			with Horizontal():
				yield Label("Hello lemon64")
				yield Button("按我", id="btn")
			yield Input(placeholder="输入名字", id="name")
			with Horizontal():
				yield Button("确定", id="btn-name")
				yield Button("清除", id="btn-clear")
		yield Footer()

	def on_button_pressed(self, event:Button.Pressed):
		name_input = self.query_one("#name", Input)
		result_static = self.query_one("#result", Static)
		if event.button.id == "btn":
			self.notify("Hello lemon64")	
		elif event.button.id == "btn-name":
			self.notify(f"Hello, {name_input.value}")
			result_static.update(f"你好阿{name_input.value}")	
		elif event.button.id == "btn-clear":
			self.notify("清除")
			result_static.update("柠檬64 App")

if __name__ == "__main__":
	app = Hello(css_path="./hello_app.tcss", watch_css=True)
	app.run()
