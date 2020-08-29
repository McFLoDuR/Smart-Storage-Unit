from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import db_connector, User, NewEditUserScreen, NewEditPermissionScreen

MySQLDatabase = db_connector.Database(host = "localhost", user = "ssu_db", password = "ssu_FRS", database = "ssu")

class Ui_ManageUserPermissionScreen(object):
    def setupUi(self, ManageUserPermissionScreen, manageUser, mainScreen):
        self.Form = ManageUserPermissionScreen
        self.ManageUser = manageUser
        self.MainScreen = mainScreen

        ManageUserPermissionScreen.setObjectName("ManageUserPermissionScreen")
        ManageUserPermissionScreen.resize(800, 480)
        font = QtGui.QFont()
        font.setPointSize(14)
        ManageUserPermissionScreen.setFont(font)
        ManageUserPermissionScreen.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.centralwidget = QtWidgets.QWidget(ManageUserPermissionScreen)
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
        self.dtv_tupels = QtWidgets.QTableWidget(self.centralwidget)
        self.dtv_tupels.setGeometry(QtCore.QRect(220, 120, 571, 291))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dtv_tupels.setFont(font)
        self.dtv_tupels.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.dtv_tupels.setObjectName("dtv_tupels")
        self.dtv_tupels.setColumnCount(0)
        self.dtv_tupels.setRowCount(0)
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
        self.liv_permissions = QtWidgets.QListWidget(self.centralwidget)
        self.liv_permissions.setGeometry(QtCore.QRect(10, 190, 201, 221))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.liv_permissions.setFont(font)
        self.liv_permissions.setObjectName("liv_permissions")
        self.lbl_permissions = QtWidgets.QLabel(self.centralwidget)
        self.lbl_permissions.setGeometry(QtCore.QRect(10, 160, 201, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_permissions.setFont(font)
        self.lbl_permissions.setObjectName("lbl_permissions")
        ManageUserPermissionScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(ManageUserPermissionScreen)
        self.btn_new.clicked.connect(self.btn_new_clicked)
        self.btn_edit.clicked.connect(self.btn_edit_clicked)
        self.btn_delete.clicked.connect(self.btn_delete_clicked)
        self.btn_cancel.clicked.connect(self.btn_cancel_clicked)
        self.btn_search.clicked.connect(self.btn_search_clicked)
        self.dtv_tupels.itemSelectionChanged.connect(self.tupel_selected)        
        QtCore.QMetaObject.connectSlotsByName(ManageUserPermissionScreen)

    def retranslateUi(self, ManageUserPermissionScreen):
        _translate = QtCore.QCoreApplication.translate

        if (self.ManageUser):
            addon = "User"
        else:
            addon = "Role"

        ManageUserPermissionScreen.setWindowTitle(_translate("ManageUserPermissionScreen", "MainWindow"))
        self.btn_search.setText(_translate("ManageUserPermissionScreen", "Search"))
        self.btn_cancel.setText(_translate("ManageUserPermissionScreen", "Cancel"))
        self.btn_new.setText(_translate("ManageUserPermissionScreen", ("New " + addon)))
        self.btn_edit.setText(_translate("ManageUserPermissionScreen", ("Edit " + addon)))
        self.btn_delete.setText(_translate("ManageUserPermissionScreen", ("Delete " + addon)))
        self.lbl_permissions.setText(_translate("ManageUserPermissionScreen", "Permissions:"))

        if (self.ManageUser):
            addon = "Users"
        else:
            addon = "Roles"

        self.lbl_screenTitle.setText(_translate("ManageUserPermissionScreen", "Manage " + addon))

    def btn_new_clicked(self):
        if (self.ManageUser):
            self.meus = QtWidgets.QMainWindow()
            self.ui = NewEditUserScreen.Ui_NewEditUserScreen()
            self.ui.setupUi(self.meus, self.Form, self, 0)
            self.meus.showFullScreen()
            self.Form.hide()
            t = QtCore.QTimer(self.Form)
            t.singleShot(0, self.ui.onLoad_NewEditUserScreen)
        else:
            self.meps = QtWidgets.QMainWindow()
            self.ui = NewEditPermissionScreen.Ui_NewEditPermissionScreen()
            self.ui.setupUi(self.meps, self.Form, self, 0)
            self.meps.showFullScreen()
            self.Form.hide()
            t = QtCore.QTimer(self.Form)
            t.singleShot(0, self.ui.onLoad_NewEditPermissionScreen)

    def btn_edit_clicked(self):
        if (self.ManageUser):
            self.meus = QtWidgets.QMainWindow()
            self.ui = NewEditUserScreen.Ui_NewEditUserScreen()
            self.ui.setupUi(self.meus, self.Form, self, self.__userID)
            self.meus.showFullScreen()
            self.Form.hide()
            t = QtCore.QTimer(self.Form)
            t.singleShot(0, self.ui.onLoad_NewEditUserScreen)
        else:
            self.meps = QtWidgets.QMainWindow()
            self.ui = NewEditPermissionScreen.Ui_NewEditPermissionScreen()
            self.ui.setupUi(self.meps, self.Form, self, self.__permissionID)
            self.meps.showFullScreen()
            self.Form.hide()
            t = QtCore.QTimer(self.Form)
            t.singleShot(0, self.ui.onLoad_NewEditPermissionScreen)

    def btn_delete_clicked(self):
        msg = QMessageBox(self.Form)
        msg.setIcon(QMessageBox.Warning) 
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        if (self.ManageUser):     
            msg.setText("Do you really want to delete this User?")
            msg.setWindowTitle("Delete?!")            
            buttonResult = msg.exec_()

            if (buttonResult == QMessageBox.Yes):
                MySQLDatabase.execDML("DELETE FROM users WHERE ID=" + str(self.__userID))

            self.getUserData(self.txb_search.text())
            self.setUserData()
        else:
            if (int(self.__permissionResult[self.__rowIndex][1]) == 0):                
                msg.setText("Do you really want to delete this Permission?")
                msg.setWindowTitle("Delete?!")            
                buttonResult = msg.exec_()

                if (buttonResult == QMessageBox.Yes):
                    MySQLDatabase.execDML("DELETE FROM permissions WHERE ID=" + str(self.__permissionID))

                self.getPermissionData(self.txb_search.text())
                self.setPermissionData()
            else:                  
                msg.setStandardButtons(QMessageBox.Ok)
                msg.setIcon(QMessageBox.Critical) 
                msg.setText("There are still users assigned to this permission!")
                msg.setWindowTitle("ERROR!")            
                msg.exec_()

    def btn_search_clicked(self):
        searchString = self.txb_search.text()

        if (self.ManageUser):
            self.getUserData(searchString)
            self.setUserData()
        else:
            self.getPermissionData(searchString)
            self.setPermissionData()

    def tupel_selected(self):
        try:
            self.__rowIndex = int(self.dtv_tupels.selectedItems()[0].row())
            
            if (self.ManageUser):
                self.__permissionID = int(self.__userResult[self.__rowIndex][4])
                self.__userID = int(self.__userResult[self.__rowIndex][0])
            else:
                self.__permissionID = int(self.__permissionResult[self.__rowIndex][2])

            self.btn_delete.setEnabled(True)
            self.btn_edit.setEnabled(True)
            self.setPermissionDataList(self.__permissionID)
        except:
            self.btn_delete.setEnabled(False)
            self.btn_edit.setEnabled(False)
            print("A problem occured while selecting a user or permission!")

    def setPermissionDataList(self, rowIndex):
        permissions = MySQLDatabase.execSelect("SELECT storeItems, withdrawItems, createInventoryReport, deleteStorageSlot, moveStorageSlot, correctQuantity, manageUsers " + 
                                               "FROM permissions WHERE ID=" + str(rowIndex))[0]

        permList = ["Store", "Withdraw", "Create Report", "Delete Slot", "Move Slot", "Corr. Quantity", "Mange Users"]
        permStateList = []

        for perm in permissions:
            if(int(perm) > 0):
                permStateList.append("yes")
            else:
                permStateList.append("no")

        self.liv_permissions.clear()
        for i in range(len(permList)):
            item = (permList[i] + ": " + permStateList[i])
            self.liv_permissions.addItem(item)
            itemState = self.liv_permissions.item(i)
            itemState.setFlags(itemState.flags() & ~Qt.ItemIsSelectable)

    def btn_cancel_clicked(self):
        self.backToMainScreen()

    def onLoad_ManageUserPermissionScreen(self):
        if(self.ManageUser):
            self.getUserData("")
            self.setUserData()
        else:
            self.getPermissionData("")
            self.setPermissionData()

    def getPermissionData(self, searchString):
        if (searchString):
            self.__permissionResult = MySQLDatabase.execSelect("SELECT p.permissionname, COALESCE((SELECT COUNT(permissionID) FROM users WHERE permissionID=p.ID GROUP BY permissionID), 0) AssignedUsers, p.ID  " +
	                                                           "FROM permissions p " +
                                                               "WHERE p.ID IN (SELECT perm.ID FROM permissions perm, " +
                                                               "(SELECT * FROM permissions WHERE ID=" + str(User.User.PermID) + ") temp " +
                                                               "WHERE ((perm.manageUsers = temp.manageUsers) OR (perm.manageUsers = 0)) " +
                                                               "AND ((perm.storeItems = temp.storeItems) OR (perm.storeItems = 0)) " +
                                                               "AND ((perm.withdrawItems = temp.withdrawItems) OR (perm.withdrawItems = 0)) " +
                                                               "AND ((perm.deleteStorageSlot = temp.deleteStorageSlot) OR (perm.deleteStorageSlot = 0)) " +
                                                               "AND ((perm.moveStorageSlot = temp.moveStorageSlot) OR (perm.moveStorageSlot = 0)) " +
                                                               "AND ((perm.managePartitions = temp.managePartitions) OR (perm.managePartitions = 0)) " +
                                                               "AND ((perm.correctQuantity = temp.correctQuantity) OR (perm.correctQuantity = 0)) " +
                                                               "AND ((perm.createInventoryReport = temp.createInventoryReport) OR (perm.createInventoryReport = 0))) " + 
                                                               "AND p.permissionname LIKE '" + searchString + "%' " + 
	                                                           "AND NOT p.ID=" + str(User.User.PermID) + " AND NOT p.permissionname='admin' " +
	                                                           "ORDER AssignedUsers DESC")

        else:
            self.__permissionResult = MySQLDatabase.execSelect("SELECT p.permissionname, COALESCE((SELECT COUNT(permissionID) FROM users WHERE permissionID=p.ID GROUP BY permissionID), 0) AssignedUsers, p.ID  " +
	                                                           "FROM permissions p " +
                                                               "WHERE p.ID IN (SELECT perm.ID FROM permissions perm, " +
                                                               "(SELECT * FROM permissions WHERE ID=" + str(User.User.PermID) + ") temp " +
                                                               "WHERE ((perm.manageUsers = temp.manageUsers) OR (perm.manageUsers = 0)) " +
                                                               "AND ((perm.storeItems = temp.storeItems) OR (perm.storeItems = 0)) " +
                                                               "AND ((perm.withdrawItems = temp.withdrawItems) OR (perm.withdrawItems = 0)) " +
                                                               "AND ((perm.deleteStorageSlot = temp.deleteStorageSlot) OR (perm.deleteStorageSlot = 0)) " +
                                                               "AND ((perm.moveStorageSlot = temp.moveStorageSlot) OR (perm.moveStorageSlot = 0)) " +
                                                               "AND ((perm.managePartitions = temp.managePartitions) OR (perm.managePartitions = 0)) " +
                                                               "AND ((perm.correctQuantity = temp.correctQuantity) OR (perm.correctQuantity = 0)) " +
                                                               "AND ((perm.createInventoryReport = temp.createInventoryReport) OR (perm.createInventoryReport = 0))) " + 
	                                                           "AND NOT p.ID=" + str(User.User.PermID) + " AND NOT p.permissionname='admin' " +
	                                                           "ORDER BY AssignedUsers DESC")

    def setPermissionData(self):
        self.dtv_tupels.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.dtv_tupels.setSelectionMode(QAbstractItemView.SingleSelection)
        self.dtv_tupels.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.dtv_tupels.setColumnCount(2)
        self.dtv_tupels.setRowCount(0)

        self.dtv_tupels.setHorizontalHeaderLabels(("Role Name", "Assigned Users"))
        header = self.dtv_tupels.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.liv_permissions.clear()

        for row in self.__permissionResult:
            rowPosition = self.dtv_tupels.rowCount()
            self.dtv_tupels.insertRow(rowPosition)

            for i in range(2):
                item = QTableWidgetItem(str(row[i]))
                item.setTextAlignment(Qt.AlignCenter)
                self.dtv_tupels.setItem(rowPosition, i, item)

            self.dtv_tupels.verticalHeader().setSectionResizeMode(rowPosition, QHeaderView.Fixed)

    def getUserData(self, searchString):
        if (searchString):
            self.__userResult = MySQLDatabase.execSelect("SELECT us.ID, us.username, us.email, perm.permissionname, us.permissionID FROM users us, permissions perm " +
                                                         "WHERE us.permissionID = perm.ID AND NOT us.username='blackColorBlocker' AND NOT us.username='redColorBlocker' AND NOT us.ID=" + str(User.User.Id) + " AND " +
                                                         "(us.username LIKE '" + searchString + "%' OR us.email LIKE '" + searchString + "%' OR perm.permissionname LIKE '" + searchString + "%') AND " + 
                                                         "us.permissionID IN " +
                                                         "(SELECT perm.ID FROM permissions perm, " +
                                                         "(SELECT * FROM permissions WHERE ID=" + str(User.User.PermID) + ") temp " +
                                                         "WHERE ((perm.manageUsers = temp.manageUsers) OR (perm.manageUsers = 0)) " +
                                                         "AND ((perm.storeItems = temp.storeItems) OR (perm.storeItems = 0)) " +
                                                         "AND ((perm.withdrawItems = temp.withdrawItems) OR (perm.withdrawItems = 0)) " +
                                                         "AND ((perm.deleteStorageSlot = temp.deleteStorageSlot) OR (perm.deleteStorageSlot = 0)) " +
                                                         "AND ((perm.moveStorageSlot = temp.moveStorageSlot) OR (perm.moveStorageSlot = 0)) " +
                                                         "AND ((perm.managePartitions = temp.managePartitions) OR (perm.managePartitions = 0)) " +
                                                         "AND ((perm.correctQuantity = temp.correctQuantity) OR (perm.correctQuantity = 0)) " +
                                                         "AND ((perm.createInventoryReport = temp.createInventoryReport) OR (perm.createInventoryReport = 0)))")

        else:
            self.__userResult = MySQLDatabase.execSelect("SELECT us.ID, us.username, us.email, perm.permissionname, us.permissionID FROM users us, permissions perm " +
                                                         "WHERE us.permissionID = perm.ID AND NOT us.username='blackColorBlocker' AND NOT us.username='redColorBlocker' AND NOT us.ID=" + str(User.User.Id) + " AND " +
                                                         "us.permissionID IN " +
                                                         "(SELECT perm.ID FROM permissions perm, " +
                                                         "(SELECT * FROM permissions WHERE ID=" + str(User.User.PermID) + ") temp " +
                                                         "WHERE ((perm.manageUsers = temp.manageUsers) OR (perm.manageUsers = 0)) " +
                                                         "AND ((perm.storeItems = temp.storeItems) OR (perm.storeItems = 0)) " +
                                                         "AND ((perm.withdrawItems = temp.withdrawItems) OR (perm.withdrawItems = 0)) " +
                                                         "AND ((perm.deleteStorageSlot = temp.deleteStorageSlot) OR (perm.deleteStorageSlot = 0)) " +
                                                         "AND ((perm.moveStorageSlot = temp.moveStorageSlot) OR (perm.moveStorageSlot = 0)) " +
                                                         "AND ((perm.managePartitions = temp.managePartitions) OR (perm.managePartitions = 0)) " +
                                                         "AND ((perm.correctQuantity = temp.correctQuantity) OR (perm.correctQuantity = 0)) " +
                                                         "AND ((perm.createInventoryReport = temp.createInventoryReport) OR (perm.createInventoryReport = 0)))")

    def setUserData(self):
        self.dtv_tupels.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.dtv_tupels.setSelectionMode(QAbstractItemView.SingleSelection)
        self.dtv_tupels.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.dtv_tupels.setColumnCount(3)
        self.dtv_tupels.setRowCount(0)

        self.dtv_tupels.setHorizontalHeaderLabels(("Username", "Email", "Permissions"))
        header = self.dtv_tupels.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        self.liv_permissions.clear()

        for row in self.__userResult:
            rowPosition = self.dtv_tupels.rowCount()
            self.dtv_tupels.insertRow(rowPosition)

            for i in range(3):
                item = QTableWidgetItem(str(row[i + 1]))

                if (i > 0):
                    item.setTextAlignment(Qt.AlignCenter)

                self.dtv_tupels.setItem(rowPosition, i, item)

            self.dtv_tupels.verticalHeader().setSectionResizeMode(rowPosition, QHeaderView.Fixed)

    def backToMainScreen(self):
        User.User.MainScreen.showFullScreen()
        self.MainScreen.dh.updateDataTable()
        self.Form.deleteLater()