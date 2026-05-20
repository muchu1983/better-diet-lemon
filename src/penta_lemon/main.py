import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui
from penta_lemon.xxxv_generator.time_driven import TimeDrivenXxxvGen
from penta_lemon.lemon import Lemon
from penta_lemon.const import XxxvCode

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.lemon = Lemon()
        self.timeDrivenXxxvGen = TimeDrivenXxxvGen()
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.updateText)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.textLemonStatus = QtWidgets.QLabel("灵萌状态", alignment=QtCore.Qt.AlignCenter)
        self.text6 = QtWidgets.QLabel("上爻", alignment=QtCore.Qt.AlignCenter)
        self.text5 = QtWidgets.QLabel("五爻", alignment=QtCore.Qt.AlignCenter)
        self.text4 = QtWidgets.QLabel("四爻", alignment=QtCore.Qt.AlignCenter)
        self.text3 = QtWidgets.QLabel("三爻", alignment=QtCore.Qt.AlignCenter)
        self.text2 = QtWidgets.QLabel("二爻", alignment=QtCore.Qt.AlignCenter)
        self.text1 = QtWidgets.QLabel("初爻", alignment=QtCore.Qt.AlignCenter)
        self.textList = [self.text1, self.text2, self.text3, self.text4, self.text5, self.text6]
        self.layout.addWidget(self.textLemonStatus)
        self.layout.addWidget(self.text6)
        self.layout.addWidget(self.text5)
        self.layout.addWidget(self.text4)
        self.layout.addWidget(self.text3)
        self.layout.addWidget(self.text2)
        self.layout.addWidget(self.text1)
        self.timer.start(300)

    @QtCore.Slot()
    def updateText(self):
        self.lemon.feedXxxv(self.timeDrivenXxxvGen.getXxxv())
        lemonStatus = str(self.lemon.octaNopoPentaMiri.octaNopoCode) + "," + str(self.lemon.octaNopoPentaMiri.pentaMiriCode)
        self.textLemonStatus.setText(lemonStatus)
        textIndex = 0
        for xxxv in self.lemon.yyp.sixXxxv:
            xxxvCode = xxxv.xxxvCode
            if textIndex == 0:
                self.text1.setText("初爻")
                self.text2.setText("二爻")
                self.text3.setText("三爻")
                self.text4.setText("四爻")
                self.text5.setText("五爻")
                self.text6.setText("上爻")
            if xxxvCode is XxxvCode.OLD_BDEM or xxxvCode is XxxvCode.YOUNG_BDEM:
                self.textList[textIndex].setText("⚊" + xxxvCode.name)
            elif xxxvCode is XxxvCode.OLD_BAYT or xxxvCode is XxxvCode.YOUNG_BAYT:
                self.textList[textIndex].setText("⚋" + xxxvCode.name)
            else:
                self.textList[textIndex].setText("error")
            textIndex += 1

def main():
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.resize(400, 50)
    widget.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
