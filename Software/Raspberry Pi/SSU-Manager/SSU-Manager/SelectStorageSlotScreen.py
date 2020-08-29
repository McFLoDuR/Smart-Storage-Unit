from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
import User, db_connector, SSUFunctions, SetStorageInformationScreen

MySQLDatabase = db_connector.Database(host = "localhost", user = "ssu_db", password = "ssu_FRS", database = "ssu")

def clickable(widget):
    class Filter(QObject):
        clicked = pyqtSignal()
        def eventFilter(self, obj, event):
            if obj == widget:
                if event.type() == QEvent.MouseButtonRelease:
                    if obj.rect().contains(event.pos()):
                        self.clicked.emit()
                        return True
            return False

    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked

class Ui_SelectStorageSlotScreen(object):
    def setupUi(self, SelectStorageSlotScreen, parent, parentForm, itemID, storeInformation):
        self.Form = SelectStorageSlotScreen
        self.Parent = parent
        self.ParentForm = parentForm
        self.ItemID = itemID
        self.StoreInformation = storeInformation

        SelectStorageSlotScreen.setObjectName("SelectStorageSlotScreen")
        SelectStorageSlotScreen.setEnabled(True)
        SelectStorageSlotScreen.resize(800, 480)
        font = QtGui.QFont()
        font.setPointSize(14)
        SelectStorageSlotScreen.setFont(font)
        SelectStorageSlotScreen.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.centralwidget = QtWidgets.QWidget(SelectStorageSlotScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.pnl_color = QtWidgets.QFrame(self.centralwidget)
        self.pnl_color.setGeometry(QtCore.QRect(130, 310, 131, 81))
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
        self.btn_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancel.setGeometry(QtCore.QRect(100, 410, 181, 51))
        self.btn_cancel.setObjectName("btn_cancel")
        self.lbl_intruction = QtWidgets.QLabel(self.centralwidget)
        self.lbl_intruction.setGeometry(QtCore.QRect(80, 10, 231, 401))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lbl_intruction.setFont(font)
        self.lbl_intruction.setTextFormat(QtCore.Qt.RichText)
        self.lbl_intruction.setWordWrap(True)
        self.lbl_intruction.setObjectName("lbl_intruction")
        self.chb_divider2 = QtWidgets.QCheckBox(self.centralwidget)
        self.chb_divider2.setGeometry(QtCore.QRect(490, 199, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.chb_divider2.setFont(font)
        self.chb_divider2.setObjectName("chb_divider2")

        self.pnl_positionView1 = QtWidgets.QFrame(self.centralwidget)
        self.pnl_positionView1.setGeometry(QtCore.QRect(330, 310, 141, 121))
        self.pnl_positionView1.setAutoFillBackground(False)
        self.pnl_positionView1.setStyleSheet("background-color: #04ff00") # rgb(119, 255, 46)
        self.pnl_positionView1.setFrameShape(QtWidgets.QFrame.Panel)
        self.pnl_positionView1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pnl_positionView1.setObjectName("pnl_positionView1")
        self.pnl_positionView2 = QtWidgets.QFrame(self.centralwidget)
        self.pnl_positionView2.setGeometry(QtCore.QRect(330, 230, 141, 61))
        self.pnl_positionView2.setAutoFillBackground(False)
        self.pnl_positionView2.setStyleSheet("background-color: #03cf00")
        self.pnl_positionView2.setFrameShape(QtWidgets.QFrame.Panel)
        self.pnl_positionView2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pnl_positionView2.setObjectName("pnl_positionView2")
        self.pnl_positionView3 = QtWidgets.QFrame(self.centralwidget)
        self.pnl_positionView3.setGeometry(QtCore.QRect(330, 160, 141, 61))
        self.pnl_positionView3.setAutoFillBackground(False)
        self.pnl_positionView3.setStyleSheet("background-color: #029e00")
        self.pnl_positionView3.setFrameShape(QtWidgets.QFrame.Panel)
        self.pnl_positionView3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pnl_positionView3.setObjectName("pnl_positionView3")
        self.pnl_positionView4 = QtWidgets.QFrame(self.centralwidget)
        self.pnl_positionView4.setGeometry(QtCore.QRect(330, 20, 141, 121))
        self.pnl_positionView4.setAutoFillBackground(False)
        self.pnl_positionView4.setStyleSheet("background-color: #037001")
        self.pnl_positionView4.setFrameShape(QtWidgets.QFrame.Panel)
        self.pnl_positionView4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.pnl_positionView4.setObjectName("pnl_positionView4")

        self.chb_divider1 = QtWidgets.QCheckBox(self.centralwidget)
        self.chb_divider1.setGeometry(QtCore.QRect(490, 270, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.chb_divider1.setFont(font)
        self.chb_divider1.setObjectName("chb_divider1")
        self.chb_divider3 = QtWidgets.QCheckBox(self.centralwidget)
        self.chb_divider3.setGeometry(QtCore.QRect(490, 120, 271, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.chb_divider3.setFont(font)
        self.chb_divider3.setObjectName("chb_divider3")
        self.btn_prevSlot = QtWidgets.QPushButton(self.centralwidget)
        self.btn_prevSlot.setGeometry(QtCore.QRect(10, 10, 61, 461))
        self.btn_prevSlot.setObjectName("btn_prevSlot")
        self.btn_nextSlot = QtWidgets.QPushButton(self.centralwidget)
        self.btn_nextSlot.setGeometry(QtCore.QRect(730, 10, 61, 461))
        self.btn_nextSlot.setObjectName("btn_nextSlot")
        self.nud_stepSize = QtWidgets.QSpinBox(self.centralwidget)
        self.nud_stepSize.setGeometry(QtCore.QRect(520, 410, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.nud_stepSize.setFont(font)
        self.nud_stepSize.setAlignment(QtCore.Qt.AlignCenter)
        self.nud_stepSize.setObjectName("nud_stepSize")
        self.nud_stepSize.setStyleSheet("QSpinBox::up-button { width: 30px; } " + 
                                        "QSpinBox::down-button { width: 30px; }")
        self.nud_stepSize.setMinimum(1)
        self.nud_stepSize.setMaximum(100)
        self.lbl_stepSize = QtWidgets.QLabel(self.centralwidget)
        self.lbl_stepSize.setGeometry(QtCore.QRect(520, 390, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_stepSize.setFont(font)
        self.lbl_stepSize.setTextFormat(QtCore.Qt.RichText)
        self.lbl_stepSize.setWordWrap(True)
        self.lbl_stepSize.setObjectName("lbl_stepSize")
        SelectStorageSlotScreen.setCentralWidget(self.centralwidget)

        self.pnl_positionView1.setVisible(False)
        self.pnl_positionView2.setVisible(False)
        self.pnl_positionView3.setVisible(False)
        self.pnl_positionView4.setVisible(False)

        self.newItem = False
        self.SlotPointer = 0
        self.sumPartitions = 0
        self.SlotPointerMax = 0
        self.LEDon = False
        self.storagepList = []
        self.boxGlobal = []
        self.wall = 0
        self.WallCount = 0

        self.retranslateUi(SelectStorageSlotScreen)
        self.btn_cancel.clicked.connect(self.btn_cancel_clicked)
        self.btn_nextSlot.clicked.connect(self.btn_nextSlot_clicked)
        self.btn_prevSlot.clicked.connect(self.btn_prevSlot_clicked)
        self.chb_divider1.toggled.connect(self.chb_divider_changed)
        self.chb_divider2.toggled.connect(self.chb_divider_changed)
        self.chb_divider3.toggled.connect(self.chb_divider_changed)
        clickable(self.pnl_positionView1).connect(self.btn_positionView1_clicked)
        clickable(self.pnl_positionView2).connect(self.btn_positionView2_clicked)
        clickable(self.pnl_positionView3).connect(self.btn_positionView3_clicked)
        clickable(self.pnl_positionView4).connect(self.btn_positionView4_clicked)
        QtCore.QMetaObject.connectSlotsByName(SelectStorageSlotScreen)

    def retranslateUi(self, SelectStorageSlotScreen):
        _translate = QtCore.QCoreApplication.translate
        SelectStorageSlotScreen.setWindowTitle(_translate("SelectStorageSlotScreen", "MainWindow"))
        self.btn_cancel.setText(_translate("SelectStorageSlotScreen", "Cancel"))
        self.lbl_intruction.setText(_translate("SelectStorageSlotScreen", "Please select a Storage Slot for your item!"))
        self.chb_divider2.setText(_translate("SelectStorageSlotScreen", "Set Divider 2"))
        self.chb_divider1.setText(_translate("SelectStorageSlotScreen", "Set Divider 1"))
        self.chb_divider3.setText(_translate("SelectStorageSlotScreen", "Set Divider 3"))
        self.btn_prevSlot.setText(_translate("SelectStorageSlotScreen", "<<"))
        self.btn_nextSlot.setText(_translate("SelectStorageSlotScreen", ">>"))
        self.lbl_stepSize.setText(_translate("SelectStorageSlotScreen", "<html><head/><body><p>Set step size:</p></body></html>"))

    def btn_positionView1_clicked(self):
        self.storageSelected(1)

    def btn_positionView2_clicked(self):
        self.storageSelected(2)

    def btn_positionView3_clicked(self):
        self.storageSelected(3)

    def btn_positionView4_clicked(self):
        self.storageSelected(4)

    def btn_cancel_clicked(self):
        self.closeForm()

    def btn_nextSlot_clicked(self):
        self.turnLEDoff()
        step = self.nud_stepSize.value()
        if ((self.SlotPointer + step) > self.SlotPointerMax):
            self.SlotPointer = ((self.SlotPointer + step) - self.SlotPointerMax)
        else:
            self.SlotPointer += step
        self.turnLEDon()     
        self.updateCheckBox()
        self.updateScreen()

    def btn_prevSlot_clicked(self):
        self.turnLEDoff()
        step = self.nud_stepSize.value()
        if ((self.SlotPointer - step) < 0):
            self.SlotPointer = ((self.SlotPointer - step) + self.SlotPointerMax)
        else:
            self.SlotPointer -= step
        self.turnLEDon()
        self.updateCheckBox()
        self.updateScreen()

    def chb_divider_changed(self):
        if (not self.newItem):
            div1 = self.chb_divider1.isChecked()
            div2 = self.chb_divider2.isChecked()
            div3 = self.chb_divider3.isChecked()

            self.sumPartitions = 0
            picID = ""
            if (div1):
                picID += "1"
                self.wall = 1
                self.sumPartitions += 1
            else:
                picID += "0"

            if (div2):
                picID += "1"
                self.wall = 2
                self.sumPartitions += 1
            else:
                picID += "0"

            if (div3):
                picID += "1"
                self.wall = 3
                self.sumPartitions += 1
            else:
                picID += "0"

            self.pgb_storageSlotView.setPixmap(QtGui.QPixmap("images/storageSlot" + picID + ".png"))
            self.updateScreen()

    def closeForm(self):
        self.turnLEDoff()
        self.ParentForm.showFullScreen()
        self.Parent.dh.updateDataTable()
        self.Form.deleteLater()

    def onLoad_SelectStorageSlotScreen(self):
        self.possibleSlots = MySQLDatabase.execSelect("SELECT * FROM storageh sth WHERE (firstPartition+secondPartition+thirdPartition+1)>(SELECT COUNT(*) " +
                                                      "FROM storagep stp WHERE stp.storagehID=sth.ID) AND NOT ID IN (SELECT storagehID FROM storagep " +
                                                      "WHERE itemID =" + str(self.ItemID) + ") ORDER BY storagePosition")
        
        self.SlotPointerMax = (len(self.possibleSlots) - 1)
        self.nud_stepSize.setMaximum(self.SlotPointerMax)
        self.turnLEDon()
        self.updateCheckBox()
        self.updateScreen()

    def updateCheckBox(self):
        self.newItem = True
        storageh = self.possibleSlots[self.SlotPointer]
        storageps = MySQLDatabase.execSelect("SELECT * FROM storagep WHERE storagehID=" + str(self.possibleSlots[self.SlotPointer][0]) + " " +
                                             "ORDER BY insidePosition ASC")
        
        self.storagepList = []
        for row in storageps:
            self.storagepList.append(list(row))

        wallPlace = []     
        posToBox = []
        sumWalls = 0
        includesBoxes = 0
        wallCounter = 0

        picID = ""
        if (bool(self.possibleSlots[self.SlotPointer][2])):
            picID += "1"
            sumWalls += 1
            wallPlace.append(1)
            self.chb_divider1.setChecked(True)
        else:
            picID += "0"
            wallPlace.append(0)
            self.chb_divider1.setChecked(False)

        if (bool(self.possibleSlots[self.SlotPointer][3])):
            picID += "1"
            sumWalls += 1
            wallPlace.append(2)
            self.chb_divider2.setChecked(True)
        else:
            picID += "0"
            wallPlace.append(0)
            self.chb_divider2.setChecked(False)

        if (bool(self.possibleSlots[self.SlotPointer][4])):
            picID += "1"
            sumWalls += 1
            wallPlace.append(3)
            self.chb_divider3.setChecked(True)
        else:
            picID += "0"
            wallPlace.append(0)
            self.chb_divider3.setChecked(False)

        self.WallCount = sumWalls
        self.pgb_storageSlotView.setPixmap(QtGui.QPixmap("images/storageSlot" + picID + ".png"))

        for i in range(sumWalls+1):
            posToBox.append([])

        for i in range(sumWalls):
            for w in range(wallCounter, len(wallPlace)):
                if(wallPlace[w] != 0):
                    break
                else:
                    wallCounter += 1

            if (i > 0):
                boxes = 0
                for box in range(i):
                    boxes += len(posToBox[box])

                counter = wallPlace[wallCounter] - boxes
                wallCounter += 1
            else:
                counter = wallPlace[wallCounter]
                wallCounter += 1

            for j in range(counter):
                posToBox[i].append(0)
            includesBoxes += counter

        if (sumWalls == 0):
            for i in range(4):
                posToBox[0].append(0)
        if (sumWalls != 0):
            for i in range(4 - includesBoxes):
                posToBox[sumWalls].append(0)

        if (len(self.storagepList) > 0):
            for row in self.storagepList:
                for i in range(len(posToBox[(int(row[3]) - 1)])):
                    posToBox[(int(row[3]) - 1)][i] = int(row[2])

            box = [0]
            self.boxGlobal = []
            for pos in posToBox:
                for i in pos:
                    box.append(i)
                    self.boxGlobal.append(i)
            
            chbDividerVirt = [True, True, True]
            
            for i in range(1, (len(box) - 1)):
                chbIndex = (len(chbDividerVirt) - i)
                if ((box[i] != 0) and (box[i+1] == 0) and (box[i] != self.ItemID)):
                    chbDividerVirt[chbIndex] = False
                elif ((box[i] == 0) and (box[i+1] != 0) and (box[i+1] != self.ItemID)):
                    chbDividerVirt[chbIndex] = False
                elif ((box[i] != 0) and (box[i + 1] != 0)):
                    chbDividerVirt[chbIndex] = False
                else:
                    chbDividerVirt[chbIndex] = True           

            self.chb_divider1.setEnabled(chbDividerVirt[2])
            self.chb_divider2.setEnabled(chbDividerVirt[1])
            self.chb_divider3.setEnabled(chbDividerVirt[0])
        else:
            self.chb_divider1.setEnabled(True)
            self.chb_divider2.setEnabled(True)
            self.chb_divider3.setEnabled(True)

        if (self.newItem):
            self.sumPartitions = self.WallCount

        self.newItem = False

    def updateScreen(self):        
        self.pnl_positionView1.setVisible(False)
        self.pnl_positionView2.setVisible(False)
        self.pnl_positionView3.setVisible(False)
        self.pnl_positionView4.setVisible(False)        

        div1 = self.chb_divider1.isChecked()
        div2 = self.chb_divider2.isChecked()
        div3 = self.chb_divider3.isChecked()

        ViewPosition1 = 20
        ViewPosition2 = 146
        ViewPosition3 = 155
        ViewPosition4 = 225
        ViewPosition5 = 232
        ViewPosition6 = 300
        ViewPosition7 = 307
        ViewPosition8 = 428
        
        insidePoints = [ViewPosition1]
        possibleInsidePositions = 1
        if (div3):
            possibleInsidePositions += 1
            insidePoints.append(ViewPosition2)
            insidePoints.append(ViewPosition3)

        if (div2):
            possibleInsidePositions += 1
            insidePoints.append(ViewPosition4)
            insidePoints.append(ViewPosition5)

        if (div1):
            possibleInsidePositions += 1
            insidePoints.append(ViewPosition6)
            insidePoints.append(ViewPosition7)

        insidePoints.append(ViewPosition8)
               
        if (len(self.storagepList) > 0):
            for i in range(self.wall, len(self.boxGlobal)):
                for row in self.storagepList:
                    if (self.boxGlobal[i] == int(row[2])):
                        if (self.WallCount > self.sumPartitions):
                            row[3] = (int(row[3]) - 1)
                        elif (self.WallCount < self.sumPartitions):
                            row[3] = (int(row[3]) + 1)

                        for w in range(i+1, len(self.boxGlobal)):
                            if (self.boxGlobal[w] != int(row[2])):
                                break
                            i += 1
            
        usedPositions = []
        for row in self.storagepList:
            usedPositions.append(int(row[3]))

        for i in range(possibleInsidePositions): 
            if (not ((i + 1) in usedPositions)):                
                self.setPanel((i + 1), possibleInsidePositions, insidePoints)

    def setPanel(self, insidePos, maxInsidePos, viewpoints):
        insidePosSave = insidePos
        insidePos = (maxInsidePos - insidePos)

        if (insidePos >= 1):                  
            insidePos *= 2

        startPoint = viewpoints[insidePos]
        endPoint = viewpoints[insidePos + 1]
        
        if (insidePosSave == 1):
            self.pnl_positionView1.setGeometry(QtCore.QRect(330, startPoint, 141, (endPoint - startPoint)))
            self.pnl_positionView1.setVisible(True)
        elif (insidePosSave == 2):
            self.pnl_positionView2.setGeometry(QtCore.QRect(330, startPoint, 141, (endPoint - startPoint)))
            self.pnl_positionView2.setVisible(True)         
        elif (insidePosSave == 3):
            self.pnl_positionView3.setGeometry(QtCore.QRect(330, startPoint, 141, (endPoint - startPoint)))
            self.pnl_positionView3.setVisible(True)  
        elif (insidePosSave == 4):
            self.pnl_positionView4.setGeometry(QtCore.QRect(330, startPoint, 141, (endPoint - startPoint)))
            self.pnl_positionView4.setVisible(True)    

    def storageSelected(self, insidePosition):
        self.turnLEDoff()
        self.StoreInformation.append(self.possibleSlots[self.SlotPointer][0]) # 2
        self.StoreInformation.append(insidePosition) # 3
        dividerList = [self.chb_divider1.isChecked(), self.chb_divider2.isChecked(), self.chb_divider3.isChecked()] # 4
        self.StoreInformation.append(dividerList)

        self.ssis = QtWidgets.QMainWindow()
        self.ui = SetStorageInformationScreen.Ui_SetStorageInformationScreen()
        self.ui.setupUi(self.ssis, self.Parent, self.ParentForm, self.ItemID, self.StoreInformation, self.storagepList)
        self.ssis.showFullScreen()
        self.Form.deleteLater()


    def turnLEDon(self):
        if (not self.LEDon):
            result = MySQLDatabase.execSelect("SELECT * FROM activeLEDs WHERE SlotID=" + str(self.possibleSlots[self.SlotPointer][1]))

            if (len(result) <= 0):
                self.LEDon = True
                slotID = int(self.possibleSlots[self.SlotPointer][1])

                SSUFunctions.startLED(slotID, User.User.Color, 0)
            else:
                self.turnLEDoff()
                step = 1
                if ((self.SlotPointer + step) > self.SlotPointerMax):
                    self.SlotPointer = ((self.SlotPointer + step) - self.SlotPointerMax)
                else:
                    self.SlotPointer += step
                self.turnLEDon()     
                self.updateCheckBox()
                self.updateScreen()

    def turnLEDoff(self):
        if (self.LEDon):
            self.LEDon = False
            slotID = int(self.possibleSlots[self.SlotPointer][1])

            SSUFunctions.stopLED(slotID)