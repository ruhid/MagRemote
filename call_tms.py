import sys


from PyQt5.QtWidgets import QDialog, QApplication,QTableWidgetItem,QFileDialog,QMainWindow
from tms import *
from magpy import magstim
import serial
from serial.tools import list_ports
import random
import time
import threading
import os

class MyForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.serials()
        self.ui.pushButtonRescanSerials.clicked.connect(self.serials)
        self.ui.pushButtonConnect.clicked.connect(self.connect)
        self.ui.pushButtonSet.clicked.connect(self.set)
        self.ui.pushButtonArm.clicked.connect(self.arm)
        self.ui.pushButtonFire.clicked.connect(self.fire)
        self.ui.spinBoxDelay.valueChanged.connect(self.set)
        self.ui.spinBoxPowerA.valueChanged.connect(self.set)
        self.ui.spinBoxPowerB.valueChanged.connect(self.set)
        self.show()

    def serials(self):
        self.ui.comboBoxSerial.clear()
        self.seriallist = list_ports.comports()
        self.serial_devices = [i.device for i in self.seriallist]
        for i in self.seriallist:
            self.ui.comboBoxSerial.addItem(str(i))

    def connect(self):
        port=self.serial_devices[self.ui.comboBoxSerial.currentIndex()]
        print(port)
        self.myMagstim = magstim.BiStim(port)
        time.sleep(5)
        self.myMagstim.connect()
        print(self.myMagstim.getParameters())

    def set(self):
        powerA=self.ui.spinBoxPowerA.value()
        powerB = self.ui.spinBoxPowerB.value()
        delay=self.ui.spinBoxDelay.value()
        self.myMagstim.setPowerA(powerA, receipt=False, delay=False)
        self.myMagstim.setPowerB(powerB, receipt=False, delay=False)
        self.myMagstim.setPulseInterval(delay)

    def arm(self):
        self.myMagstim.arm()

    def fire(self):
        self.myMagstim.fire()






if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())

