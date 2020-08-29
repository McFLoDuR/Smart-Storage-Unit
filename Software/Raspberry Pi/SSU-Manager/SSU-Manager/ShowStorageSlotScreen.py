from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
import User, db_connector, SSUFunctions

MySQLDatabase = db_connector.Database(host = "localhost", user = "ssu_db", password = "ssu_FRS", database = "ssu")

class Ui_ShowStorageSlotScreen(object):
    ViewPosition1 = 20
    ViewPosition2 = 146
    ViewPosition3 = 155
    ViewPosition4 = 225
    ViewPosition5 = 232
    ViewPosition6 = 300
    ViewPosition7 = 307
    ViewPosition8 = 428
    
    # mode = 0 -> store
    # mode = 1  ->  withdraw
    # mode = 2  ->  set quantity
    def setupUi(self, ShowStorageSlotScreen, parent, parentForm, storageList, mode, storeInformation=[]):
        self.Form = ShowStorageSlotScreen
        self.ParentScreen = parent
        self.ParentForm = parentForm
        self.StorageList = storageList
        self.StorageListPointer = 0
        self.StorageListPointerMax = len(self.StorageList)
        self.DisplayMode = mode
        self.StoreInformation = storeInformation
        
        ShowStorageSlotScreen.setObjectName("ShowStorageSlotScreen")
        ShowStorageSlotScreen.resize(800, 480)
        font = QtGui.QFont()
        font.setPointSize(14)
        ShowStorageSlotScreen.setFont(font)
        ShowStorageSlotScreen.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.centralwidget = QtWidgets.QWidget(ShowStorageSlotScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_next = QtWidgets.QPushButton(self.centralwidget)
        self.btn_next.setGeometry(QtCore.QRect(610, 420, 181, 51))
        self.btn_next.setObjectName("btn_next")
        self.pnl_color = QtWidgets.QFrame(self.centralwidget)
        self.pnl_color.setGeometry(QtCore.QRect(40, 300, 131, 81))
        self.pnl_color.setAutoFillBackground(False)
        self.pnl_color.setStyleSheet("background-color: #" + User.User.Color)
        self.pnl_color.setFrameShape(QtWidgets.QFrame.Panel)
        self.pnl_color.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pnl_color.setObjectName("pnl_color")
        self.pgb_storageSlotView = QtWidgets.QLabel(self.centralwidget)
        self.pgb_storageSlotView.setGeometry(QtCore.QRect(320, 10, 161, 461))
        self.pgb_storageSlotView.setText("")
        self.pgb_storageSlotView.setPixmap(QtGui.QPixmap("images/storageSlot000.png"))
        self.pgb_storageSlotView.setScaledContents(True)
        self.pgb_storageSlotView.setObjectName("pgb_storageSlotView")
        self.lbl_itemCounter = QtWidgets.QLabel(self.centralwidget)
        self.lbl_itemCounter.setGeometry(QtCore.QRect(480, 40, 311, 371))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_itemCounter.setFont(font)
        self.lbl_itemCounter.setTextFormat(QtCore.Qt.RichText)
        self.lbl_itemCounter.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_itemCounter.setWordWrap(True)
        self.lbl_itemCounter.setObjectName("lbl_itemCounter")
        self.nud_quantity = QtWidgets.QSpinBox(self.centralwidget)
        self.nud_quantity.setGeometry(QtCore.QRect(510, 270, 251, 71))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.nud_quantity.setFont(font)
        self.nud_quantity.setAlignment(QtCore.Qt.AlignCenter)
        self.nud_quantity.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)       
        self.nud_quantity.setStyleSheet("QSpinBox::up-button { width: 40px; } " + 
                                        "QSpinBox::down-button { width: 40px; }")
        self.nud_quantity.setObjectName("nud_quantity")
        if (self.DisplayMode != 2):
            self.nud_quantity.setVisible(False)
        self.pnl_positionView = QtWidgets.QFrame(self.centralwidget)
        self.pnl_positionView.setGeometry(QtCore.QRect(330, 20, 141, 411))
        self.pnl_positionView.setAutoFillBackground(False)
        self.pnl_positionView.setStyleSheet("background-color: rgb(119, 255, 46)")
        self.pnl_positionView.setFrameShape(QtWidgets.QFrame.Panel)
        self.pnl_positionView.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pnl_positionView.setObjectName("pnl_positionView")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(10, 420, 181, 51))
        self.btn_back.setObjectName("btn_back")
        self.lbl_intruction = QtWidgets.QLabel(self.centralwidget)
        self.lbl_intruction.setGeometry(QtCore.QRect(40, 20, 271, 371))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lbl_intruction.setFont(font)
        self.lbl_intruction.setTextFormat(QtCore.Qt.RichText)
        self.lbl_intruction.setWordWrap(True)
        self.lbl_intruction.setObjectName("lbl_intruction")
        self.btn_useMicroScale = QtWidgets.QPushButton(self.centralwidget)
        self.btn_useMicroScale.setGeometry(QtCore.QRect(510, 290, 251, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btn_useMicroScale.setFont(font)
        self.btn_useMicroScale.setObjectName("btn_useMicroScale")
        self.lbl_errorPreviousInUse = QtWidgets.QLabel(self.centralwidget)
        self.lbl_errorPreviousInUse.setGeometry(QtCore.QRect(10, 389, 301, 31))
        self.lbl_errorPreviousInUse.setObjectName("lbl_errorPreviousInUse")
        self.lbl_errorPreviousInUse.setVisible(False)
        self.lbl_errorNextInUse = QtWidgets.QLabel(self.centralwidget)
        self.lbl_errorNextInUse.setGeometry(QtCore.QRect(490, 390, 301, 31))
        self.lbl_errorNextInUse.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_errorNextInUse.setObjectName("lbl_errorNextInUse")
        self.lbl_errorNextInUse.setVisible(False)

        self.tmr_screenUpdater = QTimer(self.Form)
        self.tmr_screenUpdater.timeout.connect(self.screenUpdater) 

        self.LEDon = False
        self.FirstTimeOn = True
        self.MicroScaleOn = False
        ShowStorageSlotScreen.setCentralWidget(self.centralwidget)
        self.btn_useMicroScale.clicked.connect(self.btn_useMicroScale_clicked)
        self.btn_back.clicked.connect(self.btn_back_clicked)
        self.btn_next.clicked.connect(self.btn_next_clicked)
        self.retranslateUi(ShowStorageSlotScreen)
        QtCore.QMetaObject.connectSlotsByName(ShowStorageSlotScreen)

    def retranslateUi(self, ShowStorageSlotScreen):
        _translate = QtCore.QCoreApplication.translate
        ShowStorageSlotScreen.setWindowTitle(_translate("ShowStorageSlotScreen", "MainWindow"))
        self.btn_next.setText(_translate("ShowStorageSlotScreen", "Next"))
        self.lbl_itemCounter.setText(_translate("ShowStorageSlotScreen", "{mirco scale result}"))
        self.btn_back.setText(_translate("ShowStorageSlotScreen", "Cancel"))
        self.lbl_intruction.setText(_translate("ShowStorageSlotScreen", "<html><head/><body><p>Please: {instruction}</p></body></html>"))
        self.btn_useMicroScale.setText(_translate("ShowStorageSlotScreen", "Use Micro Scale"))
        self.lbl_errorPreviousInUse.setText(_translate("ShowStorageSlotScreen", "<span style=\"color: red\">Previous Slot in Use!"))
        self.lbl_errorNextInUse.setText(_translate("ShowStorageSlotScreen", "<html><head/><body><p><span style=\" color:#ff0000;\">Next Slot in Use!</span></p></body></html>"))

    def btn_back_clicked(self):
        if (self.stopMicroScale()):
            if (self.StorageListPointer == 0):
                self.closeForm()
            else:
                self.turnLEDoff()
                self.StorageListPointer -= 1
                self.turnLEDon()
                self.updateButtonNames()
                self.screenUpdater()

    def closeForm(self):
        if (self.stopMicroScale()):
            self.tmr_screenUpdater.deleteLater()
            self.ParentForm.showFullScreen()

            if (self.DisplayMode == 1):
                self.ParentScreen.dh.updateDataTable(False)
            elif ((self.DisplayMode == 2) or (self.DisplayMode == 0)):
                self.ParentScreen.dh.updateDataTable()

            if (self.LEDon):
                self.turnLEDoff()
            self.Form.deleteLater()

    def btn_next_clicked(self):
        if (self.stopMicroScale()):
            if ((self.StorageListPointer + 1) == self.StorageListPointerMax):
                self.turnLEDoff()
                if (self.DisplayMode == 0):
                    self.saveStore()
                elif (self.DisplayMode == 1):
                    self.saveWithdraw()
                elif (self.DisplayMode == 2):
                    self.StorageList[self.StorageListPointer][6] = int(self.nud_quantity.value())
                    self.saveSetQuantity()
                
            else:
                self.turnLEDoff()
                if (self.DisplayMode == 2):
                    self.StorageList[self.StorageListPointer][6] = int(self.nud_quantity.value())
                self.StorageListPointer += 1
                self.turnLEDon()
                if (self.DisplayMode == 2):
                    self.updateNUD()
                self.updateButtonNames()
                self.screenUpdater()
                quantity = int(self.StorageList[self.StorageListPointer][6])
                if ((quantity >= 20) and (self.DisplayMode != 2)):
                    itemID = int(MySQLDatabase.execSelect("SELECT itemID FROM storagep WHERE ID=" + str(self.StorageList[self.StorageListPointer][0]))[0][0])
                    result = SSUFunctions.isItemForMicroScaleOK(itemID, quantity)
                    msg = QMessageBox(self.Form)
                    msg.setIcon(QMessageBox.Warning) 
                    msg.setStandardButtons(QMessageBox.Ok)
                    msg.setWindowTitle("ERROR!")
                    if (result == 0):
                        msg.setText("Too many items to use micro scale!")                               
                        msg.exec_()
                    elif (result == 1):
                        msg.setText("No weight for this item!")                               
                        msg.exec_()

    def btn_useMicroScale_clicked(self):
        if (not self.MicroScaleOn):
            self.startMicroScale()
        else:
            self.stopMicroScale()

        self.screenUpdater()

    def saveStore(self):
        MySQLDatabase.execDML("UPDATE storagep SET quantity=(quantity + " + str(self.StoreInformation[0]) + ") WHERE ID=" + str(self.StorageList[0][0]))
        self.closeForm()

    def saveWithdraw(self):
        for i, row in enumerate(self.StorageList):
            if((int(row[6]) == 0) and ((i + 1) != len(self.StorageList))):
                MySQLDatabase.execDML("DELETE FROM storagep WHERE ID=" + str(row[0]))
            elif (int(row[6]) == 0):
                MySQLDatabase.execDML("UPDATE storagep SET quantity=0 WHERE ID=" + str(row[0]))
            else:
                quantity = int(MySQLDatabase.execSelect("SELECT quantity FROM storagep WHERE ID=" + str(row[0]))[0][0])
                quantity = (quantity - int(row[6]))
                if (quantity < 0):
                   quantity = 0                

                MySQLDatabase.execDML("UPDATE storagep SET quantity=" + str(quantity) + " WHERE ID=" + str(row[0]))

        self.closeForm()

    def saveSetQuantity(self):
        for i, row in enumerate(self.StorageList):
            if((int(row[6]) == 0) and ((i + 1) != len(self.StorageList))):
                MySQLDatabase.execDML("DELETE FROM storagep WHERE ID=" + str(row[0]))
            else:
                MySQLDatabase.execDML("UPDATE storagep SET quantity=" + str(row[6]) + " WHERE ID=" + str(row[0]))

        self.closeForm()

    def tmr_microScale_timeout(self):
        currentItemWeight = SSUFunctions.getMicroScaleResult()
        currentQuantity = round(currentItemWeight / self.itemWeight)
        quantity = int(self.StorageList[self.StorageListPointer][6])
        self.lbl_itemCounter.setText(str(currentQuantity) + " / " + str(quantity) + "<br> {:2.3f} g".format(currentItemWeight))

    def startMicroScale(self):
        self.MicroScaleOn = True
        self.btn_useMicroScale.setText("Cancel Micro Scale")
        itemID = int(MySQLDatabase.execSelect("SELECT itemID FROM storagep WHERE ID=" + str(self.StorageList[self.StorageListPointer][0]))[0][0])
        self.itemWeight = float(MySQLDatabase.execSelect("SELECT weight FROM items WHERE ID=" + str(itemID))[0][0])
        SSUFunctions.startMicroScale()
        self.tmr_microScale_timeout()
        self.tmr_microScale = QTimer(self.Form)
        self.tmr_microScale.timeout.connect(self.tmr_microScale_timeout)
        self.tmr_microScale.start(1000)

    def stopMicroScale(self):
        if (self.MicroScaleOn):
            if (SSUFunctions.isMicroScaleEmpty()):
                self.tmr_microScale.stop()
                self.tmr_microScale.deleteLater()
                SSUFunctions.stopMicroScale()
                self.MicroScaleOn = False
                self.btn_useMicroScale.setText("Use Micro Scale")   
                return True
            else:
                msg = QMessageBox(self.Form)
                msg.setIcon(QMessageBox.Warning) 
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setWindowTitle("ERROR!")
                msg.setText("Please clear the micro scale before retraction!")                               
                msg.exec_()
                return False
        else:
            return True

    def screenUpdater(self):
        self.updateButtons()
        self.updateMarkedArea()
        self.updateSlotPicture()
        self.updateTexts()

    def updateNUD(self):
        result = MySQLDatabase.execSelect("SELECT quantityMax, quantity FROM storagep WHERE ID=" + str(self.StorageList[self.StorageListPointer][0]))[0]

        self.nud_quantity.setMinimum(0)
        self.nud_quantity.setMaximum(int(result[0]))
        self.nud_quantity.setValue(int(result[1]))

    def updateButtonNames(self):
        if (self.StorageListPointer == 0):
            self.btn_back.setText("Cancel")
        else:
            self.btn_back.setText("Back")

        if ((self.StorageListPointer + 1) >= self.StorageListPointerMax):
            self.btn_next.setText("Finish")
        else:
            self.btn_next.setText("Next")

    def updateMarkedArea(self):
        if (not self.isCurrentStorageSlotInUse()):
            maxInsidePosition = 1
            insidePoints = [self.ViewPosition1]
            insidePosition = int(self.StorageList[self.StorageListPointer][2])

            if (int(self.StorageList[self.StorageListPointer][5])):
                maxInsidePosition += 1
                insidePoints.append(self.ViewPosition2)
                insidePoints.append(self.ViewPosition3)

            if (int(self.StorageList[self.StorageListPointer][4])):
                maxInsidePosition += 1
                insidePoints.append(self.ViewPosition4)
                insidePoints.append(self.ViewPosition5)

            if (int(self.StorageList[self.StorageListPointer][3])):
                maxInsidePosition += 1
                insidePoints.append(self.ViewPosition6)
                insidePoints.append(self.ViewPosition7)

            insidePoints.append(self.ViewPosition8)

            if (maxInsidePosition <= 4):
                self.pnl_positionView.setVisible(True)
            
                if (insidePosition <= maxInsidePosition):                
                    insidePosition = (maxInsidePosition - insidePosition)
                    if (insidePosition >= 1):                  
                        insidePosition *= 2

                    startPoint = insidePoints[insidePosition]
                    endPoint = insidePoints[insidePosition + 1]
                    self.pnl_positionView.setGeometry(QtCore.QRect(330, startPoint, 141, (endPoint - startPoint)))

        else:
            self.pnl_positionView.setVisible(False)
            
    def updateSlotPicture(self):
        if (not self.isCurrentStorageSlotInUse()):
            divider1 = int(self.StorageList[self.StorageListPointer][3])
            divider2 = int(self.StorageList[self.StorageListPointer][4])
            divider3 = int(self.StorageList[self.StorageListPointer][5])

            self.pgb_storageSlotView.setPixmap(QtGui.QPixmap("images/storageSlot" + str(divider1) + str(divider2) + str(divider3) + ".png"))
        else:
            self.pgb_storageSlotView.setPixmap(QtGui.QPixmap("images/storageSlot000.png"))            

    def updateTexts(self):
        if (self.DisplayMode == 0):
            if (self.isCurrentStorageSlotInUse()):
                self.lbl_intruction.setText("Please wait! The current storage slot is used by another user!")
                self.lbl_itemCounter.setVisible(False)
            else:
                self.lbl_itemCounter.setVisible(True)
                self.lbl_itemCounter.setText("Store " + str(self.StoreInformation[0]) + "!")
                self.lbl_intruction.setText("Please put your item in the position marked on the right, in the storage slot blinking with the color below!")
        elif (self.DisplayMode == 1):
            quantity = int(self.StorageList[self.StorageListPointer][6])
            if (self.isCurrentStorageSlotInUse()):
                self.lbl_intruction.setText("Please wait! The current storage slot is used by another user!")
                self.lbl_itemCounter.setVisible(False)
            else:
                self.lbl_itemCounter.setVisible(True)

                if (quantity <= 0):
                    instructionText = "all items"
                elif (quantity == 1):
                    instructionText = "1 item"
                else:
                    instructionText = str(quantity) + " items"

                if (not self.MicroScaleOn):
                    self.lbl_itemCounter.setText("Pick " + instructionText + "!")
                self.lbl_intruction.setText("Please take " + instructionText + " out of the area marked on the right, from the storage slot blinking with the color below!")
        elif (self.DisplayMode == 2):
            if (self.isCurrentStorageSlotInUse()):
                self.lbl_intruction.setText("Please wait! The current storage slot is used by another user!")
                self.lbl_itemCounter.setVisible(False)
            else:
                self.lbl_itemCounter.setVisible(True)

                self.lbl_itemCounter.setText("Please set the quantity!")
                self.lbl_intruction.setText("Please count the quantity of the items in the area marked on the right, from the storage slot blinking with the color below!")

    def updateButtons(self):
        if ((not self.isNextStorageSlotInUse()) or ((self.StorageListPointer + 1) == self.StorageListPointerMax)):
            self.lbl_errorNextInUse.setVisible(False)
            self.btn_next.setEnabled(True)
        else:
            self.lbl_errorNextInUse.setVisible(True)
            self.btn_next.setEnabled(False)

        if ((not self.isPreviousStorageSlotInUse()) or ((self.StorageListPointer) == 0)):
            self.lbl_errorPreviousInUse.setVisible(False)
            self.btn_back.setEnabled(True)
        else:
            self.lbl_errorPreviousInUse.setVisible(True)
            self.btn_back.setEnabled(False)

        if (self.isCurrentStorageSlotInUse()):
            self.btn_next.setEnabled(False)
        else:
            self.btn_next.setEnabled(True)

        quantity = int(self.StorageList[self.StorageListPointer][6])
        if ((quantity > 0) and (self.DisplayMode != 2) and (self.DisplayMode != 0)):
            self.btn_useMicroScale.setVisible(True)
            itemID = int(MySQLDatabase.execSelect("SELECT itemID FROM storagep WHERE ID=" + str(self.StorageList[self.StorageListPointer][0]))[0][0])

            if (SSUFunctions.isMicroScaleUsageOK(itemID, quantity) or self.MicroScaleOn):
                self.btn_useMicroScale.setEnabled(True)
            else:
                self.btn_useMicroScale.setEnabled(False)
        else:
            self.btn_useMicroScale.setVisible(False)

    def isNextStorageSlotInUse(self):
        if ((self.StorageListPointer + 1) < self.StorageListPointerMax):
            result = MySQLDatabase.execSelect("SELECT * FROM activeLEDs WHERE SlotID=" + str(self.StorageList[(self.StorageListPointer + 1)][1]))

            if (len(result) <= 0):
                return False
        #else:
            #print("StorageListPointer is out of range!")
        
        return True

    def isCurrentStorageSlotInUse(self):
        result = MySQLDatabase.execSelect("SELECT * FROM activeLEDs WHERE SlotID=" + str(self.StorageList[(self.StorageListPointer)][1]))

        if ((len(result) <= 0) or self.LEDon):
            if (self.FirstTimeOn):
                self.FirstTimeOn = False
                self.turnLEDon()
            return False
        else:
            return True

    def isPreviousStorageSlotInUse(self):
        if ((self.StorageListPointer - 1) >= 0):
            result = MySQLDatabase.execSelect("SELECT * FROM activeLEDs WHERE SlotID=" + str(self.StorageList[(self.StorageListPointer - 1)][1]))

            if (len(result) <= 0):
                return False
        #else:
            #print("StorageListPointer is out of range!")
        
        return True

    def turnLEDon(self):
        if (not self.LEDon):
            self.LEDon = True
            slotID = int(self.StorageList[self.StorageListPointer][1])

            if (self.DisplayMode == 0):
                SSUFunctions.startLED(slotID, User.User.Color, 0)
            elif (self.DisplayMode == 1):
                SSUFunctions.startLED(slotID, User.User.Color, 3)
            elif (self.DisplayMode == 2):
                SSUFunctions.startLED(slotID, User.User.Color, 1)

    def turnLEDoff(self):
        if (self.LEDon):
            self.LEDon = False
            slotID = int(self.StorageList[self.StorageListPointer][1])

            SSUFunctions.stopLED(slotID)

    def onLoad_ShowStorageSlotScreen(self):
        if (not self.isCurrentStorageSlotInUse()):
            self.turnLEDon()

        self.updateButtonNames()

        if (self.DisplayMode == 2):
            self.updateNUD()

        self.screenUpdater()
        self.tmr_screenUpdater.start(500)