from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import db_connector, User, re, SSUFunctions

MySQLDatabase = db_connector.Database(host = "localhost", user = "ssu_db", password = "ssu_FRS", database = "ssu")

class Ui_ManageUserScreen(object):
    def setupUi(self, ManageUserScreen, mainScreen):
        self.Form = ManageUserScreen
        self.MainScreen = mainScreen
        ManageUserScreen.setObjectName("ManageUserScreen")
        ManageUserScreen.resize(800, 480)
        font = QtGui.QFont()
        font.setPointSize(14)
        ManageUserScreen.setFont(font)
        ManageUserScreen.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.centralwidget = QtWidgets.QWidget(ManageUserScreen)
        self.centralwidget.setObjectName("centralwidget")

        #--------------------------------------------------------------------------------------------------------------------------------------

        self.lbl_username = QtWidgets.QLabel(self.centralwidget)
        self.lbl_username.setGeometry(QtCore.QRect(0, 10, 801, 31))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_username.setFont(font)
        self.lbl_username.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_username.setObjectName("lbl_username")
        self.lbl_permission = QtWidgets.QLabel(self.centralwidget)
        self.lbl_permission.setGeometry(QtCore.QRect(0, 50, 801, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lbl_permission.setFont(font)
        self.lbl_permission.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_permission.setObjectName("lbl_permission")

        #--------------------------------------------------------------------------------------------------------------------------------------

        self.lbl_passwordOld = QtWidgets.QLabel(self.centralwidget)
        self.lbl_passwordOld.setGeometry(QtCore.QRect(200, 80, 401, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_passwordOld.setFont(font)
        self.lbl_passwordOld.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.lbl_passwordOld.setObjectName("lbl_passwordOld")
        self.lbl_errorPasswordOld = QtWidgets.QLabel(self.centralwidget)
        self.lbl_errorPasswordOld.setEnabled(True)
        self.lbl_errorPasswordOld.setGeometry(QtCore.QRect(200, 80, 401, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_errorPasswordOld.setFont(font)
        self.lbl_errorPasswordOld.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.lbl_errorPasswordOld.setScaledContents(False)
        self.lbl_errorPasswordOld.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_errorPasswordOld.setObjectName("lbl_errorPasswordOld")
        self.lbl_errorPasswordOld.setVisible(False)
        self.txb_passwordOld = QtWidgets.QLineEdit(self.centralwidget)
        self.txb_passwordOld.setGeometry(QtCore.QRect(200, 110, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.txb_passwordOld.setFont(font)
        self.txb_passwordOld.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.txb_passwordOld.setInputMask("")
        self.txb_passwordOld.setText("")
        self.txb_passwordOld.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txb_passwordOld.setAlignment(QtCore.Qt.AlignCenter)
        self.txb_passwordOld.setObjectName("txb_passwordOld")

        #--------------------------------------------------------------------------------------------------------------------------------------

        self.lbl_passwordNew1 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_passwordNew1.setGeometry(QtCore.QRect(200, 150, 401, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_passwordNew1.setFont(font)
        self.lbl_passwordNew1.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.lbl_passwordNew1.setObjectName("lbl_passwordNew1")
        self.lbl_errorPasswordNew1 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_errorPasswordNew1.setEnabled(True)
        self.lbl_errorPasswordNew1.setGeometry(QtCore.QRect(200, 150, 401, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_errorPasswordNew1.setFont(font)
        self.lbl_errorPasswordNew1.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.lbl_errorPasswordNew1.setScaledContents(False)
        self.lbl_errorPasswordNew1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_errorPasswordNew1.setObjectName("lbl_errorPasswordNew1")
        self.lbl_errorPasswordNew1.setVisible(False)
        self.txb_passwordNew1 = QtWidgets.QLineEdit(self.centralwidget)
        self.txb_passwordNew1.setGeometry(QtCore.QRect(200, 180, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.txb_passwordNew1.setFont(font)
        self.txb_passwordNew1.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.txb_passwordNew1.setInputMask("")
        self.txb_passwordNew1.setText("")
        self.txb_passwordNew1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txb_passwordNew1.setAlignment(QtCore.Qt.AlignCenter)
        self.txb_passwordNew1.setObjectName("txb_passwordNew1")

        #--------------------------------------------------------------------------------------------------------------------------------------

        self.lbl_passwordNew2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_passwordNew2.setGeometry(QtCore.QRect(200, 220, 401, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_passwordNew2.setFont(font)
        self.lbl_passwordNew2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.lbl_passwordNew2.setObjectName("lbl_passwordNew2")
        self.lbl_errorPasswordNew2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_errorPasswordNew2.setEnabled(True)
        self.lbl_errorPasswordNew2.setGeometry(QtCore.QRect(200, 220, 401, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_errorPasswordNew2.setFont(font)
        self.lbl_errorPasswordNew2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.lbl_errorPasswordNew2.setScaledContents(False)
        self.lbl_errorPasswordNew2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_errorPasswordNew2.setObjectName("lbl_errorPasswordNew2")
        self.lbl_errorPasswordNew2.setVisible(False)
        self.txb_passwordNew2 = QtWidgets.QLineEdit(self.centralwidget)
        self.txb_passwordNew2.setGeometry(QtCore.QRect(200, 250, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.txb_passwordNew2.setFont(font)
        self.txb_passwordNew2.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.txb_passwordNew2.setInputMask("")
        self.txb_passwordNew2.setText("")
        self.txb_passwordNew2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txb_passwordNew2.setAlignment(QtCore.Qt.AlignCenter)
        self.txb_passwordNew2.setObjectName("txb_passwordNew2")

        #--------------------------------------------------------------------------------------------------------------------------------------

        self.lbl_color = QtWidgets.QLabel(self.centralwidget)
        self.lbl_color.setGeometry(QtCore.QRect(200, 290, 401, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_color.setFont(font)
        self.lbl_color.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.lbl_color.setObjectName("lbl_color")
        self.lbl_errorColor = QtWidgets.QLabel(self.centralwidget)
        self.lbl_errorColor.setEnabled(True)
        self.lbl_errorColor.setGeometry(QtCore.QRect(200, 290, 401, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_errorColor.setFont(font)
        self.lbl_errorColor.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.lbl_errorColor.setScaledContents(False)
        self.lbl_errorColor.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_errorColor.setObjectName("lbl_errorColor")
        self.lbl_errorColor.setVisible(False)
        self.btn_color = QtWidgets.QPushButton(self.centralwidget)
        self.btn_color.setGeometry(QtCore.QRect(200, 320, 151, 41))
        self.btn_color.setObjectName("btn_color")
        self.pnl_color = QtWidgets.QFrame(self.centralwidget)
        self.pnl_color.setGeometry(QtCore.QRect(360, 320, 241, 41))
        self.pnl_color.setStyleSheet("background-color: #" + str(User.User.Color))
        self.__newColor = str(User.User.Color)
        self.pnl_color.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.pnl_color.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pnl_color.setObjectName("pnl_color")

        #--------------------------------------------------------------------------------------------------------------------------------------

        self.lbl_email = QtWidgets.QLabel(self.centralwidget)
        self.lbl_email.setGeometry(QtCore.QRect(200, 360, 401, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_email.setFont(font)
        self.lbl_email.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.lbl_email.setObjectName("lbl_email")
        self.lbl_errorEmail = QtWidgets.QLabel(self.centralwidget)
        self.lbl_errorEmail.setEnabled(True)
        self.lbl_errorEmail.setGeometry(QtCore.QRect(200, 360, 401, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_errorEmail.setFont(font)
        self.lbl_errorEmail.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.lbl_errorEmail.setScaledContents(False)
        self.lbl_errorEmail.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lbl_errorEmail.setObjectName("lbl_errorEmail")
        self.lbl_errorEmail.setVisible(False)
        self.txb_email = QtWidgets.QLineEdit(self.centralwidget)
        self.txb_email.setGeometry(QtCore.QRect(200, 390, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.txb_email.setFont(font)
        self.txb_email.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.txb_email.setInputMask("")
        self.txb_email.setText("")
        self.txb_email.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.txb_email.setAlignment(QtCore.Qt.AlignCenter)
        self.txb_email.setObjectName("txb_email")
        self.txb_email.setText(User.User.Email)

        #--------------------------------------------------------------------------------------------------------------------------------------

        self.chb_monthlyNotification = QtWidgets.QCheckBox(self.centralwidget)
        self.chb_monthlyNotification.setGeometry(QtCore.QRect(235, 435, 401, 41))
        self.chb_monthlyNotification.setAutoFillBackground(False)

        if (User.User.MonthlyNotification > 0):
            self.chb_monthlyNotification.setChecked(True)

        self.chb_monthlyNotification.setObjectName("chb_monthlyNotification")

        #--------------------------------------------------------------------------------------------------------------------------------------

        self.btn_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.btn_cancel.setGeometry(QtCore.QRect(10, 420, 181, 51))
        self.btn_cancel.setObjectName("btn_cancel")

        self.btn_save = QtWidgets.QPushButton(self.centralwidget)
        self.btn_save.setGeometry(QtCore.QRect(610, 420, 181, 51))
        self.btn_save.setObjectName("btn_save")

        #--------------------------------------------------------------------------------------------------------------------------------------

        ManageUserScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(ManageUserScreen)
        self.btn_save.clicked.connect(self.btn_save_clicked)
        self.btn_cancel.clicked.connect(self.btn_cancel_clicked)
        self.btn_color.clicked.connect(self.pnl_color_clicked)
        QtCore.QMetaObject.connectSlotsByName(ManageUserScreen)

    def retranslateUi(self, ManageUserScreen):
        _translate = QtCore.QCoreApplication.translate
        ManageUserScreen.setWindowTitle(_translate("ManageUserScreen", "MainWindow"))
        self.lbl_passwordOld.setText(_translate("ManageUserScreen", "Old password:"))
        self.lbl_email.setText(_translate("ManageUserScreen", "Email:"))
        self.chb_monthlyNotification.setText(_translate("ManageUserScreen", "Send me a monthly inventory report"))
        self.btn_cancel.setText(_translate("ManageUserScreen", "Cancel"))
        self.lbl_passwordNew1.setText(_translate("ManageUserScreen", "New password:"))
        self.lbl_username.setText(_translate("ManageUserScreen", "Username: " + User.User.Username))
        self.lbl_permission.setText(_translate("ManageUserScreen", "Role: " + User.User.PermName))
        self.btn_save.setText(_translate("ManageUserScreen", "Save"))
        self.lbl_passwordNew2.setText(_translate("ManageUserScreen", "Repeat new password:"))
        self.lbl_errorEmail.setText(_translate("ManageUserScreen", "<span style=\"color:red;\">Enter a valid email!"))
        self.lbl_errorPasswordNew2.setText(_translate("ManageUserScreen", "<span style=\"color:red;\">Passwords to not match!"))
        self.lbl_errorPasswordNew1.setText(_translate("ManageUserScreen", "<span style=\"color:red;\">Must be between 8 and 16!"))
        self.lbl_errorPasswordOld.setText(_translate("ManageUserScreen", "<span style=\"color:red;\">Wrong password!"))
        self.btn_color.setText(_translate("ManageUserScreen", "Select Color"))
        self.lbl_errorColor.setText(_translate("ManageUserScreen", "<html><head/><body><p><span style=\" color:#ff0000;\">Color collision!</span></p></body></html>"))
        self.lbl_color.setText(_translate("ManageUserScreen", "New Color:"))
    
    def pnl_color_clicked(self):
        color = QColorDialog(self.Form).getColor().getRgb()
        color = color[ : 3]
        if (SSUFunctions.isColorOK(color, False)):
            self.lbl_errorColor.setVisible(False)
            self.__newColor = SSUFunctions.convertRGB2HEX(color)
            self.pnl_color.setStyleSheet("background-color: rgb(" + str(color[0]) + ", " + str(color[1]) + ", " + str(color[2]) + ")")
        else:
            self.lbl_errorColor.setVisible(True)
            self.__newColor = str(User.User.Color)
            self.pnl_color.setStyleSheet("background-color: #" + str(User.User.Color))

    def btn_save_clicked(self):
        oldPassword = self.txb_passwordOld.text()
        newPassword1 = self.txb_passwordNew1.text()
        newPassword2 = self.txb_passwordNew2.text()
        newEmail = self.txb_email.text()
        monthlyNotification = self.chb_monthlyNotification.isChecked()

        if (self.checkReadyToSave(oldPassword, newPassword1, newPassword2, newEmail)):
            if (newPassword1 and newPassword2):
                password = SSUFunctions.hashString(newPassword1)
                passwordAddon = ", password='" + password + "'"
            else:
                passwordAddon = ""

            if (newEmail):
                emailAddon = ", email='" + str(newEmail) + "'"
            else:
                emailAddon = ""

            if (monthlyNotification):
                monthNot = "TRUE"
            else:
                monthNot = "FALSE"
            
            MySQLDatabase.execDML("UPDATE users SET monthlyNotification=" + monthNot + passwordAddon + emailAddon + ", color='" + self.__newColor + "'" + 
                                  " WHERE ID=" + str(User.User.Id))

            self.backToMainScreen()


    def checkReadyToSave(self, oldPassword, passwordNew1, passwordNew2, email):
        oldPasswordError = True
        newPasswordError = True
        emailError = True

        if (self.checkOldPasswordOK(oldPassword)):
            oldPasswordError = False

        if (self.checkNewPasswordOK(passwordNew1, passwordNew2)):
            newPasswordError = False
        
        if (self.checkEmailOK(email)):
            emailError = False

        return ((not oldPasswordError) and (not emailError) and (not newPasswordError))

    def checkOldPasswordOK(self, oldPassword):
        if (oldPassword):
            password = SSUFunctions.hashString(oldPassword)

            result = MySQLDatabase.execSelect("SELECT * FROM users WHERE username='" + User.User.Username + "' AND password='" + password + "'")

            if (len(result) == 1):
                self.lbl_errorPasswordOld.setVisible(False)
                return True
            else:
                self.lbl_errorPasswordOld.setText("<span style=\"color:red;\">Wrong password!")
        else:
            self.lbl_errorPasswordOld.setText("<span style=\"color:red;\">Enter old password!")
        
        self.txb_passwordOld.setText("")
        self.lbl_errorPasswordOld.setVisible(True)
        return False

    def checkNewPasswordOK(self, passwordNew1, passwordNew2):
        if ((not SSUFunctions.isStringEmptyOrSpace(passwordNew1)) or (not SSUFunctions.isStringEmptyOrSpace(passwordNew2))):
            self.lbl_errorPasswordNew1.setVisible(False)
            self.lbl_errorPasswordNew2.setVisible(False)
            if (SSUFunctions.isPasswordLengthOK(passwordNew1)):
                if (passwordNew1 == passwordNew2):
                    return True
                else:
                    self.txb_passwordNew2.setText("")
                    self.lbl_errorPasswordNew2.setVisible(True)
                    return False
            else:
                self.txb_passwordNew1.setText("")
                self.txb_passwordNew2.setText("")
                self.lbl_errorPasswordNew1.setVisible(True)
                return False

        self.lbl_errorPasswordNew1.setVisible(False)
        self.lbl_errorPasswordNew2.setVisible(False)
        return True
        
    def checkEmailOK(self, email):
        if (not SSUFunctions.isStringEmptyOrSpace(email)):            
            if (re.search('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', email)):
                self.lbl_errorEmail.setVisible(False)
                return True
            else:
                self.txb_email.setText("")
                self.lbl_errorEmail.setVisible(True)
                return False
        else:
            self.lbl_errorEmail.setVisible(False)
            return True
        
    def btn_cancel_clicked(self):
        self.backToMainScreen()

    def backToMainScreen(self):
        User.setUser(User.User.Username)
        User.User.MainScreen.showFullScreen()
        self.MainScreen.dh.updateDataTable()
        self.Form.deleteLater()