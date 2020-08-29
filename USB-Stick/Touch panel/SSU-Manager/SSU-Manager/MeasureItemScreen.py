from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import ShowStorageSlotScreen, SelectStorageSlotScreen
import db_connector, User, SSUFunctions

MySQLDatabase = db_connector.Database(host = "localhost", user = "ssu_db", password = "ssu_FRS", database = "ssu")

class Ui_MeasureItemScreen(object):
    def setupUi(self, MeasureItemScreen, parent, parentForm, itemID, storeInformation):
        self.Form = MeasureItemScreen
        self.Parent = parent
        self.ParentForm = parentForm
        self.ItemID = itemID
        self.StoreInformation = storeInformation

        MeasureItemScreen.setObjectName("MeasureItemScreen")
        MeasureItemScreen.resize(800, 480)
        font = QtGui.QFont()
        font.setPointSize(14)
        MeasureItemScreen.setFont(font)
        MeasureItemScreen.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.centralwidget = QtWidgets.QWidget(MeasureItemScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancel.setGeometry(QtCore.QRect(10, 420, 181, 51))
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_next = QtWidgets.QPushButton(self.centralwidget)
        self.btn_next.setGeometry(QtCore.QRect(610, 420, 181, 51))
        self.btn_next.setObjectName("btn_next")
        self.lbl_item = QtWidgets.QLabel(self.centralwidget)
        self.lbl_item.setGeometry(QtCore.QRect(0, 10, 801, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_item.setFont(font)
        self.lbl_item.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_item.setObjectName("lbl_item")
        self.btn_setWeight = QtWidgets.QPushButton(self.centralwidget)
        self.btn_setWeight.setGeometry(QtCore.QRect(280, 270, 241, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btn_setWeight.setFont(font)
        self.btn_setWeight.setObjectName("btn_setWeight")
        self.lbl_intruction = QtWidgets.QLabel(self.centralwidget)
        self.lbl_intruction.setGeometry(QtCore.QRect(0, 70, 801, 141))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lbl_intruction.setFont(font)
        self.lbl_intruction.setTextFormat(QtCore.Qt.RichText)
        self.lbl_intruction.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_intruction.setWordWrap(True)
        self.lbl_intruction.setObjectName("lbl_intruction")
        self.lbl_weight = QtWidgets.QLabel(self.centralwidget)
        self.lbl_weight.setGeometry(QtCore.QRect(0, 220, 801, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_weight.setFont(font)
        self.lbl_weight.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_weight.setObjectName("lbl_weight")
        MeasureItemScreen.setCentralWidget(self.centralwidget)

        self.btn_next.setEnabled(False)

        self.tmr_weightUpdater = QTimer(self.Form)
        self.tmr_weightUpdater.timeout.connect(self.timer_tick) 

        self.retranslateUi(MeasureItemScreen)
        self.btn_cancel.clicked.connect(self.btn_cancel_clicked)
        self.btn_setWeight.clicked.connect(self.btn_setWeight_clicked)
        self.btn_next.clicked.connect(self.btn_next_clicked)
        QtCore.QMetaObject.connectSlotsByName(MeasureItemScreen)

    def retranslateUi(self, MeasureItemScreen):
        _translate = QtCore.QCoreApplication.translate
        MeasureItemScreen.setWindowTitle(_translate("MeasureItemScreen", "MainWindow"))
        self.btn_cancel.setText(_translate("MeasureItemScreen", "Cancel"))
        self.btn_next.setText(_translate("MeasureItemScreen", "Next"))
        self.lbl_item.setText(_translate("MeasureItemScreen", "Measure weight of {item}"))
        self.btn_setWeight.setText(_translate("MeasureItemScreen", "Set weight"))
        self.lbl_intruction.setText(_translate("MeasureItemScreen", "Please put 20 items on the micro scale!"))
        self.lbl_weight.setText(_translate("MeasureItemScreen", "0.00000 g"))

    def btn_cancel_clicked(self):
        self.closeForm()

    def btn_setWeight_clicked(self):
        weight = float(SSUFunctions.getMicroScaleResult())

        msg = QMessageBox(self.Form)
        msg.setIcon(QMessageBox.Warning) 
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        msg.setWindowTitle("Correct quantity?!")
        

        if (weight < 2.0):
            msg.setText("Your item is pretty light are you sure that there are 20 items on the micro scale!?")                               
            buttonResult = msg.exec_()

            if (buttonResult == QMessageBox.Yes):
                self.saveWeight(1000.0)

        elif (weight > 90.0):
            msg.setText("Your item is pretty heavy are you sure that there are only 20 items on the micro scale!?")                               
            buttonResult = msg.exec_()

            if (buttonResult == QMessageBox.Yes):
                self.saveWeight(1000.0)
        else:
            self.saveWeight(abs(weight / 20.0))
       
    def saveWeight(self, weight):       
        MySQLDatabase.execDML("UPDATE items SET weight=" + str(weight) + " WHERE ID=" + str(self.ItemID))
        self.btn_next.setEnabled(True)
        self.btn_setWeight.setEnabled(False)

    def btn_next_clicked(self):
        if(SSUFunctions.isMicroScaleEmpty()):
            if (self.StoreInformation[1]): 
                self.tmr_weightUpdater.deleteLater()
                SSUFunctions.stopMicroScale()
                result = MySQLDatabase.execSelect("SELECT sp.ID, sh.storagePosition, sh.firstPartition, sh.secondPartition, sh.thirdPartition, sp.insidePosition, sp.quantity " +
	                                              "FROM storagep sp, storageh sh " +
	                                              "WHERE sh.ID=(SELECT storagehID FROM storagep " +
	                                              "WHERE (quantityMax >= (quantity + " + str(self.StoreInformation[0]) + ")) AND itemID=" + str(self.ItemID) + " "
	                                              "ORDER BY quantity ASC LIMIT 1) AND " +
	                                              "sp.storagehID = sh.ID AND itemID=" + str(self.ItemID))[0]
                storageList = []
                storageList.append((int(result[0]), int(result[1]), int(result[5]), int(result[2]), int(result[3]), int(result[4]), int(result[6])))
                self.ssss = QtWidgets.QMainWindow()
                self.ui = ShowStorageSlotScreen.Ui_ShowStorageSlotScreen()
                self.ui.setupUi(self.ssss, self.Parent, self.ParentForm, storageList, 0, self.StoreInformation)
                self.ssss.showFullScreen()               
                t = QtCore.QTimer(self.Form)
                t.singleShot(0, self.ui.onLoad_ShowStorageSlotScreen)
                self.Form.deleteLater()
            else:
                self.tmr_weightUpdater.deleteLater()
                SSUFunctions.stopMicroScale()
                self.ssss = QtWidgets.QMainWindow()
                self.ui = SelectStorageSlotScreen.Ui_SelectStorageSlotScreen()
                self.ui.setupUi(self.ssss, self.Parent, self.ParentForm, self.ItemID, self.StoreInformation)
                self.ssss.showFullScreen()               
                t = QtCore.QTimer(self.Form)
                t.singleShot(0, self.ui.onLoad_SelectStorageSlotScreen)
                self.Form.deleteLater()
        else:
            msg = QMessageBox(self.Form)
            msg.setIcon(QMessageBox.Warning) 
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setWindowTitle("ERROR!")
            msg.setText("Please clear the micro scale before retraction!")                               
            msg.exec_()

    def closeForm(self):
        self.tmr_weightUpdater.deleteLater()
        SSUFunctions.stopMicroScale()
        self.ParentForm.showFullScreen()
        self.Parent.dh.updateDataTable()
        self.Form.deleteLater()

    def onLoad_MeasureItemScreen(self):
        articleNumber = str(MySQLDatabase.execSelect("SELECT articleNumber FROM items WHERE ID=" + str(self.ItemID))[0][0])
        self.lbl_item.setText("Measure weight of "+ str(articleNumber))
        SSUFunctions.startMicroScale()
        self.tmr_weightUpdater.start(500)

    def timer_tick(self):
        self.lbl_weight.setText(str(SSUFunctions.getMicroScaleResult()) + " g")