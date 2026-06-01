import sys
from PySide6 import QtCore, QtWidgets, QtGui
from penta_lemon.xxxv_generator.time_driven import TimeDrivenXxxvGen
from penta_lemon.gui.lemon_widget import LemonWidget

def main():
    app = QtWidgets.QApplication([])

    #第0位元widget
    widget0 = LemonWidget()
    timeDrivenXxxvGen = TimeDrivenXxxvGen()
    timer = QtCore.QTimer()
    timer.timeout.connect(lambda:widget0.updateText(food=timeDrivenXxxvGen.getXxxv()))
    timer.start(1000)
    #第1位元widget
    widget1 = LemonWidget()
    widget0.singalToNextLemonWidget.connect(lambda:widget1.updateText(food=widget0.lemon.getCarryXxxv()))
    #第2位元widget
    widget2 = LemonWidget()
    widget1.singalToNextLemonWidget.connect(lambda:widget2.updateText(food=widget1.lemon.getCarryXxxv()))
    #main window
    mainWin = QtWidgets.QWidget()
    mainWin.resize(1200, 50)
    layout = QtWidgets.QHBoxLayout(mainWin)
    layout.addWidget(widget0)
    layout.addWidget(widget1)
    layout.addWidget(widget2)
    mainWin.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
