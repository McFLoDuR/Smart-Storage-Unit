from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
import User, os

class Ui_CreateInventoryReportScreen(object):
    def setupUi(self, CreateInventoryReportScreen):
        self.Form = CreateInventoryReportScreen

        CreateInventoryReportScreen.setObjectName("CreateInventoryReportScreen")
        CreateInventoryReportScreen.resize(802, 487)
        font = QtGui.QFont()
        font.setPointSize(14)
        CreateInventoryReportScreen.setFont(font)
        CreateInventoryReportScreen.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.centralwidget = QtWidgets.QWidget(CreateInventoryReportScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancel.setGeometry(QtCore.QRect(10, 10, 181, 51))
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_ir1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ir1.setGeometry(QtCore.QRect(130, 270, 541, 61))
        self.btn_ir1.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.btn_ir1.setObjectName("btn_ir1")
        self.pcb_logo = QtWidgets.QLabel(self.centralwidget)
        self.pcb_logo.setGeometry(QtCore.QRect(310, 10, 161, 161))
        self.pcb_logo.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.pcb_logo.setText("")
        self.pcb_logo.setPixmap(QtGui.QPixmap("images/icon.PNG"))
        self.pcb_logo.setScaledContents(True)
        self.pcb_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.pcb_logo.setObjectName("pcb_logo")
        self.btn_ir2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ir2.setGeometry(QtCore.QRect(130, 340, 541, 61))
        self.btn_ir2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.btn_ir2.setObjectName("btn_ir2")
        self.btn_ir3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_ir3.setGeometry(QtCore.QRect(130, 410, 541, 61))
        self.btn_ir3.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.btn_ir3.setObjectName("btn_ir3")
        self.lbl_email = QtWidgets.QLabel(self.centralwidget)
        self.lbl_email.setGeometry(QtCore.QRect(0, 220, 801, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lbl_email.setFont(font)
        self.lbl_email.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_email.setObjectName("lbl_email")
        self.lbl_title = QtWidgets.QLabel(self.centralwidget)
        self.lbl_title.setGeometry(QtCore.QRect(0, 180, 801, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title.setFont(font)
        self.lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_title.setObjectName("lbl_title")
        CreateInventoryReportScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(CreateInventoryReportScreen)
        self.btn_ir1.clicked.connect(self.btn_CreateInventoryReport1_clicked)
        self.btn_ir2.clicked.connect(self.btn_CreateInventoryReport2_clicked)
        self.btn_ir3.clicked.connect(self.btn_CreateInventoryReport3_clicked)
        self.btn_cancel.clicked.connect(self.exitForm)
        QtCore.QMetaObject.connectSlotsByName(CreateInventoryReportScreen)

    def retranslateUi(self, CreateInventoryReportScreen):
        _translate = QtCore.QCoreApplication.translate
        CreateInventoryReportScreen.setWindowTitle(_translate("CreateInventoryReportScreen", "MainWindow"))
        self.btn_ir1.setText(_translate("CreateInventoryReportScreen", "Get all currently stored items!"))
        self.btn_ir2.setText(_translate("CreateInventoryReportScreen", "Get all items ever been added to the database!"))
        self.btn_ir3.setText(_translate("CreateInventoryReportScreen", "Get all items which are low in quantity!"))
        self.lbl_email.setText(_translate("CreateInventoryReportScreen", "To: {email}"))
        self.btn_cancel.setText(_translate("CreateInventoryReportScreen", "Cancel"))
        self.lbl_title.setText(_translate("CreateInventoryReportScreen", "Create Inventory Report"))

    def btn_CreateInventoryReport1_clicked(self):
        self.executeCommand(1, User.User.Id)
        self.showInformation()
        self.exitForm()

    def btn_CreateInventoryReport2_clicked(self):
        self.executeCommand(2, User.User.Id)
        self.showInformation()
        self.exitForm()

    def btn_CreateInventoryReport3_clicked(self):
        self.executeCommand(3, User.User.Id)
        self.showInformation()
        self.exitForm()

    def executeCommand(self, mode, userID):
        os.system("python3 /home/ssu/Desktop/PDF-Creator/PDF_Creator.py --mode " + str(mode) + " --userID " + str(userID) + " &")

    def showInformation(self):
        msg = QMessageBox(self.Form)
        msg.setIcon(QMessageBox.Information) 
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setWindowTitle("Information!")
        msg.setText("You will shortly receive your report! Please check your spam folder if you don't see the email in your inbox!")                               
        msg.exec_()

    def exitForm(self):        
        self.Form.deleteLater()

    def onLoad_CreateInventoryReportScreen(self):
        self.lbl_email.setText("To: " +  User.User.Email)