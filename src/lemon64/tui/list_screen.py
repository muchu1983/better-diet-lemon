from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.containers import Horizontal, Vertical, HorizontalGroup, VerticalGroup, VerticalScroll, HorizontalScroll
from textual.widgets import Header, Footer, Static, Label, Button, Input, Rule
from textual.reactive import reactive

class PersonStatic(Static):
	def __init__(self, text:str, **kwargs):
		super().__init__(**kwargs)
		self.person_name = text

	def compose(self) -> ComposeResult:
		yield Label(self.person_name)
		yield Label("人格")
		yield Button("发布", variant="primary", id="publish-to-map")

class ListScreen(Screen):
	TITLE = "lemon64"
	SUB_TITLE = "list"
	CSS_PATH = "list_screen.tcss"
	def compose(self) -> ComposeResult:
		self.add_class("list-screen")
		yield Header()
		yield Footer()
		with Horizontal():
			yield HorizontalScroll(
				VerticalScroll(
					PersonStatic("本人", id="myself"),
					Rule.horizontal(),
					Static("他人1", classes="left-panel"),
					Static("他人2", classes="left-panel"),
					Static("他人3", classes="left-panel"),
					Static("他人4", classes="left-panel"),
					Static("他人5", classes="left-panel"),
					classes="left-panel"
				),
				Rule.vertical(),
				VerticalScroll(
					Static("柠檬64 列表 右面板", classes="right-panel"),
					Static("柠檬64 列表 右面板", classes="right-panel"),
					Static("柠檬64 列表 右面板", classes="right-panel"),
					Static("柠檬64 列表 右面板", classes="right-panel"),
					Static("柠檬64 列表 右面板", classes="right-panel"),
					Static("柠檬64 列表 右面板", classes="right-panel"),
					Static("柠檬64 列表 右面板", classes="right-panel"),
					classes="right-panel"
				)
			)