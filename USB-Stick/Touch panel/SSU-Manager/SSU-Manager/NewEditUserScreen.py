from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import db_connector, re, User, SSUFunctions

MySQLDatabase = db_connector.Database(host = "localhost", user = "ssu_db", password = "ssu_FRS", database = "ssu")

class Ui_NewEditUserScreen(object):
    def setupUi(self, NewEditUserScreen, mus, updater, userID):
        self.Form = NewEditUserScreen
        self.ManageUserScreen = mus
        self.Updater = updater
        self.UserID = userID

        NewEditUserScreen.setObjectName("NewEditUserScreen")
        NewEditUserScreen.resize(800, 480)
        font = QtGui.QFont()
        font.setPointSize(14)
        NewEditUserScreen.setFont(font)
        NewEditUserScreen.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.centralwidget = QtWidgets.QWidget(NewEditUserScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancel.setGeometry(QtCore.QRect(10, 420, 191, 51))
        self.btn_cancel.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.btn_cancel.setObjectName("btn_cancel")
        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(600, 420, 191, 51))
        self.btn_save.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.btn_save.setObjectName("btn_save")
        self.lbl_user = QtWidgets.QLabel(self.centralwidget)
        self.lbl_user.setGeometry(QtCore.QRect(0, 10, 801, 31))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_user.setFont(font)
        self.lbl_user.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_user.setObjectName("lbl_user")
        self.txb_password1 = QtWidgets.QLineEdit(self.centralwidget)
        self.txb_password1.setGeometry(QtCore.QRect(10, 220, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.txb_password1.setFont(font)
        self.txb_password1.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.txb_password1.setInputMask("")
        self.txb_password1.setText("")
        self.txb_password1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txb_password1.setAlignment(QtCore.Qt.AlignCenter)
        self.txb_password1.setObjectName("txb_password1")
        self.lbl_password2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_password2.setGeometry(QtCore.QRect(410, 190, 381, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_password2.setFont(font)
        self.lbl_password2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.lbl_password2.setObjectName("lbl_password2")
        self.lbl_errorPassword1 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_errorPassword1.setEnabled(True)
        self.lbl_errorPassword1.setGeometry(QtCore.QRect(10, 190, 381, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_errorPassword1.setFont(font)
        self.lbl_errorPassword1.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.lbl_errorPassword1.setScaledContents(False)
        self.lbl_errorPassword1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_errorPassword1.setObjectName("lbl_errorPassword1")
        self.lbl_password1 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_password1.setGeometry(QtCore.QRect(10, 190, 381, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_password1.setFont(font)
        self.lbl_password1.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.lbl_password1.setObjectName("lbl_password1")
        self.txb_password2 = QtWidgets.QLineEdit(self.centralwidget)
        self.txb_password2.setGeometry(QtCore.QRect(410, 220, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.txb_password2.setFont(font)
        self.txb_password2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.txb_password2.setInputMask("")
        self.txb_password2.setText("")
        self.txb_password2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txb_password2.setAlignment(QtCore.Qt.AlignCenter)
        self.txb_password2.setObjectName("txb_password2")
        self.lbl_errorPassword2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_errorPassword2.setEnabled(True)
        self.lbl_errorPassword2.setGeometry(QtCore.QRect(410, 190, 381, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_errorPassword2.setFont(font)
        self.lbl_errorPassword2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.lbl_errorPassword2.setScaledContents(False)
        self.lbl_errorPassword2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_errorPassword2.setObjectName("lbl_errorPassword2")
        self.lbl_username = QtWidgets.QLabel(self.centralwidget)
        self.lbl_username.setGeometry(QtCore.QRect(200, 50, 401, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_username.setFont(font)
        self.lbl_username.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.lbl_username.setObjectName("lbl_username")
        self.txb_username = QtWidgets.QLineEdit(self.centralwidget)
        self.txb_username.setGeometry(QtCore.QRect(200, 80, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.txb_username.setFont(font)
        self.txb_username.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.txb_username.setInputMask("")
        self.txb_username.setText("")
        self.txb_username.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.txb_username.setAlignment(QtCore.Qt.AlignCenter)
        self.txb_username.setObjectName("txb_username")
        self.lbl_errorUsername = QtWidgets.QLabel(self.centralwidget)
        self.lbl_errorUsername.setEnabled(True)
        self.lbl_errorUsername.setGeometry(QtCore.QRect(200, 50, 401, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_errorUsername.setFont(font)
        self.lbl_errorUsername.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.lbl_errorUsername.setScaledContents(False)
        self.lbl_errorUsername.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_errorUsername.setObjectName("lbl_errorUsername")        
        self.lbl_errorColor = QtWidgets.QLabel(self.centralwidget)
        self.lbl_errorColor.setEnabled(True)
        self.lbl_errorColor.setGeometry(QtCore.QRect(200, 260, 401, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_errorColor.setFont(font)
        self.lbl_errorColor.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.lbl_errorColor.setScaledContents(False)
        self.lbl_errorColor.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_errorColor.setObjectName("lbl_errorColor")
        self.btn_color = QtWidgets.QPushButton(self.centralwidget)
        self.btn_color.setGeometry(QtCore.QRect(200, 290, 141, 41))
        self.btn_color.setObjectName("btn_color")
        self.lbl_color = QtWidgets.QLabel(self.centralwidget)
        self.lbl_color.setGeometry(QtCore.QRect(200, 260, 401, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_color.setFont(font)
        self.lbl_color.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.lbl_color.setObjectName("lbl_color")
        self.pnl_color = QtWidgets.QFrame(self.centralwidget)
        self.pnl_color.setGeometry(QtCore.QRect(350, 290, 251, 41))
        self.pnl_color.setStyleSheet("background-color: rgb(255, 0, 0)")
        self.pnl_color.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pnl_color.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pnl_color.setObjectName("pnl_color")
        self.txb_email = QtWidgets.QLineEdit(self.centralwidget)
        self.txb_email.setGeometry(QtCore.QRect(200, 360, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.txb_email.setFont(font)
        self.txb_email.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.txb_email.setInputMask("")
        self.txb_email.setText("")
        self.txb_email.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.txb_email.setAlignment(QtCore.Qt.AlignCenter)
        self.txb_email.setObjectName("txb_email")
        self.lbl_email = QtWidgets.QLabel(self.centralwidget)
        self.lbl_email.setGeometry(QtCore.QRect(200, 330, 401, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_email.setFont(font)
        self.lbl_email.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.lbl_email.setObjectName("lbl_email")
        self.lbl_errorEmail = QtWidgets.QLabel(self.centralwidget)
        self.lbl_errorEmail.setEnabled(True)
        self.lbl_errorEmail.setGeometry(QtCore.QRect(200, 330, 401, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_errorEmail.setFont(font)
        self.lbl_errorEmail.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.lbl_errorEmail.setScaledContents(False)
        self.lbl_errorEmail.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_errorEmail.setObjectName("lbl_errorEmail")
        self.cmb_permissions = QtWidgets.QComboBox(self.centralwidget)
        self.cmb_permissions.setGeometry(QtCore.QRect(300, 150, 201, 41))
        self.cmb_permissions.setMaxVisibleItems(5)
        self.cmb_permissions.setObjectName("cmb_permissions")
        self.lbl_permission = QtWidgets.QLabel(self.centralwidget)
        self.lbl_permission.setGeometry(QtCore.QRect(300, 120, 201, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_permission.setFont(font)
        self.lbl_permission.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.lbl_permission.setObjectName("lbl_permission")
        self.chb_monthlyNotification = QtWidgets.QCheckBox(self.centralwidget)
        self.chb_monthlyNotification.setGeometry(QtCore.QRect(252, 405, 311, 41))
        self.chb_monthlyNotification.setAutoFillBackground(False)
        self.chb_monthlyNotification.setObjectName("chb_monthlyNotification")
        NewEditUserScreen.setCentralWidget(self.centralwidget)

        self.lbl_errorUsername.setVisible(False)
        self.lbl_errorPassword1.setVisible(False)
        self.lbl_errorPassword2.setVisible(False)
        self.lbl_errorPassword2.setVisible(False)
        self.lbl_errorColor.setVisible(False)
        self.lbl_errorEmail.setVisible(False)
        self.__selectedColor = "000000"

        self.retranslateUi(NewEditUserScreen)
        self.btn_cancel.clicked.connect(self.btn_cancel_clicked)
        self.btn_save.clicked.connect(self.btn_save_clicked)
        self.btn_color.clicked.connect(self.btn_color_clicked)
        QtCore.QMetaObject.connectSlotsByName(NewEditUserScreen)

    def retranslateUi(self, NewEditUserScreen):
        _translate = QtCore.QCoreApplication.translate
        NewEditUserScreen.setWindowTitle(_translate("NewEditUserScreen", "MainWindow"))
        self.btn_cancel.setText(_translate("NewEditUserScreen", "Cancel"))
        self.btn_save.setText(_translate("NewEditUserScreen", "Save"))

        if (self.UserID > 0):
            addon = "Edit"
        else:
            addon = "New"

        self.lbl_user.setText(_translate("NewEditUserScreen", addon + " User"))
        self.lbl_password2.setText(_translate("NewEditUserScreen", "Repeat password:"))
        self.lbl_errorPassword1.setText(_translate("NewEditUserScreen", "<span style=\"color:red;\">Must be between 8 and 16!"))
        self.lbl_password1.setText(_translate("NewEditUserScreen", "Password:"))
        self.lbl_errorPassword2.setText(_translate("NewEditUserScreen", "<html><head/><body><p><span style=\" color:#ff0000;\">Passwords not the same!</span></p></body></html>"))
        self.lbl_username.setText(_translate("NewEditUserScreen", "Username:"))
        self.lbl_errorUsername.setText(_translate("NewEditUserScreen", "<html><head/><body><p><span style=\" color:#ff0000;\">Username is taken!</span></p></body></html>"))
        self.lbl_errorColor.setText(_translate("NewEditUserScreen", "<html><head/><body><p><span style=\" color:#ff0000;\">Color colision!</span></p></body></html>"))
        self.btn_color.setText(_translate("NewEditUserScreen", "Select Color"))
        self.lbl_color.setText(_translate("NewEditUserScreen", "Color:"))
        self.lbl_email.setText(_translate("NewEditUserScreen", "Email:"))
        self.lbl_errorEmail.setText(_translate("NewEditUserScreen", "<html><head/><body><p><span style=\" color:#ff0000;\">Enter a valid email!</span></p></body></html>"))
        self.lbl_permission.setText(_translate("NewEditUserScreen", "Role:"))
        self.chb_monthlyNotification.setText(_translate("NewEditUserScreen", "Send a monthly inventory report"))

    def btn_cancel_clicked(self):
        self.ManageUserScreen.showFullScreen()
        self.Form.deleteLater()

    def btn_save_clicked(self):
        username = str(self.txb_username.text())
        permission = str(self.cmb_permissions.currentText())
        password1 = str(self.txb_password1.text())
        password2 = str(self.txb_password2.text())
        mothlyNot = self.chb_monthlyNotification.isChecked()
        email = str(self.txb_email.text())
    
        if (self.checkReadyToSave(username, password1, password2, email)):          
            if (mothlyNot):
                notAdd = "TRUE"
            else:
                notAdd = "FALSE"

            if (self.UserID == 0):        
                password = SSUFunctions.hashString(password1)
                MySQLDatabase.execDML("INSERT INTO users(username, password, color, email, monthlyNotification, userSignedIn, permissionID) " +
                                      "VALUES('" + username + "', '" + password + "', '" + self.__selectedColor + "', '" + email + "', " + notAdd + ", FALSE, " +
                                      "(SELECT ID FROM permissions WHERE permissionname='" + permission + "'))")

                self.Updater.getUserData(self.Updater.txb_search.text())
                self.Updater.setUserData()
                self.ManageUserScreen.showFullScreen()
                self.Form.deleteLater()
            else:
                if (password1 and password2):
                    password = SSUFunctions.hashString(password1)
                    passwordAddon = ", password='" + password + "'"
                else:
                    passwordAddon = ""

                MySQLDatabase.execDML("UPDATE users SET username='" + username + "'" + passwordAddon + ", color='" + self.__selectedColor + "', email='" + email + "', " + 
                                      "monthlyNotification=" + notAdd + ", permissionID=(SELECT ID FROM permissions WHERE permissionname='" + permission + "') " + 
                                      "WHERE ID=" + str(self.UserID))

                self.Updater.getUserData(self.Updater.txb_search.text())
                self.Updater.setUserData()
                self.ManageUserScreen.showFullScreen()
                self.Form.deleteLater()

    def btn_color_clicked(self):
        color = QColorDialog(self.Form).getColor().getRgb()
        color = color[ : 3]
        if (SSUFunctions.isColorOK(color)):
            self.lbl_errorColor.setVisible(False)
            self.__selectedColor = SSUFunctions.convertRGB2HEX(color)
            self.pnl_color.setStyleSheet("background-color: rgb(" + str(color[0]) + ", " + str(color[1]) + ", " + str(color[2]) + ")")
        else:
            self.lbl_errorColor.setVisible(True)
            if (self.UserID > 0):
                self.pnl_color.setStyleSheet("background-color: #" + str(self.__userData[1]))
                self.__selectedColor = str(self.__userData[1])
            else:
                self.__selectedColor = "000000"
                self.pnl_color.setStyleSheet("background-color: #FF0000")

    def checkReadyToSave(self, username, password1, password2, email):
        usernameError = True
        passwordError = True
        colorError = True
        emailError = True

        if (self.checkUsernameOK(username)):
            usernameError = False

        if (password1 and password2):
            if (self.checkPasswordOK(password1, password2)):
                passwordError = False
        else:
            passwordError = False

        if (self.checkColorSelected()):
            colorError = False

        if (self.checkEmailOK(email)):
            emailError = False

        return ((not usernameError) and (not passwordError) and (not colorError) and (not emailError))

    def checkUsernameOK(self, username):
        if (not SSUFunctions.isStringEmptyOrSpace(username)):
            if (self.UserID > 0):
                userAddon = " AND NOT ID=" + str(self.UserID)
            else:
                userAddon = ""

            users = MySQLDatabase.execSelect("SELECT ID FROM users WHERE username='" + username + "'" + userAddon)

            if (len(users) > 0):
                errorText = "<span style=\" color:#ff0000;\">Username is taken!"
            else:
                self.lbl_errorUsername.setVisible(False)
                return True
        else:
            errorText = "<span style=\" color:#ff0000;\">Enter Username!"

        self.lbl_errorUsername.setText(errorText)
        self.txb_username.setText(str(self.__userData[0]))
        self.lbl_errorUsername.setVisible(True)
        return False

    def checkPasswordOK(self, password1, password2):
        if ((not SSUFunctions.isStringEmptyOrSpace(password1)) and (not SSUFunctions.isStringEmptyOrSpace(password2))):
            self.lbl_errorPassword1.setVisible(False)
            self.lbl_errorPassword2.setVisible(False)
            if (SSUFunctions.isPasswordLengthOK(password1)):
                if (password1 == password2):                   
                    return True
                else:
                    self.txb_password2.setText("")
                    self.lbl_errorPassword2.setVisible(True)
            else:
                self.txb_password1.setText("")
                self.txb_password2.setText("")
                self.lbl_errorPassword1.setVisible(True)
        else:
            self.txb_password1.setText("")
            self.txb_password2.setText("")
            self.lbl_errorPassword1.setVisible(True)
            self.lbl_errorPassword2.setVisible(True)
        
        return False

    def checkColorSelected(self):
        if (self.__selectedColor == "000000"):
            self.lbl_errorColor.setText("<span style=\" color:#ff0000;\">Select a Color!")
            self.lbl_errorColor.setVisible(True)
            return False
        else:
            self.lbl_errorColor.setVisible(False)
            return True

    def checkEmailOK(self, email):
        if (not SSUFunctions.isStringEmptyOrSpace(email)):
            if (re.search('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', email)):
                self.lbl_errorEmail.setVisible(False)
                return True

        self.txb_email.setText("")
        self.lbl_errorEmail.setVisible(True)
        return False

    def onLoad_NewEditUserScreen(self):
        self.__possiblePermissions = MySQLDatabase.execSelect("SELECT perm.permissionName FROM permissions perm, " +
	                                                          "(SELECT * FROM permissions WHERE ID=" + str(User.User.PermID) + ") temp " +
	                                                          "WHERE ((perm.manageUsers = temp.manageUsers) OR (perm.manageUsers = 0)) " +
	                                                          "AND ((perm.storeItems = temp.storeItems) OR (perm.storeItems = 0)) " +
	                                                          "AND ((perm.withdrawItems = temp.withdrawItems) OR (perm.withdrawItems = 0)) " +
	                                                          "AND ((perm.deleteStorageSlot = temp.deleteStorageSlot) OR (perm.deleteStorageSlot = 0)) " +
	                                                          "AND ((perm.moveStorageSlot = temp.moveStorageSlot) OR (perm.moveStorageSlot = 0)) " +
	                                                          "AND ((perm.managePartitions = temp.managePartitions) OR (perm.managePartitions = 0)) " +
	                                                          "AND ((perm.correctQuantity = temp.correctQuantity) OR (perm.correctQuantity = 0)) " +
	                                                          "AND ((perm.createInventoryReport = temp.createInventoryReport) OR (perm.createInventoryReport = 0))")
        
        self.__possiblePermissions = self.__possiblePermissions[::-1]
        for permission in self.__possiblePermissions:
            item = str(permission[0])
            self.cmb_permissions.addItem(item)

        if (self.UserID > 0):
            self.__userData = MySQLDatabase.execSelect("SELECT us.username, us.color, us.email, us.monthlyNotification, perm.permissionname " + 
                                                   "FROM users us, permissions perm " +
                                                   "WHERE us.permissionID = perm.ID AND us.ID=" + str(self.UserID))[0]

            self.__Username = str(self.__userData[0])
            self.txb_username.setText(str(self.__userData[0]))           
            self.pnl_color.setStyleSheet("background-color: #" + str(self.__userData[1]))
            self.__selectedColor = str(self.__userData[1])
            self.txb_email.setText(str(self.__userData[2]))

            if (int(self.__userData[3]) > 0):
                self.chb_monthlyNotification.setChecked(True)

            index = self.cmb_permissions.findText(str(self.__userData[4]), QtCore.Qt.MatchFixedString)
            if(index >= 0):
                self.cmb_permissions.setCurrentIndex(index)