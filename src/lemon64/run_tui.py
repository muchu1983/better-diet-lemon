from lemon64.tui.main_app import MainApp
from lemon64.mvc_c import Controller

def run_tui():
    controller = Controller()
    #注入 mvc controller 到 app
    app = MainApp(controller=controller, watch_css=True)
    app.run()
