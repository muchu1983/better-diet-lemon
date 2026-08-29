from textual.message import Message

class PersonStaticClicked(Message):

	def __init__(self, person_name: str):
		super().__init__()
		self.person_name = person_name