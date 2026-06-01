import sys
from PySide6 import QtCore, QtWidgets, QtGui
from penta_lemon.xxxv_generator.time_driven import TimeDrivenXxxvGen
from penta_lemon.gui.lemon_widget import LemonWidget

def main():
    app = QtWidgets.QApplication([])
    #第0位元
    widget0 = LemonWidget()
    timeDrivenXxxvGen = TimeDrivenXxxvGen()
    timer = QtCore.QTimer()
    timer.timeout.connect(lambda:widget0.updateText(food=timeDrivenXxxvGen.getXxxv()))
    timer.start(300)
    widget0.resize(400, 50)
    widget0.show()
    #第1位元
    widget1 = LemonWidget()
    widget0.singalToNextLemonWidget.connect(lambda:widget1.updateText(food=widget0.lemon.getCarryXxxv()))
    widget1.resize(400, 50)
    widget1.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
