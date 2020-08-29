from PyQt5 import QtCore, QtGui, QtWidgets
import MainScreen
import db_connector
import User
import SSUFunctions

MySQLDatabase = db_connector.Database(host = "localhost", user = "ssu_db", password = "ssu_FRS", database = "ssu")

class Ui_LoginScreen(object):
    # auto generated code from the pyqt5 designer
    def setupUi(self, LoginScreen):  
        self.Form = LoginScreen
        LoginScreen.setObjectName("LoginScreen")
        LoginScreen.resize(800, 480)
        LoginScreen.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.loginPage = QtWidgets.QWidget(LoginScreen)
        self.loginPage.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.loginPage.setObjectName("loginPage")
        self.lbl_username = QtWidgets.QLabel(self.loginPage)
        self.lbl_username.setGeometry(QtCore.QRect(230, 240, 341, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_username.setFont(font)
        self.lbl_username.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.lbl_username.setObjectName("lbl_username")
        self.btn_login = QtWidgets.QPushButton(self.loginPage)
        self.btn_login.setGeometry(QtCore.QRect(250, 400, 301, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btn_login.setFont(font)
        self.btn_login.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.btn_login.setObjectName("btn_login")
        self.lbl_password = QtWidgets.QLabel(self.loginPage)
        self.lbl_password.setGeometry(QtCore.QRect(230, 310, 341, 16))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_password.setFont(font)
        self.lbl_password.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.lbl_password.setObjectName("lbl_password")
        self.txb_password = QtWidgets.QLineEdit(self.loginPage)
        self.txb_password.setGeometry(QtCore.QRect(230, 330, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.txb_password.setFont(font)
        self.txb_password.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.txb_password.setInputMask("")
        self.txb_password.setText("")
        self.txb_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txb_password.setAlignment(QtCore.Qt.AlignCenter)
        self.txb_password.setObjectName("txb_password")
        self.pcb_logo = QtWidgets.QLabel(self.loginPage)
        self.pcb_logo.setGeometry(QtCore.QRect(300, 30, 201, 201))
        self.pcb_logo.setText("")
        self.pcb_logo.setPixmap(QtGui.QPixmap("images/icon.PNG"))
        self.pcb_logo.setScaledContents(True)
        self.pcb_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.pcb_logo.setObjectName("pcb_logo")
        self.txb_username = QtWidgets.QLineEdit(self.loginPage)
        self.txb_username.setGeometry(QtCore.QRect(230, 260, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.txb_username.setFont(font)
        self.txb_username.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.txb_username.setText("")
        self.txb_username.setAlignment(QtCore.Qt.AlignCenter)
        self.txb_username.setObjectName("txb_username")
        self.lbl_error = QtWidgets.QLabel(self.loginPage)
        self.lbl_error.setEnabled(True)
        self.lbl_error.setGeometry(QtCore.QRect(230, 370, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_error.setFont(font)
        self.lbl_error.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.lbl_error.setScaledContents(False)
        self.lbl_error.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_error.setObjectName("lbl_error")
        self.lbl_error.setVisible(False)
        LoginScreen.setCentralWidget(self.loginPage)

        self.retranslateUi(LoginScreen)
        self.btn_login.clicked.connect(self.btn_login_clicked)
        QtCore.QMetaObject.connectSlotsByName(LoginScreen)

    def retranslateUi(self, LoginScreen):
        _translate = QtCore.QCoreApplication.translate
        LoginScreen.setWindowTitle(_translate("LoginScreen", "MainWindow"))
        self.lbl_username.setText(_translate("LoginScreen", "Username:"))
        self.btn_login.setText(_translate("LoginScreen", "Log in"))
        self.lbl_password.setText(_translate("LoginScreen", "Password:"))
        self.lbl_error.setText(_translate("LoginScreen", "<span style=\"color:red;\">Username or password incorrect!"))

    #--------------------------------------------------------------------------------------------------------------------------
    # self written code

    # open the main screen
    def openMainScreen(self):
        self.ms = QtWidgets.QMainWindow()
        self.ui = MainScreen.Ui_MainScreen()
        self.ui.setupUi(self.ms)
        self.ms.showFullScreen()
        User.User.LoginScreen.hide()
        t = QtCore.QTimer()
        t.singleShot(0,self.ui.onLoad_MainScreen)
        
    def onLoad_LoginScreen(self):
        User.User.LoginScreen = self.Form

    # login button clicked action
    def btn_login_clicked(self):
        # check if username and password boxes aren't empty
        if (self.txb_username.text() and self.txb_password.text()):
            # search in the database for the user and check if his password is correct
            username = str(self.txb_username.text())
            password = str(self.txb_password.text())
            password = SSUFunctions.hashString(password)
            
            resultSQL = MySQLDatabase.execSelect("SELECT * FROM users WHERE username='" + username +"' AND password='" + password + "'")
            # if there is 1 result everything is fine
            if (len(resultSQL) == 1):
                # check if the user isn't already logged in
                if(int(resultSQL[0][6]) == 0):
                    self.txb_username.setText("")
                    self.txb_password.setText("")
                    self.lbl_error.setVisible(False)
                    User.setUser(username)
                    # MySQLDatabase.execDML("UPDATE users SET userSignedIn=1 WHERE ID=" + str(User.User.Id))

                    # go on to the main screen
                    self.openMainScreen()
                # if he is already logged 
                else:
                    self.lbl_error.setText("<span style=\"color:red;\">User is already logged in!")
                    self.lbl_error.setVisible(True)
            # otherwise the username or password is incorrect
            else:
                self.txb_username.setText("")
                self.txb_password.setText("")
                self.lbl_error.setText("<span style=\"color:red;\">Username or password wrong!")
                self.lbl_error.setVisible(True)