from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.containers import Horizontal, Vertical, HorizontalGroup, VerticalGroup, VerticalScroll, HorizontalScroll
from textual.widgets import Header, Footer, Static, Label, Button, Input
from textual.reactive import reactive


class BSOD(Screen):
    BINDINGS = [("escape", "app.pop_screen", "Pop screen")]

    def compose(self) -> ComposeResult:
        yield Static(" Windows ", id="title")
        yield Static("ERROR_TEXT")
        yield Static("Press any key to continue [blink]_[/]", id="any-key")

class HelloApp(App):
	BINDINGS = [("d", "toggle_dark", "Toggle dark mode"),
				("b", "push_screen('bsod')", "BSOD")]
	SCREENS = {"bsod": BSOD}
	def compose(self) -> ComposeResult:
		yield Header()
		yield Footer()
		with Vertical():
			yield Static("柠檬64 App", id="result")
			with Horizontal():
				yield Label("Hello lemon64")
				yield Button("按我", id="btn")
			yield HorizontalScroll(
				Input(placeholder="输入名字", id="name"),
				Button("确定", id="btn-name"),
				Button("清除", id="btn-clear")
			)
		
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

	def action_toggle_dark(self) -> None:
		"""An action to toggle dark mode."""
		self.theme = ("textual-dark" if self.theme == "textual-light" else "textual-light")

if __name__ == "__main__":
	app = HelloApp(css_path="./hello_app.tcss", watch_css=True)
	app.run()
