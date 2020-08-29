from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import db_connector, User, SSUFunctions

MySQLDatabase = db_connector.Database(host = "localhost", user = "ssu_db", password = "ssu_FRS", database = "ssu")

class Ui_NewEditPermissionScreen(object):
    def setupUi(self, NewEditPermissionScreen, mus, updater, permissionID):
        self.Form = NewEditPermissionScreen
        self.ManageUserScreen = mus
        self.Updater = updater
        self.PermissionID = permissionID

        offset1 = -50
        offset2 = -25
        NewEditPermissionScreen.setObjectName("NewEditPermissionScreen")
        NewEditPermissionScreen.resize(800, 480)
        font = QtGui.QFont()
        font.setPointSize(14)
        NewEditPermissionScreen.setFont(font)
        NewEditPermissionScreen.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.centralwidget = QtWidgets.QWidget(NewEditPermissionScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancel.setGeometry(QtCore.QRect(10, 420, 201, 51))
        self.btn_cancel.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(590, 420, 201, 51))
        self.btn_save.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.btn_save.setObjectName("btn_save")
        self.lbl_permission = QtWidgets.QLabel(self.centralwidget)
        self.lbl_permission.setGeometry(QtCore.QRect(0, 10, 801, 31))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_permission.setFont(font)
        self.lbl_permission.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_permission.setObjectName("lbl_permission")
        self.lbl_permissionName = QtWidgets.QLabel(self.centralwidget)
        self.lbl_permissionName.setGeometry(QtCore.QRect(200, 60, 401, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_permissionName.setFont(font)
        self.lbl_permissionName.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.lbl_permissionName.setObjectName("lbl_permissionName")
        self.txb_permissionName = QtWidgets.QLineEdit(self.centralwidget)
        self.txb_permissionName.setGeometry(QtCore.QRect(200, 90, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.txb_permissionName.setFont(font)
        self.txb_permissionName.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.txb_permissionName.setInputMask("")
        self.txb_permissionName.setText("")
        self.txb_permissionName.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.txb_permissionName.setAlignment(QtCore.Qt.AlignCenter)
        self.txb_permissionName.setObjectName("txb_permissionName")
        self.lbl_errorPermissionName = QtWidgets.QLabel(self.centralwidget)
        self.lbl_errorPermissionName.setEnabled(True)
        self.lbl_errorPermissionName.setGeometry(QtCore.QRect(200, 60, 401, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_errorPermissionName.setFont(font)
        self.lbl_errorPermissionName.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.lbl_errorPermissionName.setScaledContents(False)
        self.lbl_errorPermissionName.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_errorPermissionName.setObjectName("lbl_errorPermissionName")
        self.lbl_errorPermissionName.setVisible(False)
        self.chb_manageUsers = QtWidgets.QCheckBox(self.centralwidget)
        self.chb_manageUsers.setGeometry(QtCore.QRect(170 + offset1, 150, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.chb_manageUsers.setFont(font)
        self.chb_manageUsers.setObjectName("chb_manageUsers")
        self.chb_storeItems = QtWidgets.QCheckBox(self.centralwidget)
        self.chb_storeItems.setGeometry(QtCore.QRect(170 + offset1, 210, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.chb_storeItems.setFont(font)
        self.chb_storeItems.setObjectName("chb_storeItems")
        self.chb_withdrawItems = QtWidgets.QCheckBox(self.centralwidget)
        self.chb_withdrawItems.setGeometry(QtCore.QRect(170 + offset1, 270, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.chb_withdrawItems.setFont(font)
        self.chb_withdrawItems.setObjectName("chb_withdrawItems")
        self.chb_deleteStorageSlot = QtWidgets.QCheckBox(self.centralwidget)
        self.chb_deleteStorageSlot.setGeometry(QtCore.QRect(170 + offset1, 330, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.chb_deleteStorageSlot.setFont(font)
        self.chb_deleteStorageSlot.setObjectName("chb_deleteStorageSlot")
        self.chb_moveStorageSlot = QtWidgets.QCheckBox(self.centralwidget)
        self.chb_moveStorageSlot.setGeometry(QtCore.QRect(460 + offset2, 210, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.chb_moveStorageSlot.setFont(font)
        self.chb_moveStorageSlot.setObjectName("chb_moveStorageSlot")
        #self.chb_managePartitions = QtWidgets.QCheckBox(self.centralwidget)
        #self.chb_managePartitions.setGeometry(QtCore.QRect(460 + offset2, 270, 401, 41))
        #font = QtGui.QFont()
        #font.setPointSize(18)
        #self.chb_managePartitions.setFont(font)
        #self.chb_managePartitions.setObjectName("chb_managePartitions")
        self.chb_correctQuantity = QtWidgets.QCheckBox(self.centralwidget)
        self.chb_correctQuantity.setGeometry(QtCore.QRect(460 + offset2, 270, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.chb_correctQuantity.setFont(font)
        self.chb_correctQuantity.setObjectName("chb_correctQuantity")
        self.chb_createInventoryReport = QtWidgets.QCheckBox(self.centralwidget)
        self.chb_createInventoryReport.setGeometry(QtCore.QRect(460 + offset2, 150, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.chb_createInventoryReport.setFont(font)
        self.chb_createInventoryReport.setObjectName("chb_createInventoryReport")
        NewEditPermissionScreen.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(NewEditPermissionScreen)
        self.btn_cancel.clicked.connect(self.btn_cancel_clicked)
        self.btn_save.clicked.connect(self.btn_save_clicked)
        QtCore.QMetaObject.connectSlotsByName(NewEditPermissionScreen)

    def retranslateUi(self, NewEditPermissionScreen):
        _translate = QtCore.QCoreApplication.translate
        NewEditPermissionScreen.setWindowTitle(_translate("NewEditPermissionScreen", "MainWindow"))
        self.btn_cancel.setText(_translate("NewEditPermissionScreen", "Cancel"))
        self.btn_save.setText(_translate("NewEditPermissionScreen", "Save"))

        if (self.PermissionID > 0):
            addon = "Edit"
        else:
            addon = "New"

        self.lbl_permission.setText(_translate("NewEditPermissionScreen", addon + " Role"))
        self.lbl_permissionName.setText(_translate("NewEditPermissionScreen", "Role Name:"))
        self.lbl_errorPermissionName.setText(_translate("NewEditPermissionScreen", "<html><head/><body><p><span style=\" color:#ff0000;\">Role Name is taken!</span></p></body></html>"))
        self.chb_manageUsers.setText(_translate("NewEditPermissionScreen", "Manage Users"))
        self.chb_storeItems.setText(_translate("NewEditPermissionScreen", "Store Items"))
        self.chb_withdrawItems.setText(_translate("NewEditPermissionScreen", "Withdraw Items"))
        self.chb_deleteStorageSlot.setText(_translate("NewEditPermissionScreen", "Delete Storage Slot"))
        self.chb_moveStorageSlot.setText(_translate("NewEditPermissionScreen", "Move Storage Slot"))
        #self.chb_managePartitions.setText(_translate("NewEditPermissionScreen", "Manage Partitions"))
        self.chb_correctQuantity.setText(_translate("NewEditPermissionScreen", "Correct Quantity"))
        self.chb_createInventoryReport.setText(_translate("NewEditPermissionScreen", "Create Inventory Report"))

    def btn_cancel_clicked(self):
        self.ManageUserScreen.showFullScreen()
        self.Form.deleteLater()

    def btn_save_clicked(self):
        permissionName = str(self.txb_permissionName.text())        
        
        if (self.checkReadyToSave(permissionName)):
            manageUsers = "FALSE"
            storeItems = "FALSE"
            withdrawItems = "FALSE"
            deleteStorageSlot = "FALSE"
            moveStorageSlot = "FALSE"
            managePartitions = "FALSE"
            correctQuantity = "FALSE"
            createInventoryReport = "FALSE"

            if (self.chb_manageUsers.isChecked()):
                manageUsers = "TRUE"
            if (self.chb_storeItems.isChecked()):
                storeItems = "TRUE"
            if (self.chb_withdrawItems.isChecked()):
                withdrawItems = "TRUE"
            if (self.chb_deleteStorageSlot.isChecked()):
                deleteStorageSlot = "TRUE"
            if (self.chb_moveStorageSlot.isChecked()):
                moveStorageSlot = "TRUE"
            #if (self.chb_managePartitions.isChecked()):
                #managePartitions = "TRUE"
            if (self.chb_correctQuantity.isChecked()):
                correctQuantity = "TRUE"
            if (self.chb_createInventoryReport.isChecked()):
                createInventoryReport = "TRUE"

            if (self.PermissionID > 0):
                MySQLDatabase.execDML("UPDATE permissions SET permissionName='" + permissionName + "', manageUsers=" + manageUsers + ", storeItems=" + storeItems + ", withdrawItems=" + withdrawItems + ", " + 
                                      "deleteStorageSlot=" + deleteStorageSlot + ", moveStorageSlot=" + moveStorageSlot + ", managePartitions=" + managePartitions + ", " + 
                                      "correctQuantity=" + correctQuantity + ", createInventoryReport=" + createInventoryReport + " WHERE ID=" + str(self.PermissionID))
            else:
                MySQLDatabase.execDML("INSERT INTO permissions(permissionName, manageUsers, storeItems, withdrawItems, deleteStorageSlot, moveStorageSlot, managePartitions, correctQuantity, createInventoryReport) " + 
                                      "VALUES('" + permissionName + "', " + manageUsers + ", " + storeItems + ", " + withdrawItems + 
                                      ", " + deleteStorageSlot + ", " + moveStorageSlot + ", " + managePartitions + ", " + correctQuantity + ", " + createInventoryReport + ")")
                   
            self.Updater.getPermissionData(self.Updater.txb_search.text())
            self.Updater.setPermissionData()
            self.ManageUserScreen.showFullScreen()
            self.Form.deleteLater()    
        else:
            if (self.PermissionID > 0):
                self.txb_permissionName.setText(self.__PermissionName)

    def checkReadyToSave(self, permissionname):
        permissionNameError = True

        if (self.checkPermissionNameOK(permissionname)):
            permissionNameError = False

        return (not permissionNameError)

    def checkPermissionNameOK(self, permissionname):
        if (not SSUFunctions.isStringEmptyOrSpace(permissionname)):
            if (self.PermissionID > 0):
                permissionAddon = " AND NOT ID=" + str(self.PermissionID)
            else:
                permissionAddon = ""

            permissions = MySQLDatabase.execSelect("SELECT ID FROM permissions WHERE permissionname='" + permissionname + "'" + permissionAddon)

            if (len(permissions) > 0):
                errorText = "<span style=\" color:#ff0000;\">Permission Name is taken!"
            else:
                self.lbl_errorPermissionName.setVisible(False)
                return True
        else:
            errorText = "<span style=\" color:#ff0000;\">Enter Permission Name!"

        self.lbl_errorPermissionName.setText(errorText)
        self.txb_permissionName.setText("")
        self.lbl_errorPermissionName.setVisible(True)
        return False

    def onLoad_NewEditPermissionScreen(self):
        if (self.PermissionID > 0):
            permissions = MySQLDatabase.execSelect("SELECT * FROM permissions WHERE ID=" + str(self.PermissionID))[0]

            self.__PermissionName = str(permissions[1])
            self.txb_permissionName.setText(self.__PermissionName)

            if (int(permissions[2]) > 0):
                self.chb_manageUsers.setChecked(True)
            if (int(permissions[3]) > 0):
                self.chb_storeItems.setChecked(True)
            if (int(permissions[4]) > 0):
                self.chb_withdrawItems.setChecked(True)
            if (int(permissions[5]) > 0):
                self.chb_deleteStorageSlot.setChecked(True)
            if (int(permissions[6]) > 0):
                self.chb_moveStorageSlot.setChecked(True)
            #if (int(permissions[7]) > 0):
                #self.chb_managePartitions.setChecked(True)
            if (int(permissions[8]) > 0):
                self.chb_correctQuantity.setChecked(True)
            if (int(permissions[9]) > 0):
                self.chb_createInventoryReport.setChecked(True)

        if (not (User.User.PermManageUsers > 0)):
            self.chb_manageUsers.setEnabled(False)
        if (not (User.User.PermStoreItems > 0)):
            self.chb_storeItems.setEnabled(False)
        if (not (User.User.PermWithdrawItems > 0)):
            self.chb_withdrawItems.setEnabled(False)
        if (not (User.User.PermDeleteStorageSlot > 0)):
            self.chb_deleteStorageSlot.setEnabled(False)
        if (not (User.User.PermMoveStorageSlot > 0)):
            self.chb_moveStorageSlot.setEnabled(False)
        #if (not (User.User.PermManagePartitions > 0)):
            #self.chb_managePartitions.setEnabled(False)
        if (not (User.User.PermCorrectQuantity > 0)):
            self.chb_correctQuantity.setEnabled(False)
        if (not (User.User.PermCreateInventoryReport > 0)):
            self.chb_createInventoryReport.setEnabled(False)