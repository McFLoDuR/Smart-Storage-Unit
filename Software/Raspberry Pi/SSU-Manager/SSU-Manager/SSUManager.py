import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import LoginScreen

def main():
    app = QtWidgets.QApplication(sys.argv)
    lgs = QtWidgets.QMainWindow()
    ui = LoginScreen.Ui_LoginScreen()
    ui.setupUi(lgs)
    lgs.showFullScreen()
    t = QtCore.QTimer()
    t.singleShot(0, ui.onLoad_LoginScreen)
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()