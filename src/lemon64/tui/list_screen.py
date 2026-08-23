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
		yield Static("柠檬64 列表", id="my-static")