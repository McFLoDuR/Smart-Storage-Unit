from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import ManageUserScreen, ManageUserPermissionScreen, StoreItemScreen, WithdrawItemScreen, CreateInventoryReportScreen
import CorrectQuantityScreen, MoveRemoveStorageSlotScreen, ManageItemsScreen
import User, db_connector, DataHandler

MySQLDatabase = db_connector.Database(host = "localhost", user = "ssu_db", password = "ssu_FRS", database = "ssu")

class Ui_MainScreen(object):
    # auto generated code from the pyqt5 designer
    def setupUi(self, MainScreen):
        User.User.MainScreen = MainScreen
        MainScreen.setObjectName("MainScreen")
        MainScreen.resize(800, 480)
        font = QtGui.QFont()
        font.setPointSize(14)
        MainScreen.setFont(font)
        MainScreen.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.centralwidget = QtWidgets.QWidget(MainScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_screenTitle = QtWidgets.QLabel(self.centralwidget)
        self.lbl_screenTitle.setGeometry(QtCore.QRect(220, -10, 580, 50))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_screenTitle.setFont(font)
        self.lbl_screenTitle.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.lbl_screenTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_screenTitle.setObjectName("lbl_screenTitle")
        self.txb_search = QtWidgets.QLineEdit(self.centralwidget)
        self.txb_search.setGeometry(QtCore.QRect(220, 50, 461, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.txb_search.setFont(font)
        self.txb_search.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.txb_search.setText("")
        self.txb_search.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.txb_search.setObjectName("txb_search")
        self.btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_search.setGeometry(QtCore.QRect(680, 50, 111, 41))
        self.btn_search.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.btn_search.setObjectName("btn_search")
        self.dtv_items = QtWidgets.QTableWidget(self.centralwidget)
        self.dtv_items.setGeometry(QtCore.QRect(220, 100, 571, 341))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.dtv_items.setFont(font)
        self.dtv_items.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.dtv_items.setObjectName("dtv_items")
        self.dtv_items.setColumnCount(0)
        self.dtv_items.setRowCount(0)
        self.pcb_logo = QtWidgets.QLabel(self.centralwidget)
        self.pcb_logo.setGeometry(QtCore.QRect(40, 10, 141, 141))
        self.pcb_logo.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.pcb_logo.setText("")
        self.pcb_logo.setPixmap(QtGui.QPixmap("images/icon.PNG"))
        self.pcb_logo.setScaledContents(True)
        self.pcb_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.pcb_logo.setObjectName("pcb_logo")
        self.lbl_itemData = QtWidgets.QLabel(self.centralwidget)
        self.lbl_itemData.setGeometry(QtCore.QRect(10, 160, 201, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_itemData.setFont(font)
        self.lbl_itemData.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.lbl_itemData.setObjectName("lbl_itemData")
        self.liv_itemData = QtWidgets.QListWidget(self.centralwidget)
        self.liv_itemData.setGeometry(QtCore.QRect(10, 190, 201, 251))
        self.liv_itemData.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
        self.liv_itemData.setObjectName("liv_itemData")
        MainScreen.setCentralWidget(self.centralwidget)
        self.addMenuBar(MainScreen)

        self.dh = DataHandler.DataHandlerMainScreen(dtv=self.dtv_items, liv=self.liv_itemData, txb=self.txb_search)
        self.retranslateUi(MainScreen)
        self.act_exit.triggered.connect(self.btn_exit_clicked)
        self.btn_search.clicked.connect(self.btn_search_clicked)
        self.dtv_items.itemSelectionChanged.connect(self.dh.rowSelected)
        self.act_manageProfile.triggered.connect(self.openManageProfileScreen)        

        self.addActions()            
        QtCore.QMetaObject.connectSlotsByName(MainScreen)        

    def retranslateUi(self, MainScreen):
        _translate = QtCore.QCoreApplication.translate
        MainScreen.setWindowTitle(_translate("MainScreen", "MainWindow"))
        self.btn_search.setText(_translate("MainScreen", "Search"))        
        self.lbl_itemData.setText(_translate("MainScreen", "Item Data:"))
        self.lbl_screenTitle.setText(_translate("MainScreen", "Main Menu"))
        self.translateMenuBar(_translate)
    
    #--------------------------------------------------------------------------------------------------------------------------
    # self written code

    # add the menubar to the window
    def addMenuBar(self, screen):
        self.menubar = QtWidgets.QMenuBar(screen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName("menubar")

        self.menu_options = QtWidgets.QMenu(self.menubar)
        self.menu_options.setObjectName("menu_options")

        if ((User.User.PermStoreItems > 0) or (User.User.PermWithdrawItems > 0) or (User.User.PermCorrectQuantity > 0)):
            self.menu_manageItems = QtWidgets.QMenu(self.menu_options)
            font = QtGui.QFont()
            font.setPointSize(14)
            self.menu_manageItems.setFont(font)
            self.menu_manageItems.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Austria))
            self.menu_manageItems.setObjectName("menu_manageItems")

        if (User.User.PermManageUsers > 0):
            self.menu_manageUsers = QtWidgets.QMenu(self.menu_options)
            font = QtGui.QFont()
            font.setPointSize(14)
            self.menu_manageUsers.setFont(font)
            self.menu_manageUsers.setTearOffEnabled(False)
            self.menu_manageUsers.setObjectName("menu_manageUsers")

        if ((User.User.PermMoveStorageSlot > 0) or (User.User.PermDeleteStorageSlot > 0) or (User.User.PermManagePartitions > 0)):
            self.menu_manageStorage = QtWidgets.QMenu(self.menu_options)
            font = QtGui.QFont()
            font.setPointSize(14)
            self.menu_manageStorage.setFont(font)
            self.menu_manageStorage.setObjectName("menu_manageStorage")

        self.menu_logout = QtWidgets.QMenu(self.menubar)
        self.menu_logout.setObjectName("menu_logout")
        screen.setMenuBar(self.menubar)

        self.act_manageProfile = QtWidgets.QAction(screen)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.act_manageProfile.setFont(font)
        self.act_manageProfile.setObjectName("act_manageProfile")

        if (User.User.PermStoreItems > 0):
            self.act_storeItems = QtWidgets.QAction(screen)
            font = QtGui.QFont()
            font.setPointSize(12)
            self.act_storeItems.setFont(font)
            self.act_storeItems.setObjectName("act_storeItems")
            self.act_manageItems = QtWidgets.QAction(screen)
            font = QtGui.QFont()
            font.setPointSize(12)
            self.act_manageItems.setFont(font)
            self.act_manageItems.setObjectName("act_manageItems")

        if (User.User.PermWithdrawItems > 0):
            self.act_withdrawItems = QtWidgets.QAction(screen)
            font = QtGui.QFont()
            font.setPointSize(12)
            self.act_withdrawItems.setFont(font)
            self.act_withdrawItems.setObjectName("act_withdrawItems")

        if (User.User.PermManageUsers > 0):
            self.act_manageUser = QtWidgets.QAction(screen)
            font = QtGui.QFont()
            font.setPointSize(12)
            self.act_manageUser.setFont(font)
            self.act_manageUser.setObjectName("act_manageUser")
            self.act_managePermissions = QtWidgets.QAction(screen)
            font = QtGui.QFont()
            font.setPointSize(12)
            self.act_managePermissions.setFont(font)
            self.act_managePermissions.setObjectName("act_managePermissions")

        self.act_exit = QtWidgets.QAction(screen)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.act_exit.setFont(font)
        self.act_exit.setObjectName("act_exit")

        if (User.User.PermMoveStorageSlot > 0):
            self.act_moveStorageSlot = QtWidgets.QAction(screen)
            font = QtGui.QFont()
            font.setPointSize(12)
            self.act_moveStorageSlot.setFont(font)
            self.act_moveStorageSlot.setObjectName("act_moveStorageSlot")
        
        if (User.User.PermCreateInventoryReport > 0):
            self.act_createInventoryReport = QtWidgets.QAction(screen)
            font = QtGui.QFont()
            font.setPointSize(12)
            self.act_createInventoryReport.setFont(font)
            self.act_createInventoryReport.setObjectName("act_createInventoryReport")

        if (User.User.PermCorrectQuantity > 0):
            self.act_setQuantity = QtWidgets.QAction(screen)
            font = QtGui.QFont()
            font.setPointSize(12)
            self.act_setQuantity.setFont(font)
            self.act_setQuantity.setObjectName("act_setQuantity")


        #if (User.User.PermManagePartitions > 0):
            #self.act_changeParititions = QtWidgets.QAction(screen)
            #font = QtGui.QFont()
            #font.setPointSize(12)
            #self.act_changeParititions.setFont(font)
            #self.act_changeParititions.setObjectName("act_changeParititions")

        if (User.User.PermDeleteStorageSlot > 0):
            self.act_removeStorageSlot = QtWidgets.QAction(screen)
            font = QtGui.QFont()
            font.setPointSize(12)
            self.act_removeStorageSlot.setFont(font)
            self.act_removeStorageSlot.setObjectName("act_removeStorageSlot")

        setSepartor = False
        if (User.User.PermStoreItems > 0):
            self.menu_manageItems.addAction(self.act_storeItems)
            self.menu_manageItems.addAction(self.act_manageItems)
            setSepartor = True
        if (User.User.PermWithdrawItems > 0):
            self.menu_manageItems.addAction(self.act_withdrawItems)
            setSepartor = True
        if (User.User.PermStoreItems > 0):
            self.menu_manageItems.addAction(self.act_manageItems)
        if (setSepartor):
            self.menu_manageItems.addSeparator()
            setSepartor = False
        if (User.User.PermCorrectQuantity > 0):
            self.menu_manageItems.addAction(self.act_setQuantity)

        if (User.User.PermManageUsers > 0):
            self.menu_manageUsers.addAction(self.act_manageUser)
            self.menu_manageUsers.addSeparator()
            self.menu_manageUsers.addAction(self.act_managePermissions)

        if (User.User.PermMoveStorageSlot > 0):
            self.menu_manageStorage.addAction(self.act_moveStorageSlot)
            #setSepartor = True
        if (User.User.PermDeleteStorageSlot > 0):
            self.menu_manageStorage.addAction(self.act_removeStorageSlot)
            #setSepartor = True
        #if (setSepartor):
            #self.menu_manageStorage.addSeparator()
            #setSepartor = False

        #if (User.User.PermManagePartitions > 0):
            #self.menu_manageStorage.addAction(self.act_changeParititions)
        
        self.menu_options.addAction(self.act_manageProfile)

        if ((User.User.PermManageUsers > 0) or (User.User.PermStoreItems > 0) or (User.User.PermWithdrawItems > 0) or (User.User.PermDeleteStorageSlot > 0) or (User.User.PermMoveStorageSlot > 0) or (User.User.PermManagePartitions > 0) or (User.User.PermCorrectQuantity > 0) or (User.User.PermCreateInventoryReport > 0)):
            self.menu_options.addSeparator()

        if ((User.User.PermStoreItems > 0) or (User.User.PermWithdrawItems > 0) or (User.User.PermCorrectQuantity > 0)):
            self.menu_options.addAction(self.menu_manageItems.menuAction())
            setSepartor = True
        if ((User.User.PermMoveStorageSlot > 0) or (User.User.PermDeleteStorageSlot > 0) or (User.User.PermManagePartitions > 0)):
            self.menu_options.addAction(self.menu_manageStorage.menuAction())
            setSepartor = True
        if (setSepartor):
            self.menu_options.addSeparator()
            setSepartor = False

        if (User.User.PermManageUsers > 0):
            self.menu_options.addAction(self.menu_manageUsers.menuAction())
            self.menu_options.addSeparator()

        if (User.User.PermCreateInventoryReport > 0):
            self.menu_options.addAction(self.act_createInventoryReport)

        self.menu_logout.addAction(self.act_exit)
        self.menubar.addAction(self.menu_options.menuAction())
        self.menubar.addAction(self.menu_logout.menuAction())
    # translate the menubar
    def translateMenuBar(self, _translate):
        self.menu_options.setTitle(_translate("MainScreen", "Options"))

        if ((User.User.PermStoreItems > 0) or (User.User.PermWithdrawItems > 0) or (User.User.PermCorrectQuantity > 0)):
            self.menu_manageItems.setTitle(_translate("MainScreen", "Manage Items"))
        if (User.User.PermManageUsers > 0):
            self.menu_manageUsers.setTitle(_translate("MainScreen", "Manage Users"))
        if ((User.User.PermMoveStorageSlot > 0) or (User.User.PermDeleteStorageSlot > 0) or (User.User.PermManagePartitions > 0)):
            self.menu_manageStorage.setTitle(_translate("MainScreen", "Manage Storage"))

        self.menu_logout.setTitle(_translate("MainScreen", "Log out"))
        self.act_manageProfile.setText(_translate("MainScreen", "Manage Profile"))

        if (User.User.PermStoreItems > 0):
            self.act_storeItems.setText(_translate("MainScreen", "Store Items"))
            self.act_manageItems.setText(_translate("MainScreen", "Manage Items"))
        if (User.User.PermWithdrawItems > 0):
            self.act_withdrawItems.setText(_translate("MainScreen", "Withdraw Items"))
        if (User.User.PermManageUsers > 0):
            self.act_manageUser.setText(_translate("MainScreen", "Manage Users"))
            self.act_managePermissions.setText(_translate("MainScreen", "Manage Roles"))

        self.act_exit.setText(_translate("MainScreen", "Exit"))

        if (User.User.PermMoveStorageSlot > 0):
            self.act_moveStorageSlot.setText(_translate("MainScreen", "Move Storage Slot"))
        if (User.User.PermCreateInventoryReport > 0):
            self.act_createInventoryReport.setText(_translate("MainScreen", "Create Inventory Report"))
        if (User.User.PermCorrectQuantity > 0):
            self.act_setQuantity.setText(_translate("MainScreen", "Set Quantity"))
        #if (User.User.PermManagePartitions > 0):
            #self.act_changeParititions.setText(_translate("MainScreen", "Change Partitions"))
        if (User.User.PermDeleteStorageSlot > 0):
            self.act_removeStorageSlot.setText(_translate("MainScreen", "Remove Storage Slot"))

    def btn_storeItems_clicked(self):
        self.openStoreItemScreen()

    def btn_manageItems_clicked(self):
        self.openManageItemScreen()

    def btn_withdrawItems_clicked(self):
        self.openWithdrawItemScreen()

    def btn_setQuantity_clicked(self):
        self.openCorrectQuantityScreen()

    def btn_manageUser_clicked(self):
        self.openManageUserPermissionScreen(True)

    def btn_managePermissions_clicked(self):
        self.openManageUserPermissionScreen(False)

    def btn_createInventoryReport_clicked(self):
        self.cirs = QtWidgets.QMainWindow()
        self.ui = CreateInventoryReportScreen.Ui_CreateInventoryReportScreen()
        self.ui.setupUi(self.cirs)
        self.cirs.showFullScreen()
        t = QtCore.QTimer(User.User.MainScreen)
        t.singleShot(0, self.ui.onLoad_CreateInventoryReportScreen)

    def btn_moveStorageSlot_clicked(self):
        self.openMoveRemoveStorageSlotScreen(False)

    def btn_removeStorageSlot_clicked(self):
        self.openMoveRemoveStorageSlotScreen(True)

    def openStoreItemScreen(self):
        self.sis = QtWidgets.QMainWindow()
        self.ui = StoreItemScreen.Ui_StoreItemScreen()
        self.ui.setupUi(self.sis, self)
        self.sis.showFullScreen()
        User.User.MainScreen.hide()
        t = QtCore.QTimer(User.User.MainScreen)
        t.singleShot(0, self.ui.onLoad_StoreItemScreen)

    def openManageItemScreen(self):
        self.mis = QtWidgets.QMainWindow()
        self.ui = ManageItemsScreen.Ui_ManageItemsScreen()
        self.ui.setupUi(self.mis, self)
        self.mis.showFullScreen()
        User.User.MainScreen.hide()
        t = QtCore.QTimer(User.User.MainScreen)
        t.singleShot(0, self.ui.onLoad_ManageUserPermissionScreen)

    def openWithdrawItemScreen(self):
        self.wis = QtWidgets.QMainWindow()
        self.ui = WithdrawItemScreen.Ui_WithdrawItemScreen()
        self.ui.setupUi(self.wis, self)
        self.wis.showFullScreen()
        User.User.MainScreen.hide()
        t = QtCore.QTimer(User.User.MainScreen)
        t.singleShot(0, self.ui.onLoad_WithdrawItemScreen)

    def openCorrectQuantityScreen(self):
        self.cqs = QtWidgets.QMainWindow()
        self.ui = CorrectQuantityScreen.Ui_CorrectQuantityScreen()
        self.ui.setupUi(self.cqs, self)
        self.cqs.showFullScreen()
        User.User.MainScreen.hide()
        t = QtCore.QTimer(User.User.MainScreen)
        t.singleShot(0, self.ui.onLoad_CorrectQuantityScreen)

    def openMoveRemoveStorageSlotScreen(self, removeSlot):
        self.rsss = QtWidgets.QMainWindow()
        self.ui = MoveRemoveStorageSlotScreen.Ui_MoveRemoveStorageSlotScreen()
        self.ui.setupUi(self.rsss, self, removeSlot)
        self.rsss.showFullScreen()
        User.User.MainScreen.hide()
        t = QtCore.QTimer(User.User.MainScreen)
        t.singleShot(0, self.ui.onLoad_RemoveStorageSlotScreen)

    def openManageProfileScreen(self):
        self.mus = QtWidgets.QMainWindow()
        self.ui = ManageUserScreen.Ui_ManageUserScreen()
        self.ui.setupUi(self.mus, self)
        self.mus.showFullScreen()
        User.User.MainScreen.hide()

    def openManageUserPermissionScreen(self, manageUser):
        self.mups = QtWidgets.QMainWindow()
        self.ui = ManageUserPermissionScreen.Ui_ManageUserPermissionScreen()
        self.ui.setupUi(self.mups, manageUser, self)
        self.mups.showFullScreen()
        User.User.MainScreen.hide()
        t = QtCore.QTimer(User.User.MainScreen)
        t.singleShot(0, self.ui.onLoad_ManageUserPermissionScreen)
    
    # add actions
    def addActions(self):
        if (User.User.PermStoreItems > 0):
            self.act_storeItems.triggered.connect(self.btn_storeItems_clicked)
            self.act_manageItems.triggered.connect(self.btn_manageItems_clicked)
        if (User.User.PermWithdrawItems > 0):
            self.act_withdrawItems.triggered.connect(self.btn_withdrawItems_clicked)
        if (User.User.PermCorrectQuantity > 0):
            self.act_setQuantity.triggered.connect(self.btn_setQuantity_clicked)
        if (User.User.PermManageUsers > 0):
            self.act_manageUser.triggered.connect(self.btn_manageUser_clicked)
            self.act_managePermissions.triggered.connect(self.btn_managePermissions_clicked)
        if (User.User.PermCreateInventoryReport > 0):
            self.act_createInventoryReport.triggered.connect(self.btn_createInventoryReport_clicked)   
        #if (User.User.PermManagePartitions > 0):
            #self.act_changeParititions.triggered.connect(self.btn_changePartitions_clicked)
        if (User.User.PermMoveStorageSlot > 0):
            self.act_moveStorageSlot.triggered.connect(self.btn_moveStorageSlot_clicked)
        if (User.User.PermDeleteStorageSlot > 0):
            self.act_removeStorageSlot.triggered.connect(self.btn_removeStorageSlot_clicked)      

    # exit button clicked action
    def btn_exit_clicked(self):
        MySQLDatabase.execDML("UPDATE users SET userSignedIn=0 WHERE ID=" + str(User.User.Id))
        User.unsetUser()
        User.User.LoginScreen.showFullScreen()
        User.User.MainScreen.close()

    # search button clicked action
    def btn_search_clicked(self):
        self.dh.updateDataTable()

    def onLoad_MainScreen(self):
        self.dh.updateDataTable()