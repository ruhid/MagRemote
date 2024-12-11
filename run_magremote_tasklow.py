import sys
from PyQt5.QtWidgets import QDialog, QApplication, QTableWidgetItem, QFileDialog, QMainWindow, QLineEdit, QWidget, \
    QLCDNumber, QSlider
from magremote_ui import *
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
        self.ui.checkBoxPowerA.clicked.connect(self.set)
        self.ui.checkBoxPowerB.clicked.connect(self.set)
        self.ui.pushButtonDisArm.clicked.connect(self.disarm)
        self.ui.pushButtonDisconnect.clicked.connect(self.disconnect_mag)
        self.ui.verticalSliderPowerA.valueChanged.connect(self.syncronyse)
        self.ui.verticalSliderPowerB.valueChanged.connect(self.syncronyse)
        self.ui.verticalSliderDelay.valueChanged.connect(self.syncronyse)
        self.ui.pushButtonsSync.clicked.connect(self.sync_from_device)
        self.ui.comboBoxSerial.currentIndexChanged.connect(self.port_assign)
        self.show()

    def port_assign(self):
        self.port = self.serial_devices[self.ui.comboBoxSerial.currentIndex()]

    def sync_from_device(self):
        status = self.myMagstim.getParameters()
        a=int(status[1]['bistimParam']['powerA'])
        b=int(status[1]['bistimParam']['powerB'])
        d=int(status[1]['bistimParam']['ppOffset'])
        self.ui.verticalSliderPowerA.setValue(a)
        self.ui.verticalSliderPowerB.setValue(b)
        self.ui.verticalSliderDelay.setValue(d)

    def disconnect_mag(self):
        try:
            self.port = self.serial_devices[self.ui.comboBoxSerial.currentIndex()]
            ser = serial.Serial(port=self.port)
            if ser.isOpen:
                ser.close()
                self.ui.textBrowserStatus.append("disconnected")
                self.myMagstim.disconnect()
        except Exception as e:
            print(f"cant disconnect{e}")
            pass

    def serials(self):
        self.ui.comboBoxSerial.clear()
        self.seriallist = list_ports.comports()
        self.serial_devices = [i.device for i in self.seriallist]
        for i in self.seriallist:
            self.ui.comboBoxSerial.addItem(str(i))

    def connect(self):
        self.port=self.serial_devices[self.ui.comboBoxSerial.currentIndex()]
        print(self.port)
        self.disconnect_mag()
        try:
            self.myMagstim = magstim.BiStim(self.port)
            time.sleep(5)
            self.myMagstim.connect( )
            self.ui.mainArea.setEnabled(True)
            self.ui.pushButtonDisconnect.setEnabled(True)
            self.update_status()
        except Exception as e:
            print(e)
            self.ui.textBrowserStatus.setText(str(e))

    def syncronyse(self):
        self.ui.spinBoxPowerA.setValue(self.ui.verticalSliderPowerA.value())
        self.ui.spinBoxPowerB.setValue(self.ui.verticalSliderPowerB.value())
        self.ui.spinBoxDelay.setValue(self.ui.verticalSliderDelay.value())
        self.set()
    def set(self):
        self.ui.verticalSliderPowerA.setValue(self.ui.spinBoxPowerA.value())
        self.ui.verticalSliderPowerB.setValue(self.ui.spinBoxPowerB.value())
        self.ui.verticalSliderDelay.setValue(self.ui.spinBoxDelay.value())
        powerB = self.ui.spinBoxPowerB.value()
        delay=self.ui.spinBoxDelay.value()
        if self.ui.checkBoxPowerA.isChecked():
            powerA = self.ui.spinBoxPowerA.value()
        else:
            powerA=0

        if self.ui.checkBoxPowerB.isChecked():
            powerB = self.ui.spinBoxPowerB.value()
        else:
            powerB=0
        self.myMagstim.setPowerA(powerA, receipt=False, delay=False)
        self.myMagstim.setPowerB(powerB, receipt=False, delay=False)
        self.myMagstim.setPulseInterval(delay)
        self.update_status()

    def update_status(self):
        status = self.myMagstim.getParameters()
        temperature=self.myMagstim.getTemperature()
        self.ui.textBrowserStatus.setText(str(status))
        a=int(status[1]['bistimParam']['powerA'])
        b=int(status[1]['bistimParam']['powerB'])
        d=int(status[1]['bistimParam']['ppOffset'])
        self.ui.lcdNumberPowerA.display(a)
        self.ui.lcdNumberPowerB.display(b)
        self.ui.lcdNumberPowerDelay.display(d)
        self.ui.lcdNumberTemp1.display(temperature[1]["magstimTemp"]['coil1Temp'])
        self.ui.lcdNumberTemp2.display(temperature[1]["magstimTemp"]['coil2Temp'])
        self.ui.textBrowserStatus.append(str(temperature))
    def arm(self):
        self.myMagstim.arm()
        self.update_status()

    def disarm(self):
        self.myMagstim.disarm()
        self.update_status()

    def fire(self):
        self.myMagstim.fire()
        self.update_status()






if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec_())

