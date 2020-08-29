from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import db_connector, User, DataHandler, SSUFunctions

MySQLDatabase = db_connector.Database(host = "localhost", user = "ssu_db", password = "ssu_FRS", database = "ssu")

class Ui_MoveRemoveStorageSlotScreen(object):
    def setupUi(self, MoveRemoveStorageSlotScreen, mainScreen, removeSlot):
        self.Form = MoveRemoveStorageSlotScreen
        self.MainScreen = mainScreen
        self.RemoveSlot = removeSlot

        MoveRemoveStorageSlotScreen.setObjectName("MoveRemoveStorageSlotScreen")
        MoveRemoveStorageSlotScreen.resize(802, 487)
        font = QtGui.QFont()
        font.setPointSize(14)
        MoveRemoveStorageSlotScreen.setFont(font)
        MoveRemoveStorageSlotScreen.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.centralwidget = QtWidgets.QWidget(MoveRemoveStorageSlotScreen)
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
        self.btn_manageStorageSlot = QtWidgets.QPushButton(self.centralwidget)
        self.btn_manageStorageSlot.setGeometry(QtCore.QRect(10, 360, 201, 51))
        self.btn_manageStorageSlot.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.btn_manageStorageSlot.setObjectName("btn_manageStorageSlot")
        self.btn_manageStorageSlot.setEnabled(False)
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
        MoveRemoveStorageSlotScreen.setCentralWidget(self.centralwidget)

        self.MoveSlotSelected = False
        self.retranslateUi(MoveRemoveStorageSlotScreen)
        self.btn_cancel.clicked.connect(self.btn_cancel_clicked)
        self.btn_search.clicked.connect(self.btn_search_clicked)
        self.btn_manageStorageSlot.clicked.connect(self.btn_manageStorageSlot_clicked)
        self.dtv_items.itemSelectionChanged.connect(self.item_selected)
        QtCore.QMetaObject.connectSlotsByName(MoveRemoveStorageSlotScreen)

    def retranslateUi(self, MoveRemoveStorageSlotScreen):
        _translate = QtCore.QCoreApplication.translate
        MoveRemoveStorageSlotScreen.setWindowTitle(_translate("MoveRemoveStorageSlotScreen", "MainWindow"))
        self.btn_search.setText(_translate("MoveRemoveStorageSlotScreen", "Search"))
        self.btn_cancel.setText(_translate("MoveRemoveStorageSlotScreen", "Cancel"))

        if (self.RemoveSlot):
            self.btnTitle = "Remove Slot"
        else:
            self.btnTitle = "Select Slot"

        self.btn_manageStorageSlot.setText(_translate("MoveRemoveStorageSlotScreen", self.btnTitle))
        self.lbl_itemData.setText(_translate("MoveRemoveStorageSlotScreen", "Stored Items:"))

        if (self.RemoveSlot):
            self.title = "Remove Slots"
        else:
            self.title = "Select Slot to move"

        self.lbl_screenTitle.setText(_translate("MoveRemoveStorageSlotScreen", self.title))

    def btn_cancel_clicked(self):
        if (not self.MoveSlotSelected):
            User.User.MainScreen.showFullScreen()
            self.MainScreen.dh.updateDataTable()
            self.Form.deleteLater()
        else:
            self.MoveSlotSelected = False
            self.updateScreen()

    def btn_search_clicked(self):
        self.setDataViewScreen(self.txb_search.text())

    def btn_manageStorageSlot_clicked(self):
        if (self.slotPosition > 0):
            if (self.RemoveSlot):
                msg = QMessageBox(self.Form)
                msg.setIcon(QMessageBox.Warning)
                if (SSUFunctions.startLED(int(self.slotPosition), User.User.Color, 2)):
                    msg = QMessageBox(self.Form)
                    msg.setIcon(QMessageBox.Warning) 
                    msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                    msg.setWindowTitle("Warning!")
                    msg.setText("Do you really want to remove the storage slot blicking <span style='color: #" + User.User.Color + "'>in this color</span>?")                               
                    buttonResult = msg.exec_()

                    if (buttonResult == QMessageBox.Yes):
                        msg.setIcon(QMessageBox.Information) 
                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.setWindowTitle("Information!")
                        msg.setText("Please remove all items and dividers from the storage slot blicking <span style='color: #" + User.User.Color + "'>in this color</span>!")
                        msg.exec_()
                        MySQLDatabase.execDML("DELETE FROM storagep WHERE storagehID=" + str(self.slotPosition))
                        MySQLDatabase.execDML("UPDATE storageh SET firstPartition=0, secondPartition=0, thirdPartition=0 WHERE ID=" + str(self.slotPosition))

                    SSUFunctions.stopLED(int(self.slotPosition))
                    self.setDataViewScreen("")
                else:
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.setWindowTitle("Warning!")
                    msg.setText("Can't be deleted, due there is a person working in this slot!")                               
                    msg.exec_()
            else:
                if (not self.MoveSlotSelected):
                    self.SlotToMove = self.slotPosition
                    self.MoveSlotSelected = True
                    self.updateScreen()
                else:
                    if(SSUFunctions.startLED(int(self.slotPosition), User.User.Color, 2)):
                        if (SSUFunctions.startLED(int(self.SlotToMove), User.User.Color, 2)):
                            msg = QMessageBox(self.Form)
                            msg.setIcon(QMessageBox.Warning) 
                            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                            msg.setWindowTitle("Warning!")
                            msg.setText("Do you really want to switch the storage slots blinking <span style='color: #" + User.User.Color + "'>in this color</span>?")                               
                            buttonResult = msg.exec_()

                            if (buttonResult == QMessageBox.Yes):
                                msg.setIcon(QMessageBox.Information) 
                                msg.setStandardButtons(QMessageBox.Ok)
                                msg.setWindowTitle("Information!")
                                msg.setText("Please switch the storage slots blinking <span style='color: #" + User.User.Color + "'>in this color</span>!")
                                msg.exec_()
                                storagePos1 = MySQLDatabase.execSelect("SELECT storagePosition FROM storageh WHERE ID=" + str(self.SlotToMove))[0][0]
                                storagePos2 = MySQLDatabase.execSelect("SELECT storagePosition FROM storageh WHERE ID=" + str(self.slotPosition))[0][0]           

                                MySQLDatabase.execDML("UPDATE storageh SET storagePosition=87263 WHERE ID=" + str(self.SlotToMove))
                                MySQLDatabase.execDML("UPDATE storageh SET storagePosition=" + str(storagePos1) + " WHERE ID=" + str(self.slotPosition))
                                MySQLDatabase.execDML("UPDATE storageh SET storagePosition=" + str(storagePos2) + " WHERE ID=" + str(self.SlotToMove))                          

                            SSUFunctions.stopLED(int(self.slotPosition))
                            SSUFunctions.stopLED(int(self.SlotToMove))
                            self.MoveSlotSelected = False
                            self.updateScreen()
                        else:
                            SSUFunctions.stopLED(int(self.slotPosition))
                            msg.setStandardButtons(QMessageBox.Ok)
                            msg.setWindowTitle("Warning!")
                            msg.setText("Can't be deleted, due there is a person working in this slot!")                               
                            msg.exec_()
                    else:
                        msg.setStandardButtons(QMessageBox.Ok)
                        msg.setWindowTitle("Warning!")
                        msg.setText("Can't be deleted, due there is a person working in this slot!")                               
                        msg.exec_()
        else:
            self.btn_manageStorageSlot.setEnabled(False)

    def onLoad_RemoveStorageSlotScreen(self):
        self.updateScreen()

    def updateScreen(self):
        if (self.MoveSlotSelected):
            self.lbl_screenTitle.setText("Select Target")
            self.btn_manageStorageSlot.setText("Move Slot")
            self.btn_cancel.setText("Back")
            self.setDataViewScreen("", True)
        else:
            self.lbl_screenTitle.setText(self.title)
            self.btn_manageStorageSlot.setText(self.btnTitle)
            self.btn_cancel.setText("Cancel")
            self.setDataViewScreen("")

    def item_selected(self):
         try:
            rowIndex = self.dtv_items.selectedItems()[0].row()
            self.slotPosition = self.__storageSlots[rowIndex][0]

            itemDataResult = MySQLDatabase.execSelect("SELECT cmpt.typeName, cmpt.typeVersion, itm.articleNumber " +
	                                                  "FROM componenttypes cmpt, items itm " +
	                                                  "WHERE cmpt.ID = itm.typeID AND " +
                                                      "itm.ID IN (SELECT sp.itemID FROM storagep sp WHERE sp.storagehID = " + str(self.slotPosition) + ")")
            self.liv_itemData.clear()
            i = 0
            for row in itemDataResult:
                self.liv_itemData.addItem(str(row[2]) + ": " + str(row[0]) + " - " + str(row[1]))

                itemState = self.liv_itemData.item(i)
                itemState.setFlags(itemState.flags() & ~Qt.ItemIsSelectable)
                i += 1

            self.btn_manageStorageSlot.setEnabled(True)
         except:
            self.slotPosition = 0
            print("Could not select a row!")
            self.btn_manageStorageSlot.setEnabled(False)

    def setDataViewScreen(self, searchString, showEmtpy=False):
        self.btn_manageStorageSlot.setEnabled(False)
        if (not self.MoveSlotSelected):
            self.__storageSlots = MySQLDatabase.execSelect("SELECT sh.ID, sh.storagePosition, sh.firstPartition, sh.secondPartition, sh.thirdPartition, SUM(sp.quantity) " +
	                                                       "FROM storageh sh, storagep sp " +
	                                                       "WHERE sp.storagehID=sh.ID AND " +
	                                                       "(sh.storagePosition LIKE '" + str(searchString) + "%' OR " +
	                                                       "sh.ID IN (SELECT DISTINCT temp.storagehID FROM storagep temp WHERE temp.itemID IN " +
	                                                       "(SELECT itm.ID FROM items itm WHERE itm.typeID IN " +
	                                                       "(SELECT cmpt.ID FROM componenttypes cmpt WHERE " +
	                                                       "typeName LIKE '" + str(searchString) + "%' OR typeVersion LIKE '" + str(searchString) + "%') OR " + 
                                                           "itm.articleNumber LIKE '" + str(searchString) + "%'))) " +
	                                                       "GROUP BY sp.storagehID " +
	                                                       "ORDER BY sh.storagePosition")
        else:
            self.__storageSlots = MySQLDatabase.execSelect("SELECT sh.ID, sh.storagePosition, sh.firstPartition, sh.secondPartition, sh.thirdPartition, " +
	                                                       "COALESCE((SELECT SUM(quantity) FROM storagep WHERE storagehID=sh.ID), 0) AS quantity " +
                                                           "FROM storageh sh, storagep sp " + 
                                                           "WHERE NOT sh.ID=" + str(self.SlotToMove) + " AND " +
                                                           "(sh.storagePosition LIKE '" + str(searchString) + "%' OR " +
                                                           "sh.ID IN (SELECT DISTINCT temp.storagehID FROM storagep temp WHERE temp.itemID IN " +
                                                           "(SELECT itm.ID FROM items itm WHERE itm.typeID IN " +
                                                           "(SELECT cmpt.ID FROM componenttypes cmpt WHERE " +
                                                           "typeName LIKE '" + str(searchString) + "%' OR typeVersion LIKE '" + str(searchString) + "%') OR " +
                                                           "itm.articleNumber LIKE '" + str(searchString) + "%'))) " +
                                                           "GROUP BY sh.ID " +
                                                           "ORDER BY COALESCE((SELECT SUM(quantity) FROM storagep WHERE storagehID=sh.ID), 0), sh.storagePosition")

        self.dtv_items.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.dtv_items.setSelectionMode(QAbstractItemView.SingleSelection)
        self.dtv_items.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.dtv_items.setColumnCount(5)
        self.dtv_items.setRowCount(0)

        self.dtv_items.setHorizontalHeaderLabels(("Slot Pos.", "Divider 1", "Divider 2", "Divider 3", "Quantity"))

        self.liv_itemData.clear()

        header = self.dtv_items.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)       
        for i in range(1, 5):
            header.setSectionResizeMode(i, QHeaderView.ResizeToContents)

        for row in self.__storageSlots:
            rowPosition = self.dtv_items.rowCount()    
            self.dtv_items.insertRow(rowPosition)

            for i in range(5):
                if ((i >= 1) and (i <= 3)):
                    if (int(row[i + 1]) > 0):
                        itemData = "Yes"
                    else:
                        itemData = "No"
                else:
                    itemData = str(row[i + 1])

                item = QTableWidgetItem(itemData)

                item.setTextAlignment(Qt.AlignCenter)

                self.dtv_items.setItem(rowPosition, i, item)

            vHeader = self.dtv_items.verticalHeader()
            vHeader.setSectionResizeMode(rowPosition, QHeaderView.Fixed)