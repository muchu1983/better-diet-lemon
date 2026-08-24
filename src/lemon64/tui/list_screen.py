from textual.app import App, ComposeResult
from textual.screen import Screen
from textual.containers import Horizontal, Vertical, HorizontalGroup, VerticalGroup, VerticalScroll, HorizontalScroll
from textual.widgets import Header, Footer, Static, Label, Button, Input, Rule
from textual.reactive import reactive

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
					Static("柠檬64 列表 左面板1", classes="left-panel"),
					Static("柠檬64 列表 左面板2", classes="left-panel"),
					Static("柠檬64 列表 左面板3", classes="left-panel"),
					Static("柠檬64 列表 左面板4", classes="left-panel"),
					Static("柠檬64 列表 左面板5", classes="left-panel"),
				),
				Rule.vertical(),
				Static("柠檬64 列表 右面板", classes="right-panel")
			)