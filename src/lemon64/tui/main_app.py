from textual.app import App
from textual.widgets import Label
from lemon64.tui.list_screen import ListScreen
from lemon64.tui.map_screen import MapScreen
from lemon64.tui.list_screen import PersonStatic

class MainApp(App):

	CSS_PATH = "main_app.tcss"
	BINDINGS = [("l", "switch_mode('list')", "列表"),
				("m", "switch_mode('map')", "地图")]
	MODES = {"list": ListScreen,
			 "map": MapScreen}

	def __init__(self, controller, **kwargs):
		super().__init__(**kwargs)
		self.controller = controller

	def on_mount(self):
		self.switch_mode("list")
		