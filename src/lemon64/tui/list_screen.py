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
					Static("本人", classes="left-panel"),
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