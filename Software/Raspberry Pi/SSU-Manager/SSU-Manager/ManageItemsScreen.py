from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import db_connector, User, NewEditItemScreen, DataHandler

MySQLDatabase = db_connector.Database(host = "localhost", user = "ssu_db", password = "ssu_FRS", database = "ssu")

class Ui_ManageItemsScreen(object):
    def setupUi(self, ManageItemsScreen, mainScreen):
        self.Form = ManageItemsScreen
        self.MainScreen = mainScreen

        ManageItemsScreen.setObjectName("ManageItemsScreen")
        ManageItemsScreen.resize(800, 480)
        font = QtGui.QFont()
        font.setPointSize(14)
        ManageItemsScreen.setFont(font)
        ManageItemsScreen.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.centralwidget = QtWidgets.QWidget(ManageItemsScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_screenTitle = QtWidgets.QLabel(self.centralwidget)
        self.lbl_screenTitle.setGeometry(QtCore.QRect(220, 10, 570, 50))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_screenTitle.setFont(font)
        self.lbl_screenTitle.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.lbl_screenTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_screenTitle.setObjectName("lbl_screenTitle")
        self.txb_search = QtWidgets.QLineEdit(self.centralwidget)
        self.txb_search.setGeometry(QtCore.QRect(220, 70, 461, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.txb_search.setFont(font)
        self.txb_search.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.txb_search.setText("")
        self.txb_search.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.txb_search.setObjectName("txb_search")
        self.btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_search.setGeometry(QtCore.QRect(680, 70, 111, 41))
        self.btn_search.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.btn_search.setObjectName("btn_search")
        self.dtv_items = QtWidgets.QTableWidget(self.centralwidget)
        self.dtv_items.setGeometry(QtCore.QRect(220, 120, 571, 291))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dtv_items.setFont(font)
        self.dtv_items.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.dtv_items.setObjectName("dtv_items")
        self.dtv_items.setColumnCount(0)
        self.dtv_items.setRowCount(0)
        self.btn_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancel.setGeometry(QtCore.QRect(10, 420, 201, 51))
        self.btn_cancel.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_new = QtWidgets.QPushButton(self.centralwidget)
        self.btn_new.setGeometry(QtCore.QRect(220, 420, 186, 51))
        self.btn_new.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.btn_new.setObjectName("btn_new")
        self.pcb_logo = QtWidgets.QLabel(self.centralwidget)
        self.pcb_logo.setGeometry(QtCore.QRect(40, 10, 141, 141))
        self.pcb_logo.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.pcb_logo.setText("")
        self.pcb_logo.setPixmap(QtGui.QPixmap("images/icon.PNG"))
        self.pcb_logo.setScaledContents(True)
        self.pcb_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.pcb_logo.setObjectName("pcb_logo")
        self.btn_edit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_edit.setEnabled(False)
        self.btn_edit.setGeometry(QtCore.QRect(413, 420, 186, 51))
        self.btn_edit.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.btn_edit.setObjectName("btn_edit")
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setEnabled(False)
        self.btn_delete.setGeometry(QtCore.QRect(605, 420, 186, 51))
        self.btn_delete.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.btn_delete.setObjectName("btn_delete")
        self.liv_itemData = QtWidgets.QListWidget(self.centralwidget)
        self.liv_itemData.setGeometry(QtCore.QRect(10, 190, 201, 221))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.liv_itemData.setFont(font)
        self.liv_itemData.setObjectName("liv_itemData")
        self.lbl_permissions = QtWidgets.QLabel(self.centralwidget)
        self.lbl_permissions.setGeometry(QtCore.QRect(10, 160, 201, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_permissions.setFont(font)
        self.lbl_permissions.setObjectName("lbl_permissions")
        ManageItemsScreen.setCentralWidget(self.centralwidget)

        self.dh = DataHandler.DataHandlerStorageScreen(dtv=self.dtv_items, liv=self.liv_itemData, txb=self.txb_search)
        self.retranslateUi(ManageItemsScreen)
        self.btn_new.clicked.connect(self.btn_new_clicked)
        self.btn_edit.clicked.connect(self.btn_edit_clicked)
        self.btn_delete.clicked.connect(self.btn_delete_clicked)
        self.btn_cancel.clicked.connect(self.btn_cancel_clicked)
        self.btn_search.clicked.connect(self.btn_search_clicked)  
        self.dtv_items.itemSelectionChanged.connect(self.item_selected)
        QtCore.QMetaObject.connectSlotsByName(ManageItemsScreen)

    def retranslateUi(self, ManageItemsScreen):
        _translate = QtCore.QCoreApplication.translate
        ManageItemsScreen.setWindowTitle(_translate("ManageItemsScreen", "MainWindow"))
        self.btn_search.setText(_translate("ManageItemsScreen", "Search"))
        self.btn_cancel.setText(_translate("ManageItemsScreen", "Cancel"))
        self.btn_new.setText(_translate("ManageItemsScreen", ("New Item")))
        self.btn_edit.setText(_translate("ManageItemsScreen", ("Edit Item")))
        self.btn_delete.setText(_translate("ManageItemsScreen", ("Delete Item")))
        self.lbl_permissions.setText(_translate("ManageItemsScreen", "Item Data:"))
        self.lbl_screenTitle.setText(_translate("ManageItemsScreen", "Manage Items"))

    def btn_cancel_clicked(self):
        User.User.MainScreen.showFullScreen()
        self.MainScreen.dh.updateDataTable()
        self.Form.deleteLater()

    def btn_new_clicked(self):
        self.openNewEditItemScreen(0)

    def btn_edit_clicked(self):
        self.openNewEditItemScreen(self.itemID)

    def openNewEditItemScreen(self, itemID):
        self.neis = QtWidgets.QMainWindow()
        self.ui = NewEditItemScreen.Ui_NewEditItemScreen()
        self.ui.setupUi(self.neis, self.Form, self, itemID)
        self.neis.showFullScreen()
        self.Form.hide()
        t = QtCore.QTimer(self.Form)
        t.singleShot(0, self.ui.onLoad_NewEditItemScreen)

    def btn_delete_clicked(self):
        msg = QMessageBox(self.Form)
        if (self.dh.quantity > 0):           
            msg.setIcon(QMessageBox.Critical) 
            msg.setStandardButtons(QMessageBox.Ok)
            msg.setWindowTitle("ERROR!")
            msg.setText("This item is not empty!")                               
            msg.exec_()
        else:
            msg.setIcon(QMessageBox.Warning) 
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg.setWindowTitle("Warning!")
            msg.setText("Do you really want to delete this item?")                               
            buttonResult = msg.exec_()

            if (buttonResult == QMessageBox.Yes):
                MySQLDatabase.execDML("DELETE FROM itemdata WHERE itemID=" + str(self.itemID))
                MySQLDatabase.execDML("DELETE FROM items WHERE ID=" + str(self.itemID))
                self.dh.updateDataTable()

    def btn_search_clicked(self):
        self.dh.updateDataTable()
        self.btn_edit.setEnabled(False)
        self.btn_delete.setEnabled(False)

    def item_selected(self):
        self.dh.rowSelected()
        self.itemID = self.dh.rowIndex
        if(self.itemID > 0):
            self.btn_edit.setEnabled(True)
            self.btn_delete.setEnabled(True)
        else:
            self.btn_edit.setEnabled(False)
            self.btn_delete.setEnabled(False)

    def onLoad_ManageUserPermissionScreen(self):
        self.dh.updateDataTable()