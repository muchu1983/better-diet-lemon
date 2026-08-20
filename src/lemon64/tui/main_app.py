from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.containers import Horizontal, Vertical, HorizontalGroup, VerticalGroup, VerticalScroll, HorizontalScroll
from textual.widgets import Header, Footer, Static, Label, Button, Input
from textual.reactive import reactive

class ListScreen(Screen):
	TITLE = "lemon64"
	SUB_TITLE = "list"
	
	def compose(self) -> ComposeResult:
		yield Header()
		yield Footer()
		yield Static("柠檬64 App", id="my-static")

class MapScreen(Screen):
	TITLE = "lemon64"
	SUB_TITLE = "map"
	
	def compose(self) -> ComposeResult:
		yield Header()
		yield Footer()
		yield Static("柠檬64 App", id="my-static")

class MainApp(App):
	CSS_PATH = "main_app.tcss"
	BINDINGS = [("l", "switch_mode('list')", "列表"),
				("m", "switch_mode('map')", "地图")]
	MODES = {"list": ListScreen,
			 "map": MapScreen}
	
	def on_mount(self):
		self.switch_mode("list")

if __name__ == "__main__":
	app = MainApp(watch_css=True)
	app.run()
