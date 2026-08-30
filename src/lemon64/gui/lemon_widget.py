import sys
import random
from PySide6 import QtWidgets, QtGui
from PySide6.QtCore import Qt, Slot, Signal
from lemon64.core.lemon import Lemon
from lemon64.core.const import XxxvCode, YypCodeMap, EmojiMap

class LemonWidget(QtWidgets.QWidget):
    singalToNextLemonWidget = Signal()
    def __init__(self):
        super().__init__()    
        self.lemon = Lemon()
        self.layout = QtWidgets.QVBoxLayout(self)
        self.textLemonStatus = QtWidgets.QLabel("灵萌状态", alignment=Qt.AlignCenter)
        self.text6 = QtWidgets.QLabel("上爻", alignment=Qt.AlignCenter)
        self.text5 = QtWidgets.QLabel("五爻", alignment=Qt.AlignCenter)
        self.text4 = QtWidgets.QLabel("四爻", alignment=Qt.AlignCenter)
        self.text3 = QtWidgets.QLabel("三爻", alignment=Qt.AlignCenter)
        self.text2 = QtWidgets.QLabel("二爻", alignment=Qt.AlignCenter)
        self.text1 = QtWidgets.QLabel("初爻", alignment=Qt.AlignCenter)
        self.textList = [self.text1, self.text2, self.text3, self.text4, self.text5, self.text6]
        self.layout.addWidget(self.textLemonStatus)
        self.layout.addWidget(self.text6)
        self.layout.addWidget(self.text5)
        self.layout.addWidget(self.text4)
        self.layout.addWidget(self.text3)
        self.layout.addWidget(self.text2)
        self.layout.addWidget(self.text1)

    @Slot()
    def updateText(self, food=None):
        if food is not None: #喂食
            self.lemon.feedXxxv(food)
        if self.lemon.yyp.isCompleted(): #进位
            self.singalToNextLemonWidget.emit()
        #更新text
        if self.lemon.octaNopoPentaMiri.octaNopoCode and self.lemon.octaNopoPentaMiri.pentaMiriCode:
            lemonStatus = ",".join([
                YypCodeMap[self.lemon.yyp.getYypId()].value[1],
                EmojiMap[self.lemon.octaNopoPentaMiri.octaNopoCode],
                EmojiMap[self.lemon.octaNopoPentaMiri.pentaMiriCode]
            ])
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
            self.textList[textIndex].setText(EmojiMap[xxxvCode])
            textIndex += 1

