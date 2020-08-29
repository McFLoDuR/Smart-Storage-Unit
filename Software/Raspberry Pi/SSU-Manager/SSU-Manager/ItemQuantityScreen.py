from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
import ShowStorageSlotScreen, SelectStorageSlotScreen, MeasureItemScreen
import User, db_connector, SSUFunctions

MySQLDatabase = db_connector.Database(host = "localhost", user = "ssu_db", password = "ssu_FRS", database = "ssu")

class Ui_ItemScreen(object):
    def setupUi(self, ItemQuantityScreen, parentScreen, parentScreenForm, itemID, withdraw):
        self.Form = ItemQuantityScreen
        self.ParentScreen = parentScreen
        self.ParentScreenForm = parentScreenForm
        self.ItemID = itemID
        self.WithdrawItem = withdraw

        ItemQuantityScreen.setObjectName("ItemQuantityScreen")
        ItemQuantityScreen.resize(800, 480)
        font = QtGui.QFont()
        font.setPointSize(14)
        ItemQuantityScreen.setFont(font)
        ItemQuantityScreen.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.centralwidget = QtWidgets.QWidget(ItemQuantityScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancel.setGeometry(QtCore.QRect(10, 420, 181, 51))
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_withdraw = QtWidgets.QPushButton(self.centralwidget)
        self.btn_withdraw.setGeometry(QtCore.QRect(610, 420, 181, 51))
        self.btn_withdraw.setObjectName("btn_withdraw")
        self.nud_quantity = QtWidgets.QSpinBox(self.centralwidget)
        self.nud_quantity.setGeometry(QtCore.QRect(240, 300, 321, 81))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.nud_quantity.setFont(font)
        self.nud_quantity.setAlignment(QtCore.Qt.AlignCenter)
        self.nud_quantity.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)       
        self.nud_quantity.setStyleSheet("QSpinBox::up-button { width: 50px; } " + 
                                        "QSpinBox::down-button { width: 50px; }")
        self.nud_quantity.setObjectName("nud_quantity")
        self.lbl_component = QtWidgets.QLabel(self.centralwidget)
        self.lbl_component.setGeometry(QtCore.QRect(0, 0, 801, 51))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_component.setFont(font)
        self.lbl_component.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_component.setObjectName("lbl_component")
        self.lbl_type = QtWidgets.QLabel(self.centralwidget)
        self.lbl_type.setGeometry(QtCore.QRect(0, 40, 801, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lbl_type.setFont(font)
        self.lbl_type.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_type.setObjectName("lbl_type")
        self.lbl_instruction = QtWidgets.QLabel(self.centralwidget)
        self.lbl_instruction.setGeometry(QtCore.QRect(240, 380, 321, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbl_instruction.setFont(font)
        self.lbl_instruction.setWordWrap(True)
        self.lbl_instruction.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_instruction.setObjectName("lbl_instruction")
        self.lbl_articleNumber = QtWidgets.QLabel(self.centralwidget)
        self.lbl_articleNumber.setGeometry(QtCore.QRect(0, 80, 801, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lbl_articleNumber.setFont(font)
        self.lbl_articleNumber.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_articleNumber.setObjectName("lbl_articleNumber")
        self.liv_itemdata = QtWidgets.QListWidget(self.centralwidget)
        self.liv_itemdata.setGeometry(QtCore.QRect(240, 160, 321, 131))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.liv_itemdata.setFont(font)
        self.liv_itemdata.setObjectName("liv_itemdata")
        self.lbl_itemdata = QtWidgets.QLabel(self.centralwidget)
        self.lbl_itemdata.setGeometry(QtCore.QRect(250, 130, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lbl_itemdata.setFont(font)
        self.lbl_itemdata.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_itemdata.setObjectName("lbl_itemdata")
        ItemQuantityScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(ItemQuantityScreen)
        self.btn_cancel.clicked.connect(self.btn_cancel_clicked)
        self.btn_withdraw.clicked.connect(self.btn_withdraw_clicked)
        QtCore.QMetaObject.connectSlotsByName(ItemQuantityScreen)

    def retranslateUi(self, ItemQuantityScreen):
        _translate = QtCore.QCoreApplication.translate
        ItemQuantityScreen.setWindowTitle(_translate("ItemQuantityScreen", "MainWindow"))
        self.btn_cancel.setText(_translate("ItemQuantityScreen", "Cancel"))

        if(self.WithdrawItem):
            addon = "Withdraw"
            addon1 = "withdraw"
        else:
            addon = "Next"
            addon1 = "store"

        self.btn_withdraw.setText(_translate("ItemQuantityScreen", addon))
        self.lbl_instruction.setText(_translate("ItemQuantityScreen", "Please set the quantity you would like to " + addon1 + "!"))

        self.lbl_component.setText(_translate("ItemQuantityScreen", "Component: "))
        self.lbl_type.setText(_translate("ItemQuantityScreen", "Type: "))
        self.lbl_articleNumber.setText(_translate("ItemQuantityScreen", "Article Number: "))
        self.lbl_itemdata.setText(_translate("ItemQuantityScreen", "Item data:"))

    def btn_withdraw_clicked(self):
        if (self.WithdrawItem):
            self.buildItemList()
            self.ssss = QtWidgets.QMainWindow()
            self.ui = ShowStorageSlotScreen.Ui_ShowStorageSlotScreen()
            self.ui.setupUi(self.ssss, self.ParentScreen, self.ParentScreenForm, self.__storageList, 1)
            self.ssss.showFullScreen()
            t = QtCore.QTimer(self.Form)
            t.singleShot(0, self.ui.onLoad_ShowStorageSlotScreen)
            self.Form.deleteLater()
        else:
            result = MySQLDatabase.execSelect("SELECT storagePosition FROM storageh " + 
                                              "WHERE ID IN (SELECT storagehID FROM storagep " +
                                              "WHERE (quantityMax >= (quantity + " + str(self.nud_quantity.value()) + ")) " +
                                              "AND itemID=" + str(self.ItemID) + ")")

            itemWeight = float(MySQLDatabase.execSelect("SELECT weight FROM items WHERE ID=" + str(self.ItemID))[0][0])
            microScaleUsage = SSUFunctions.getMicroScaleUser()
            StoreInformation = [int(self.nud_quantity.value())]
            StoreInformation.append(len(result) > 0)
            goOn = True

            if((abs(0.0 - itemWeight) < 0.00001) and (StoreInformation[0] >= 20) and ((microScaleUsage == User.User.Id) or (microScaleUsage == 0))):
                msg = QMessageBox(self.Form)
                msg.setIcon(QMessageBox.Question) 
                msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
                msg.setText("Do you want to measure the weight of the item?")
                msg.setWindowTitle("Measure weight?")            
                buttonResult = msg.exec_()
                
                if (buttonResult == QMessageBox.Yes):
                    goOn = False
                    self.mis = QtWidgets.QMainWindow()
                    self.ui = MeasureItemScreen.Ui_MeasureItemScreen()
                    self.ui.setupUi(self.mis, self.ParentScreen, self.ParentScreenForm, self.ItemID, StoreInformation)
                    self.mis.showFullScreen()
                    t = QtCore.QTimer(self.Form)
                    t.singleShot(0, self.ui.onLoad_MeasureItemScreen)
                    self.Form.deleteLater()                    

            if (goOn):  
                if (StoreInformation[1]):             
                    result = MySQLDatabase.execSelect("SELECT sp.ID, sh.storagePosition, sh.firstPartition, sh.secondPartition, sh.thirdPartition, sp.insidePosition, sp.quantity " +
	                                                  "FROM storagep sp, storageh sh " +
	                                                  "WHERE sh.ID=(SELECT storagehID FROM storagep " +
	                                                  "WHERE (quantityMax >= (quantity + " + str(self.nud_quantity.value()) + ")) AND itemID=" + str(self.ItemID) + " "
	                                                  "ORDER BY quantity ASC LIMIT 1) AND " +
	                                                  "sp.storagehID = sh.ID AND itemID=" + str(self.ItemID))[0]
                    storageList = []
                    storageList.append((int(result[0]), int(result[1]), int(result[5]), int(result[2]), int(result[3]), int(result[4]), int(result[6])))
                    self.ssss = QtWidgets.QMainWindow()
                    self.ui = ShowStorageSlotScreen.Ui_ShowStorageSlotScreen()
                    self.ui.setupUi(self.ssss, self.ParentScreen, self.ParentScreenForm, storageList, 0, StoreInformation)
                    self.ssss.showFullScreen()               
                    t = QtCore.QTimer(self.Form)
                    t.singleShot(0, self.ui.onLoad_ShowStorageSlotScreen)
                    self.Form.deleteLater()
                else:
                    self.ssss = QtWidgets.QMainWindow()
                    self.ui = SelectStorageSlotScreen.Ui_SelectStorageSlotScreen()
                    self.ui.setupUi(self.ssss, self.ParentScreen, self.ParentScreenForm, self.ItemID, StoreInformation)
                    self.ssss.showFullScreen()               
                    t = QtCore.QTimer(self.Form)
                    t.singleShot(0, self.ui.onLoad_SelectStorageSlotScreen)
                    self.Form.deleteLater()


    def buildItemList(self):
        requiredQuantity = int(self.nud_quantity.value())
        result = MySQLDatabase.execSelect("SELECT sp.ID, sh.storagePosition, sh.firstPartition, sh.secondPartition, sh.thirdPartition, sp.insidePosition, sp.quantity " +
	                                      "FROM storagep sp, storageh sh " +
	                                      "WHERE sp.itemID=" + str(self.ItemID) + " AND sp.storagehID = sh.ID AND NOT sp.quantity = 0 " + 
	                                      "ORDER BY sp.quantity ASC")

        self.__storageList = []
        for i, row in enumerate(result):
            requiredQuantity -= int(row[6])
            
            if (requiredQuantity <= 0):
                if ((i + 1) == len(result) and (requiredQuantity == 0)):
                    remainingQuantity = 0
                else:
                    remainingQuantity = (int(row[6]) - abs(requiredQuantity))


                if (remainingQuantity == 0):
                    self.__storageList.append((int(row[0]), int(row[1]), int(row[5]), int(row[2]), int(row[3]), int(row[4]), 0))
                elif (remainingQuantity > 0):
                    self.__storageList.append((int(row[0]), int(row[1]), int(row[5]), int(row[2]), int(row[3]), int(row[4]), remainingQuantity))

                break
            else:
                # append = StorageP.ID, StorageSlot, insidePosition, firstPartition, secondPartition, thirdPartition, quantity to pick (0 = all)
                self.__storageList.append((int(row[0]), int(row[1]), int(row[5]), int(row[2]), int(row[3]), int(row[4]), 0))

    def btn_cancel_clicked(self):
        self.ParentScreenForm.showFullScreen()
        self.ParentScreen.dh.updateDataTable()
        self.Form.deleteLater()

    def onLoad_ItemQuantityScreen(self):
        result = MySQLDatabase.execSelect("SELECT rfn.name, itd.propertyValue, itd.unit FROM itemdata itd, referencenames rfn WHERE " +
                                          "itd.referenceID = rfn.ID AND itd.itemID = " + str(self.ItemID))

        i = 0
        for row in result:
            if (row[2] == "none"):
                unit = ""
            else:
                unit = (" " + str(row[2]))

            self.liv_itemdata.addItem(str(row[0]) + " = " + str(row[1]) + unit)
            itemState = self.liv_itemdata.item(i)
            itemState.setFlags(itemState.flags() & ~Qt.ItemIsSelectable)
            i += 1

        if (self.WithdrawItem):
            maxQuantity = int(MySQLDatabase.execSelect("SELECT SUM(quantity) FROM storagep WHERE itemID=" + str(self.ItemID))[0][0])

        mainInformation = MySQLDatabase.execSelect("SELECT cmpt.typeName, cmpt.typeVersion, itm.articleNumber FROM items itm, componenttypes cmpt WHERE itm.typeID = cmpt.ID AND itm.ID=" + str(self.ItemID))[0]

        self.lbl_component.setText("Component: " + str(mainInformation[0]))
        self.lbl_type.setText("Type: " + str(mainInformation[1]))
        self.lbl_articleNumber.setText("Article Number: " + str(mainInformation[2]))

        self.nud_quantity.setMinimum(1)
        if (self.WithdrawItem):
            self.nud_quantity.setMaximum(maxQuantity)
        else:
            self.nud_quantity.setMaximum(10000)
        self.nud_quantity.setValue(1)