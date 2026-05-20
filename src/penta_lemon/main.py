import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from penta_lemon.xxxv_generator.time_driven import TimeDrivenXxxvGen
from penta_lemon.lemon import Lemon

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.lemon = Lemon()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateText)
        self.timeDrivenXxxvGen = TimeDrivenXxxvGen()
        self.text = QtWidgets.QLabel("Hello World Penta Lemon", alignment=QtCore.Qt.AlignCenter)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.timer.start(1000)

    @QtCore.Slot()
    def updateText(self):
        self.lemon.feedXxxv(self.timeDrivenXxxvGen.getXxxv())
        self.text.setText(str(self.lemon))

def main():
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.resize(400, 300)
    widget.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
