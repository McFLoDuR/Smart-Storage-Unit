from PyQt5 import QtCore, QtGui, QtWidgets
import db_connector

class User:
    Id = 0
    Username = "nobody"
    Color = "000000"
    Email = "@"
    MonthlyNotification = 0

    LoginScreen = None
    MainScreen = None

    PermID = 0
    PermName = "none"
    PermManageUsers = 0
    PermStoreItems = 0
    PermWithdrawItems = 0
    PermDeleteStorageSlot = 0
    PermMoveStorageSlot = 0
    PermManagePartitions = 0
    PermCorrectQuantity = 0
    PermCreateInventoryReport = 0

def setLoginScreen(lgs):
    User.LoginScreen = QtWidgets.QMainWindow()
    User.LoginScreen = lgs

def setMainScreen(ms):
    User.MainScreen = QtWidgets.QMainWindow()
    User.MainScreen = ms

def setUser(username):
    MySQLDatabase = db_connector.Database(host = "localhost", user = "ssu_db", password = "ssu_FRS", database = "ssu")
    userResult = MySQLDatabase.execSelect("SELECT * FROM users WHERE username='" + str(username) + "'")[0]
    permResult = MySQLDatabase.execSelect("SELECT * FROM permissions WHERE ID=(SELECT permissionID FROM users WHERE username='" + str(username) + "')")[0]

    User.Id = int(userResult[0])
    User.Username = str(username)
    User.Color = str(userResult[3])
    User.Email = str(userResult[4])
    User.MonthlyNotification = int(userResult[5])

    User.PermID = int(permResult[0])
    User.PermName = str(permResult[1])
    User.PermManageUsers = int(permResult[2])
    User.PermStoreItems = int(permResult[3])
    User.PermWithdrawItems = int(permResult[4])
    User.PermDeleteStorageSlot = int(permResult[5])
    User.PermMoveStorageSlot = int(permResult[6])
    User.PermManagePartitions = int(permResult[7])
    User.PermCorrectQuantity = int(permResult[8])
    User.PermCreateInventoryReport = int(permResult[9])

def unsetUser():
    User.Id = 0
    User.Username = "nobody"
    User.Color = "000000"
    User.Email = "@"
    User.MonthlyNotification = 0

    User.PermID = 0
    User.PermName = "none"
    User.PermManageUsers = 0
    User.PermStoreItems = 0
    User.PermWithdrawItems = 0
    User.PermDeleteStorageSlot = 0
    User.PermMoveStorageSlot = 0
    User.PermManagePartitions = 0
    User.PermCorrectQuantity = 0
    User.PermCreateInventoryReport = 0