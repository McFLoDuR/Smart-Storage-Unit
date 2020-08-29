from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
import db_connector, User, ShowStorageSlotScreen

MySQLDatabase = db_connector.Database(host = "localhost", user = "ssu_db", password = "ssu_FRS", database = "ssu")

class Ui_SetStorageInformationScreen(object):
    def setupUi(self, SetStorageInformationScreen, parentScreen, parentForm, itemID, storeInformation, storagep=[]):
        self.Form = SetStorageInformationScreen
        self.Parent = parentScreen
        self.ParentForm = parentForm
        self.ItemID = itemID
        self.StoreInformation = storeInformation
        self.Storagep = storagep

        SetStorageInformationScreen.setObjectName("SetStorageInformationScreen")
        SetStorageInformationScreen.resize(798, 473)
        font = QtGui.QFont()
        font.setPointSize(14)
        SetStorageInformationScreen.setFont(font)
        SetStorageInformationScreen.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.centralwidget = QtWidgets.QWidget(SetStorageInformationScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancel.setGeometry(QtCore.QRect(10, 410, 181, 51))
        self.btn_cancel.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_next = QtWidgets.QPushButton(self.centralwidget)
        self.btn_next.setGeometry(QtCore.QRect(610, 410, 181, 51))
        self.btn_next.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.btn_next.setObjectName("btn_next")
        self.nud_minQuantity = QtWidgets.QSpinBox(self.centralwidget)
        self.nud_minQuantity.setGeometry(QtCore.QRect(200, 160, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.nud_minQuantity.setFont(font)
        self.nud_minQuantity.setAlignment(QtCore.Qt.AlignCenter)
        self.nud_minQuantity.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.nud_minQuantity.setStyleSheet("QSpinBox::up-button { width: 35px; } " + 
                                           "QSpinBox::down-button { width: 35px; }")
        self.nud_minQuantity.setObjectName("nud_minQuantity")
        self.nud_maxQuantity = QtWidgets.QSpinBox(self.centralwidget)
        self.nud_maxQuantity.setGeometry(QtCore.QRect(440, 160, 171, 81))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.nud_maxQuantity.setFont(font)
        self.nud_maxQuantity.setAlignment(QtCore.Qt.AlignCenter)
        self.nud_maxQuantity.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.nud_maxQuantity.setStyleSheet("QSpinBox::up-button { width: 35px; } " + 
                                           "QSpinBox::down-button { width: 35px; }")
        self.nud_maxQuantity.setObjectName("nud_maxQuantity")
        self.lbl_minQuantity = QtWidgets.QLabel(self.centralwidget)
        self.lbl_minQuantity.setGeometry(QtCore.QRect(200, 130, 171, 31))
        self.lbl_minQuantity.setObjectName("lbl_minQuantity")
        self.lbl_maxQiantity = QtWidgets.QLabel(self.centralwidget)
        self.lbl_maxQiantity.setGeometry(QtCore.QRect(440, 130, 171, 31))
        self.lbl_maxQiantity.setObjectName("lbl_maxQiantity")
        self.lbl_title = QtWidgets.QLabel(self.centralwidget)
        self.lbl_title.setGeometry(QtCore.QRect(0, 10, 801, 71))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_title.setFont(font)
        self.lbl_title.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_title.setObjectName("lbl_title")
        self.chb_alarmActive = QtWidgets.QCheckBox(self.centralwidget)
        self.chb_alarmActive.setGeometry(QtCore.QRect(300, 290, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.chb_alarmActive.setFont(font)
        self.chb_alarmActive.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.chb_alarmActive.setObjectName("chb_alarmActive")
        SetStorageInformationScreen.setCentralWidget(self.centralwidget)

        self.nud_maxQuantity.setValue(int(self.StoreInformation[0]))
        self.nud_minQuantity.setValue(1)

        self.nud_maxQuantity.setMinimum(int(self.StoreInformation[0]))
        self.nud_minQuantity.setMinimum(1)

        self.nud_maxQuantity.setMaximum(10000)
        self.nud_minQuantity.setMaximum(10000)

        self.retranslateUi(SetStorageInformationScreen)
        self.btn_cancel.clicked.connect(self.btn_cancel_clicked)
        self.btn_next.clicked.connect(self.btn_next_clicked)
        self.nud_maxQuantity.valueChanged.connect(self.nud_maxQuantity_changed)
        self.nud_minQuantity.valueChanged.connect(self.nud_minQuantity_changed)
        QtCore.QMetaObject.connectSlotsByName(SetStorageInformationScreen)

    def retranslateUi(self, SetStorageInformationScreen):
        _translate = QtCore.QCoreApplication.translate
        SetStorageInformationScreen.setWindowTitle(_translate("SetStorageInformationScreen", "MainWindow"))
        self.btn_cancel.setText(_translate("SetStorageInformationScreen", "Cancel"))
        self.btn_next.setText(_translate("SetStorageInformationScreen", "Next"))
        self.lbl_minQuantity.setText(_translate("SetStorageInformationScreen", "Minimum Quantity:"))
        self.lbl_maxQiantity.setText(_translate("SetStorageInformationScreen", "Maximal Quantity:"))
        self.lbl_title.setText(_translate("SetStorageInformationScreen", "Set Storage Settings"))
        self.chb_alarmActive.setText(_translate("SetStorageInformationScreen", "Activate item alarm"))

    def btn_cancel_clicked(self):
        self.closeForm()

    def nud_maxQuantity_changed(self):
        max = self.nud_maxQuantity.value()
        min = self.nud_minQuantity.value()
        
        if (min > max):
            self.nud_minQuantity.setValue(max)

    def nud_minQuantity_changed(self):
        max = self.nud_maxQuantity.value()
        min = self.nud_minQuantity.value()
        
        if (min > max):
            self.nud_maxQuantity.setValue(min)

    def btn_next_clicked(self):
        quantity = int(self.StoreInformation[0])
        quantityMin = self.nud_minQuantity.value()
        quantityMax = self.nud_maxQuantity.value()
        if (self.chb_alarmActive.isChecked()):
            alarmActivated = "1"
        else:
            alarmActivated = "0"
        storagehID = self.StoreInformation[2]
        insidePos = self.StoreInformation[3]
        dividers = self.StoreInformation[4]

        MySQLDatabase.execDML("UPDATE storageh SET firstPartition=" + str(dividers[0]) + " ,secondPartition=" + str(dividers[1]) + " ,thirdPartition=" + str(dividers[2]) + " " +
                              "WHERE ID=" + str(storagehID))

        for row in self.Storagep:
            MySQLDatabase.execDML("UPDATE storagep SET insidePosition=" + str(row[3]) + " WHERE ID=" + str(row[0]))

        MySQLDatabase.execDML("INSERT INTO storagep(storagehID, itemID, insidePosition, quantity, quantityMin, quantityMax, alarmActivated) " +
                              "VALUES(" + str(storagehID) + ", " + str(self.ItemID) + ", " + str(insidePos) + ", " + str(0) + ", " + str(quantityMin) + "" + 
                              ", " + str(quantityMax) + ", " + alarmActivated + ")")

        MySQLDatabase.execDML("UPDATE storagep SET alarmActivated=" + alarmActivated + " WHERE itemID=" + str(self.ItemID))

        result = MySQLDatabase.execSelect("SELECT sp.ID, sh.storagePosition, sh.firstPartition, sh.secondPartition, sh.thirdPartition, sp.insidePosition, sp.quantity " +
	                                      "FROM storagep sp, storageh sh " +
	                                      "WHERE sh.ID=" + str(storagehID) + " AND " +
	                                      "sp.storagehID = sh.ID AND itemID=" + str(self.ItemID))[0]

        storageList=[]
        storageList.append((int(result[0]), int(result[1]), int(result[5]), int(result[2]), int(result[3]), int(result[4]), int(result[6])))
        self.ssss = QtWidgets.QMainWindow()
        self.ui = ShowStorageSlotScreen.Ui_ShowStorageSlotScreen()
        self.ui.setupUi(self.ssss, self.Parent, self.ParentForm, storageList, 0, self.StoreInformation)
        self.ssss.showFullScreen()               
        t = QtCore.QTimer(self.Form)
        t.singleShot(0, self.ui.onLoad_ShowStorageSlotScreen)
        self.Form.deleteLater()

    def closeForm(self):
        self.ParentForm.showFullScreen()
        self.Parent.dh.updateDataTable()
        self.Form.deleteLater()