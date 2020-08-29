from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import db_connector, User, DataHandler, ItemQuantityScreen

MySQLDatabase = db_connector.Database(host = "localhost", user = "ssu_db", password = "ssu_FRS", database = "ssu")

class Ui_StoreItemScreen(object):
    def setupUi(self, StoreItemScreen, mainScreen):
        self.Form = StoreItemScreen
        self.MainScreen = mainScreen

        StoreItemScreen.setObjectName("StoreItemScreen")
        StoreItemScreen.resize(800, 480)
        font = QtGui.QFont()
        font.setPointSize(14)
        StoreItemScreen.setFont(font)
        StoreItemScreen.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.centralwidget = QtWidgets.QWidget(StoreItemScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_screenTitle = QtWidgets.QLabel(self.centralwidget)
        self.lbl_screenTitle.setGeometry(QtCore.QRect(220, 10, 580, 50))
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
        self.dtv_items.setGeometry(QtCore.QRect(220, 120, 571, 351))
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
        self.btn_store = QtWidgets.QPushButton(self.centralwidget)
        self.btn_store.setGeometry(QtCore.QRect(10, 360, 201, 51))
        self.btn_store.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.btn_store.setObjectName("btn_store")
        self.btn_store.setEnabled(False)
        self.pcb_logo = QtWidgets.QLabel(self.centralwidget)
        self.pcb_logo.setGeometry(QtCore.QRect(40, 10, 141, 141))
        self.pcb_logo.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.pcb_logo.setText("")
        self.pcb_logo.setPixmap(QtGui.QPixmap("images/icon.PNG"))
        self.pcb_logo.setScaledContents(True)
        self.pcb_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.pcb_logo.setObjectName("pcb_logo")
        self.liv_itemData = QtWidgets.QListWidget(self.centralwidget)
        self.liv_itemData.setGeometry(QtCore.QRect(10, 180, 201, 171))
        self.liv_itemData.setObjectName("liv_itemData")
        self.lbl_itemData = QtWidgets.QLabel(self.centralwidget)
        self.lbl_itemData.setGeometry(QtCore.QRect(10, 150, 201, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_itemData.setFont(font)
        self.lbl_itemData.setObjectName("lbl_itemData")
        StoreItemScreen.setCentralWidget(self.centralwidget)

        self.ItemID = 0
        self.dh = DataHandler.DataHandlerStorageScreen(dtv=self.dtv_items, liv=self.liv_itemData, txb=self.txb_search)
        self.retranslateUi(StoreItemScreen)
        self.btn_store.clicked.connect(self.btn_store_clicked)
        self.btn_cancel.clicked.connect(self.btn_cancel_clicked)
        self.btn_search.clicked.connect(self.btn_search_clicked)
        self.dtv_items.itemSelectionChanged.connect(self.item_selected)
        QtCore.QMetaObject.connectSlotsByName(StoreItemScreen)

    def retranslateUi(self, StoreItemScreen):
        _translate = QtCore.QCoreApplication.translate
        StoreItemScreen.setWindowTitle(_translate("StoreItemScreen", "MainWindow"))
        self.btn_search.setText(_translate("StoreItemScreen", "Search"))
        self.btn_cancel.setText(_translate("StoreItemScreen", "Cancel"))
        self.btn_store.setText(_translate("StoreItemScreen", "Store"))
        self.lbl_itemData.setText(_translate("StoreItemScreen", "Item Data:"))
        self.lbl_screenTitle.setText(_translate("StoreItemScreen", "Store Items"))

    def btn_store_clicked(self):
        self.iqs = QtWidgets.QMainWindow()
        self.ui = ItemQuantityScreen.Ui_ItemScreen()
        self.ui.setupUi(self.iqs, self, self.Form, self.ItemID, False)
        self.iqs.showFullScreen()
        self.Form.hide()
        t = QtCore.QTimer(self.Form)
        t.singleShot(0, self.ui.onLoad_ItemQuantityScreen)

    def btn_cancel_clicked(self):
        self.backToMainScreen()

    def btn_search_clicked(self):        
        self.dh.updateDataTable()
        self.btn_store.setEnabled(False)

    def item_selected(self):
        self.dh.rowSelected()
        self.ItemID = self.dh.rowIndex
        if (self.ItemID > 0):
            self.btn_store.setEnabled(True)
        else:
            self.btn_store.setEnabled(False)

    def backToMainScreen(self):
        User.User.MainScreen.showFullScreen()
        self.MainScreen.dh.updateDataTable()
        self.Form.deleteLater()

    def onLoad_StoreItemScreen(self):
        self.dh.updateDataTable()