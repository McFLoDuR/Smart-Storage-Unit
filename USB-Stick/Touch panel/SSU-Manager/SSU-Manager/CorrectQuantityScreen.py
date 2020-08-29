from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import db_connector, User, DataHandler, ShowStorageSlotScreen

MySQLDatabase = db_connector.Database(host = "localhost", user = "ssu_db", password = "ssu_FRS", database = "ssu")

class Ui_CorrectQuantityScreen(object):
    def setupUi(self, CorrectQuantityScreen, mainScreen):
        self.Form = CorrectQuantityScreen
        self.MainScreen = mainScreen

        CorrectQuantityScreen.setObjectName("CorrectQuantityScreen")
        CorrectQuantityScreen.resize(802, 487)
        font = QtGui.QFont()
        font.setPointSize(14)
        CorrectQuantityScreen.setFont(font)
        CorrectQuantityScreen.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.centralwidget = QtWidgets.QWidget(CorrectQuantityScreen)
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
        self.pcb_logo = QtWidgets.QLabel(self.centralwidget)
        self.pcb_logo.setGeometry(QtCore.QRect(40, 10, 141, 141))
        self.pcb_logo.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.pcb_logo.setText("")
        self.pcb_logo.setPixmap(QtGui.QPixmap("images/icon.PNG"))
        self.pcb_logo.setScaledContents(True)
        self.pcb_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.pcb_logo.setObjectName("pcb_logo")
        self.btn_setQuantity = QtWidgets.QPushButton(self.centralwidget)
        self.btn_setQuantity.setGeometry(QtCore.QRect(10, 360, 201, 51))
        self.btn_setQuantity.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.btn_setQuantity.setObjectName("btn_setQuantity")
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
        CorrectQuantityScreen.setCentralWidget(self.centralwidget)

        self.btn_setQuantity.setEnabled(False)
        self.dh = DataHandler.DataHandlerMainScreen(dtv=self.dtv_items, liv=self.liv_itemData, txb=self.txb_search)
        self.retranslateUi(CorrectQuantityScreen)
        self.btn_cancel.clicked.connect(self.btn_cancel_clicked)
        self.btn_search.clicked.connect(self.btn_search_clicked)
        self.btn_setQuantity.clicked.connect(self.btn_setQuantity_clicked)
        self.dtv_items.itemSelectionChanged.connect(self.item_selected)
        QtCore.QMetaObject.connectSlotsByName(CorrectQuantityScreen)

    def retranslateUi(self, CorrectQuantityScreen):
        _translate = QtCore.QCoreApplication.translate
        CorrectQuantityScreen.setWindowTitle(_translate("CorrectQuantityScreen", "MainWindow"))
        self.btn_search.setText(_translate("CorrectQuantityScreen", "Search"))
        self.btn_cancel.setText(_translate("CorrectQuantityScreen", "Cancel"))
        self.btn_setQuantity.setText(_translate("CorrectQuantityScreen", "Correct Quantity"))
        self.lbl_itemData.setText(_translate("CorrectQuantityScreen", "Item Data:"))
        self.lbl_screenTitle.setText(_translate("CorrectQuantityScreen", "Correct Quantity"))

    def btn_cancel_clicked(self):
        User.User.MainScreen.showFullScreen()
        self.MainScreen.dh.updateDataTable()
        self.Form.deleteLater()

    def btn_setQuantity_clicked(self):
        self.buildItemList()
        self.ssss = QtWidgets.QMainWindow()
        self.ui = ShowStorageSlotScreen.Ui_ShowStorageSlotScreen()
        self.ui.setupUi(self.ssss, self, self.Form, self.__storageList, 2)
        self.ssss.showFullScreen()
        self.Form.hide()
        t = QtCore.QTimer(self.Form)
        t.singleShot(0, self.ui.onLoad_ShowStorageSlotScreen)


    def btn_search_clicked(self):
        self.btn_setQuantity.setEnabled(False)
        self.dh.updateDataTable()

    def item_selected(self):
        self.btn_setQuantity.setEnabled(True)
        self.dh.rowSelected()
        self.itemID = self.dh.rowIndex
        if(self.itemID > 0):
            self.btn_setQuantity.setEnabled(True)
        else:
            self.btn_setQuantity.setEnabled(False)

    def buildItemList(self):
        result = MySQLDatabase.execSelect("SELECT sp.ID, sh.storagePosition, sh.firstPartition, sh.secondPartition, sh.thirdPartition, sp.insidePosition, sp.quantity " +
	                                      "FROM storagep sp, storageh sh " +
	                                      "WHERE sp.itemID=" + str(self.itemID) + " AND sp.storagehID = sh.ID " + 
	                                      "ORDER BY sp.quantity ASC")

        self.__storageList = []
        for row in result:
            self.__storageList.append([int(row[0]), int(row[1]), int(row[5]), int(row[2]), int(row[3]), int(row[4]), int(row[6])])

    def onLoad_CorrectQuantityScreen(self):
        self.dh.updateDataTable()