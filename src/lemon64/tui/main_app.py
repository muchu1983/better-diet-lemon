from textual.app import App
from lemon64.tui.list_screen import ListScreen
from lemon64.tui.map_screen import MapScreen

class MainApp(App):
	CSS_PATH = "main_app.tcss"
	BINDINGS = [("l", "switch_mode('list')", "列表"),
				("m", "switch_mode('map')", "地图")]
	MODES = {"list": ListScreen,
			 "map": MapScreen}
	def on_mount(self):
		self.switch_mode("list")

