from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import db_connector, User, DataHandler, SSUFunctions

MySQLDatabase = db_connector.Database(host = "localhost", user = "ssu_db", password = "ssu_FRS", database = "ssu")

class Ui_NewEditItemScreen(object):
    def setupUi(self, NewEditItemScreen, sis, itemScreenForm, itemID=0):
        self.Form = NewEditItemScreen
        self.StorageItemScreen = sis
        self.ItemScreenForm = itemScreenForm
        self.ItemID = itemID

        NewEditItemScreen.setObjectName("NewEditItemScreen")
        NewEditItemScreen.resize(800, 480)
        font = QtGui.QFont()
        font.setPointSize(14)
        NewEditItemScreen.setFont(font)
        NewEditItemScreen.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.centralwidget = QtWidgets.QWidget(NewEditItemScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancel.setGeometry(QtCore.QRect(10, 420, 181, 51))
        self.btn_cancel.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(610, 420, 181, 51))
        self.btn_save.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.btn_save.setObjectName("btn_save")
        self.lbl_item = QtWidgets.QLabel(self.centralwidget)
        self.lbl_item.setGeometry(QtCore.QRect(0, 10, 801, 31))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_item.setFont(font)
        self.lbl_item.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_item.setObjectName("lbl_item")
        self.lbl_articleNumber = QtWidgets.QLabel(self.centralwidget)
        self.lbl_articleNumber.setGeometry(QtCore.QRect(200, 50, 401, 31))
        self.lbl_articleNumber.setObjectName("lbl_articleNumber")        
        self.lbl_errorArticleNumber = QtWidgets.QLabel(self.centralwidget)
        self.lbl_errorArticleNumber.setGeometry(QtCore.QRect(200, 50, 401, 31))
        self.lbl_errorArticleNumber.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_errorArticleNumber.setObjectName("lbl_errorArticleNumber")
        self.lbl_errorArticleNumber.setVisible(False)
        self.cmb_itemType = QtWidgets.QComboBox(self.centralwidget)
        self.cmb_itemType.setGeometry(QtCore.QRect(200, 150, 191, 31))
        self.cmb_itemType.setObjectName("cmb_itemType")
        self.cmb_itemType.setEditable(True)
        self.lbl_itemType = QtWidgets.QLabel(self.centralwidget)
        self.lbl_itemType.setGeometry(QtCore.QRect(200, 120, 191, 31))
        self.lbl_itemType.setObjectName("lbl_itemType")
        self.cmb_itemVersion = QtWidgets.QComboBox(self.centralwidget)
        self.cmb_itemVersion.setGeometry(QtCore.QRect(410, 150, 191, 31))
        self.cmb_itemVersion.setObjectName("cmb_itemVersion")
        self.lbl_itemVersion = QtWidgets.QLabel(self.centralwidget)
        self.lbl_itemVersion.setGeometry(QtCore.QRect(410, 120, 191, 31))
        self.lbl_itemVersion.setObjectName("lbl_itemVersion")
        self.txb_articleNumber = QtWidgets.QLineEdit(self.centralwidget)        
        self.txb_articleNumber.setGeometry(QtCore.QRect(200, 80, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.txb_articleNumber.setFont(font)
        self.txb_articleNumber.setAlignment(QtCore.Qt.AlignCenter)
        self.txb_articleNumber.setObjectName("txb_articleNumber")
        self.txb_propertyValue = QtWidgets.QLineEdit(self.centralwidget)
        self.txb_propertyValue.setGeometry(QtCore.QRect(320, 220, 141, 31))
        self.txb_propertyValue.setText("")
        self.txb_propertyValue.setAlignment(QtCore.Qt.AlignCenter)
        self.txb_propertyValue.setObjectName("txb_propertyValue")
        self.cmb_reference = QtWidgets.QComboBox(self.centralwidget)
        self.cmb_reference.setGeometry(QtCore.QRect(120, 220, 191, 31))
        self.cmb_reference.setObjectName("cmb_reference")
        self.cmb_reference.setEditable(True)
        self.cmb_unit = QtWidgets.QComboBox(self.centralwidget)
        self.cmb_unit.setGeometry(QtCore.QRect(470, 220, 101, 31))
        self.cmb_unit.setObjectName("cmb_unit")
        self.cmb_unit.setEditable(True)
        self.btn_edit = QtWidgets.QPushButton(self.centralwidget)
        self.btn_edit.setGeometry(QtCore.QRect(580, 310, 101, 41))
        self.btn_edit.setObjectName("btn_edit")        
        self.btn_edit.setEnabled(False)
        self.dtv_itemData = QtWidgets.QTableWidget(self.centralwidget)
        self.dtv_itemData.setGeometry(QtCore.QRect(120, 260, 451, 141))
        self.dtv_itemData.setObjectName("dtv_itemData")
        self.dtv_itemData.setColumnCount(0)
        self.dtv_itemData.setRowCount(0)
        self.dtv_itemData.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.dtv_itemData.setSelectionMode(QAbstractItemView.SingleSelection)
        self.dtv_itemData.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.dtv_itemData.setColumnCount(3)
        self.dtv_itemData.setRowCount(0)
        self.dtv_itemData.setHorizontalHeaderLabels(("Reference", "Value", "Unit"))
        header = self.dtv_itemData.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)       
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)

        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(580, 360, 101, 41))
        self.btn_delete.setObjectName("btn_delete")
        self.btn_delete.setEnabled(False)
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(580, 260, 101, 41))
        self.btn_add.setObjectName("btn_add")
        self.lbl_itemData = QtWidgets.QLabel(self.centralwidget)
        self.lbl_itemData.setGeometry(QtCore.QRect(120, 190, 551, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_itemData.setFont(font)
        self.lbl_itemData.setObjectName("lbl_itemData")
        self.chb_alarmActivated = QtWidgets.QCheckBox(self.centralwidget)
        self.chb_alarmActivated.setGeometry(QtCore.QRect(300, 415, 221, 31))
        self.chb_alarmActivated.setAutoFillBackground(False)
        self.chb_alarmActivated.setObjectName("chb_alarmActivated")
        NewEditItemScreen.setCentralWidget(self.centralwidget)

        self.changeAlarmPossible = False
        result = MySQLDatabase.execSelect("SELECT * FROM  storagep WHERE itemID=" + str(self.ItemID))
        if (len(result) > 0):
            self.changeAlarmPossible = True

        self.chb_alarmActivated.setVisible(self.changeAlarmPossible)

        self.retranslateUi(NewEditItemScreen)
        self.dtv_itemData.itemSelectionChanged.connect(self.itemdata_selected)
        self.btn_add.clicked.connect(self.btn_add_clicked)
        self.btn_edit.clicked.connect(self.btn_edit_clicked)
        self.btn_delete.clicked.connect(self.btn_delete_clicked)
        self.btn_cancel.clicked.connect(self.btn_cancel_clicked)
        self.btn_save.clicked.connect(self.btn_save_clicked)
        self.cmb_itemType.currentTextChanged.connect(self.cmb_itemType_changed)
        QtCore.QMetaObject.connectSlotsByName(NewEditItemScreen)

        self.__editActive = False

    def retranslateUi(self, NewEditItemScreen):
        _translate = QtCore.QCoreApplication.translate
        NewEditItemScreen.setWindowTitle(_translate("NewEditItemScreen", "MainWindow"))
        self.btn_cancel.setText(_translate("NewEditItemScreen", "Cancel"))
        self.btn_save.setText(_translate("NewEditItemScreen", "Save"))

        if (self.ItemID > 0):
            addon = "Edit"
        else:
            addon = "New"

        self.lbl_item.setText(_translate("NewEditItemScreen", addon + " Item"))
        self.lbl_articleNumber.setText(_translate("NewEditItemScreen", "Article No.:"))
        self.lbl_errorArticleNumber.setText(_translate("NewEditItemScreen", "<html><head/><body><p><span style=\" color:#ff0000;\">Already in Database!</span></p></body></html>"))
        self.lbl_itemType.setText(_translate("NewEditItemScreen", "Item Type:"))
        self.lbl_itemVersion.setText(_translate("NewEditItemScreen", "Item Version:"))
        self.btn_edit.setText(_translate("NewEditItemScreen", "Edit"))
        self.btn_delete.setText(_translate("NewEditItemScreen", "Delete"))
        self.btn_add.setText(_translate("NewEditItemScreen", "Add"))
        self.lbl_itemData.setText(_translate("NewEditItemScreen", "Item Data:"))
        self.chb_alarmActivated.setText(_translate("NewEditItemScreen", "Activate item alarm"))

    def itemdata_selected(self):
        try:
            self.__rowIndex = self.dtv_itemData.selectedItems()[0].row()
            self.btn_delete.setEnabled(True)
            self.btn_edit.setEnabled(True)
        except:
            print("Could not select item data!")
            self.btn_delete.setEnabled(False)
            self.btn_edit.setEnabled(False)

    def btn_add_clicked(self):
        msg = QMessageBox(self.Form)
        msg.setIcon(QMessageBox.Critical) 
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setWindowTitle("ERROR!") 
        referenceName = self.cmb_reference.currentText()
        propertyValue = self.txb_propertyValue.text()
        unit = self.cmb_unit.currentText()        

        referenceNotUsed = True
        for i in range(self.dtv_itemData.rowCount()):
            if (self.dtv_itemData.item(i, 0).text() == referenceName):
                referenceNotUsed = False

        if (referenceNotUsed or self.__editActive):
            if (referenceName):
                if (propertyValue):
                    if (not self.__editActive):
                        rowPosition = self.dtv_itemData.rowCount()    
                        self.dtv_itemData.insertRow(rowPosition)

                        item0 = QTableWidgetItem(referenceName)
                        item1 = QTableWidgetItem(propertyValue)
                        item2 = QTableWidgetItem(unit)
                        item1.setTextAlignment(Qt.AlignCenter)
                        self.dtv_itemData.setItem(rowPosition, 0, item0)
                        self.dtv_itemData.setItem(rowPosition, 1, item1)
                        self.dtv_itemData.setItem(rowPosition, 2, item2)

                        vHeader = self.dtv_itemData.verticalHeader()
                        vHeader.setSectionResizeMode(rowPosition, QHeaderView.Fixed)

                        index = self.cmb_reference.findText(referenceName, Qt.MatchFixedString)
                        self.cmb_reference.removeItem(index)

                    else:
                        self.dtv_itemData.item(self.__editIndex, 0).setText(referenceName)
                        self.dtv_itemData.item(self.__editIndex, 1).setText(propertyValue)
                        self.dtv_itemData.item(self.__editIndex, 2).setText(unit)

                        self.__editActive = False
                        self.btn_add.setText("Add")
                        self.btn_delete.setText("Delete")
                        self.btn_edit.setEnabled(True)

                        try:
                            self.cmb_reference.setCurrentIndex(0)
                            self.txb_propertyValue.setText("")
                        except:
                            pass
                else:
                    msg.setText("Missing Value!")                               
                    msg.exec_()
            else:
                msg.setText("Missing Reference!")          
                msg.exec_()
        else:
            msg.setText("Referenece already used!")         
            msg.exec_()
    
    def btn_edit_clicked(self):
        self.__editActive = True
        self.__editIndex = self.__rowIndex
        self.btn_add.setText("Save")
        self.btn_delete.setText("Cancel")
        self.btn_edit.setEnabled(False)
        referenceName = self.dtv_itemData.item(self.__rowIndex, 0).text()
        propertyValue = self.dtv_itemData.item(self.__rowIndex, 1).text()
        unit = self.dtv_itemData.item(self.__rowIndex, 2).text()

        self.cmb_reference.setCurrentText(referenceName)
        self.txb_propertyValue.setText(propertyValue)
        self.cmb_unit.setCurrentText(unit)

    def btn_delete_clicked(self):
        if (not self.__editActive):
            msg = QMessageBox(self.Form)
            msg.setIcon(QMessageBox.Warning) 
            msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            msg.setText("Do you really want to delete this Item Data?")
            msg.setWindowTitle("Delete?!")            
            buttonResult = msg.exec_()

            if (buttonResult == QMessageBox.Yes):
                try:
                    item = self.dtv_itemData.item(self.__rowIndex, 0).text()
                    self.dtv_itemData.removeRow(self.__rowIndex)

                    referenceList = []
                    for row in self.__referenceName:
                        referenceList.append(str(row[0]))

                    if (item in referenceList):
                        self.cmb_reference.addItem(item)
                except:
                    print("Could not delete this item!")

        else:
            self.__editActive = False
            self.btn_add.setText("Add")
            self.btn_delete.setText("Delete")
            self.btn_edit.setEnabled(True)

            try:
                self.cmb_reference.setCurrentIndex(0)
                self.txb_propertyValue.setText("")
            except:
                pass

    def btn_cancel_clicked(self):
        self.StorageItemScreen.showFullScreen()
        self.ItemScreenForm.dh.updateDataTable()
        self.Form.deleteLater()

    def btn_save_clicked(self):
        msg = QMessageBox(self.Form)
        msg.setIcon(QMessageBox.Critical) 
        msg.setStandardButtons(QMessageBox.Ok)
        msg.setWindowTitle("ERROR!")
        articleNumber = self.txb_articleNumber.text()
        typeName = self.cmb_itemType.currentText()
        typeVersion = self.cmb_itemVersion.currentText()
        alarmActive = self.chb_alarmActivated.isChecked()

        if (self.articleNumberOK(articleNumber)):
            if ((not SSUFunctions.isStringEmptyOrSpace(typeVersion)) and (not SSUFunctions.isStringEmptyOrSpace(typeName))):
                self.lbl_errorArticleNumber.setVisible(False)
            
                if (self.newTypeNameOrVersion(typeName, typeVersion)):
                    MySQLDatabase.execDML("INSERT INTO componenttypes(typeName, typeVersion) VALUES('" + typeName + "', '" + typeVersion + "')")

                itemDataList = []
                for index in range(self.dtv_itemData.rowCount()):
                    itemDataList.append((self.dtv_itemData.item(index, 0).text(), self.dtv_itemData.item(index, 1).text(), self.dtv_itemData.item(index, 2).text()))

                for row in itemDataList:
                    referenceName = str(row[0])
                    if (self.newReferenceName(referenceName)):
                        MySQLDatabase.execDML("INSERT INTO referencenames(name) VALUES('" + referenceName + "')")

                if (self.changeAlarmPossible and (self.ItemID > 0)):
                    if (alarmActive):
                        alarmAddon = "1"
                    else:
                        alarmAddon = "0"

                    MySQLDatabase.execDML("UPDATE storagep SET alarmActivated=" + alarmAddon + " WHERE itemID=" + str(self.ItemID))

                if (self.ItemID <= 0):
                    MySQLDatabase.execDML("INSERT INTO items(typeID, articleNumber, weight) " + 
                                          "VALUES((SELECT ID FROM componenttypes WHERE typeName='" + typeName + "' AND typeVersion='" + typeVersion + "'), '" + articleNumber + "', 0.0)")
                    itemID = str(MySQLDatabase.execSelect("SELECT ID FROM items WHERE articleNumber='" + articleNumber + "'")[0][0])

                    for row in itemDataList:
                        referenceName = str(row[0])
                        propertyValue = str(row[1])
                        unit = str(row[2])
                        MySQLDatabase.execDML("INSERT INTO itemdata(itemID, referenceID, propertyValue, unit) " + 
                                              "VALUES(" + itemID + ", " +
                                              "(SELECT ID FROM referencenames WHERE name='" + referenceName + "'), " +
                                              "'" + propertyValue + "', '" + unit + "')")
                else:
                     MySQLDatabase.execDML("UPDATE items SET " + 
                                           "typeID=(SELECT ID FROM componenttypes WHERE typeName='" + typeName + "' AND typeVersion='" + typeVersion + "'), " + 
                                           "articleNumber='" + articleNumber + "' " +
                                           "WHERE ID=" + str(self.ItemID))

                     MySQLDatabase.execDML("DELETE FROM itemdata WHERE itemID=" + str(self.ItemID))
                     for row in itemDataList:
                        referenceName = str(row[0])
                        propertyValue = str(row[1])
                        unit = str(row[2])
                        MySQLDatabase.execDML("INSERT INTO itemdata(itemID, referenceID, propertyValue, unit) " + 
                                              "VALUES(" + str(self.ItemID) + ", " +
                                              "(SELECT ID FROM referencenames WHERE name='" + referenceName + "'), " +
                                              "'" + propertyValue + "', '" + unit + "')")

                self.StorageItemScreen.showFullScreen()
                self.ItemScreenForm.dh.updateDataTable()
                self.Form.deleteLater()
            else:
                msg.setText("Item Type and Item Version can't be blank!")                               
                msg.exec_()
        else:
            self.lbl_errorArticleNumber.setVisible(True)

    def articleNumberOK(self, articleNumber):
        if (self.ItemID > 0):
            itemAddon = " AND NOT ID=" + str(self.ItemID)
        else:
            itemAddon = ""

        result = MySQLDatabase.execSelect("SELECT * FROM items WHERE articleNumber='" + articleNumber + "'" + itemAddon)

        if (len(result) > 0):
            return False
        else:
            return True

    def newTypeNameOrVersion(self, typeName, typeVersion):
        result = MySQLDatabase.execSelect("SELECT * FROM componenttypes WHERE typeName='" + typeName + "' AND typeVersion='" + typeVersion + "'")

        if (len(result) > 0):
            return False
        else:
            return True

    def newReferenceName(self, name):
        result = MySQLDatabase.execSelect("SELECT * FROM referencenames WHERE name='" + name + "'")

        if (len(result) > 0):
            return False
        else:
            return True

    def onLoad_NewEditItemScreen(self):
        self.updateAll()

    def cmb_itemType_changed(self):
        try:
            typeInDatabase = False
            itemTypeText = self.cmb_itemType.currentText()
            for row in self.__ItemType:
                if (itemTypeText in row):
                    typeInDatabase = True
                    break

            self.cmb_itemVersion.clear()
            if (typeInDatabase):        
                self.cmb_itemVersion.setEditable(True)
                typeVersion = MySQLDatabase.execSelect("SELECT DISTINCT typeVersion FROM componenttypes WHERE typeName='" + itemTypeText + "'")
                for row in typeVersion:
                    self.cmb_itemVersion.addItem(str(row[0]))
            else:
                self.cmb_itemVersion.setEditable(True)
                self.cmb_itemVersion.addItem("default")
        except:
            print("Could not select item!")


    # comboboxes

    def updateAll(self):
        self.updateUnits()
        self.updateReferenceNames()
        self.updateItemType()

        if (self.ItemID > 0):
            self.setItemData()

    def updateUnits(self):
        self.getUnits()
        self.setUnits()

    def getUnits(self):
        self.__units = MySQLDatabase.execSelect("SELECT DISTINCT unit FROM itemdata")

    def setUnits(self):
        self.cmb_unit.clear()
        for row in self.__units:
            self.cmb_unit.addItem(str(row[0]))

    def updateReferenceNames(self):
        self.getReferenceNames()
        self.setReferenceNames()

    def getReferenceNames(self):
        self.__referenceName = MySQLDatabase.execSelect("SELECT name FROM referencenames")

    def setReferenceNames(self):
        self.cmb_reference.clear()
        for row in self.__referenceName:
            self.cmb_reference.addItem(str(row[0]))

    def updateItemType(self):
        self.getItemType()
        self.setItemType()

    def getItemType(self):
        self.__ItemType = MySQLDatabase.execSelect("SELECT ID, typeName FROM (SELECT ID, typeName, Row_number() OVER(PARTITION BY typeName ORDER BY ID) rn FROM componenttypes) t WHERE rn = 1")

    def setItemType(self):
        self.cmb_itemType.clear()
        for row in self.__ItemType:
            self.cmb_itemType.addItem(str(row[1]))

    def setItemData(self):
        articleNumber = MySQLDatabase.execSelect("SELECT articleNumber FROM items WHERE ID=" + str(self.ItemID))[0][0]
        self.txb_articleNumber.setText(str(articleNumber))

        itemType = MySQLDatabase.execSelect("SELECT typeName, typeVersion FROM componenttypes WHERE ID=(SELECT typeID FROM items WHERE ID=" + str(self.ItemID) + ")")[0]
        self.cmb_itemType.setCurrentText(str(itemType[0]))
        self.cmb_itemVersion.setCurrentText(str(itemType[1]))

        itemData = MySQLDatabase.execSelect("SELECT ref.name, itd.propertyValue, itd.unit FROM itemdata itd, referencenames ref " + 
                                            "WHERE itd.referenceID=ref.ID AND itd.itemID=" + str(self.ItemID))

        if (self.changeAlarmPossible):
            alarmActive = bool(MySQLDatabase.execSelect("SELECT alarmActivated FROM storagep WHERE itemID=" + str(self.ItemID))[0][0])
            self.chb_alarmActivated.setChecked(alarmActive)


        for row in itemData:
            try:
                self.cmb_reference.setCurrentText(str(row[0]))
                self.txb_propertyValue.setText(str(row[1]))
                self.cmb_unit.setCurrentText(str(row[2]))
                self.btn_add_clicked()
            except:
                pass

        try:
            self.cmb_reference.setCurrentIndex(0)
            self.txb_propertyValue.setText("")
            self.cmb_unit.setCurrentIndex(0)
        except:
            pass