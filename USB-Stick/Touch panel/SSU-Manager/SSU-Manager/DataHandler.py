from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import db_connector, User

MySQLDatabase = db_connector.Database(host = "localhost", user = "ssu_db", password = "ssu_FRS", database = "ssu")

class DataHandlerMainScreen:
    def __init__(self, **kwargs):
        self.__dataTableView = kwargs.get('dtv')
        self.__dataListView = kwargs.get('liv')
        self.__textboxSearch = kwargs.get('txb')

    def rowSelected(self):
        try:
            self.rowIndex = self.__dataTableView.selectedItems()[0].row()
            self.rowIndex = self.__data[self.rowIndex][0]
            itemDataResult = MySQLDatabase.execSelect("SELECT rfn.name, itd.propertyValue, itd.unit FROM itemdata itd, referencenames rfn WHERE " +
                                                      "itd.referenceID = rfn.ID AND itd.itemID = " + str(self.rowIndex) + " ORDER BY rfn.name ASC")
            self.__dataListView.clear()
            i = 0
            for row in itemDataResult:
                if (row[2] == "none"):
                    unit = ""
                else:
                    unit = (" " + str(row[2]))

                self.__dataListView.addItem(str(row[0]) + " = " + str(row[1]) + unit)
                itemState = self.__dataListView.item(i)
                itemState.setFlags(itemState.flags() & ~Qt.ItemIsSelectable)
                i += 1
        except:
            self.rowIndex = 0
            print("Could not select a row!")


    def updateDataTable(self, showZeroQuantity=True):
        self.getData()
        self.setDataTable(showZeroQuantity)

    def getData(self):
        searchString = self.__textboxSearch.text()

        self.__data = MySQLDatabase.execSelect("SELECT itm.ID, SUM(sp.alarmActivated), " + 
	                                           "(SELECT COALESCE(SUM(quantityMin), 0) FROM storagep sp WHERE sp.alarmActivated = TRUE AND sp.itemID = itm.ID) AS SUMquantityMin, " +
	                                           "cmpt.typeName, cmpt.typeVersion, itm.articleNumber, SUM(sp.quantity) " +
	                                           "FROM items itm, storagep sp, componenttypes cmpt " +
	                                           "WHERE (sp.itemID = itm.ID AND itm.typeID = cmpt.ID) AND " +
                                               "(cmpt.typeName LIKE '" + searchString + "%' OR itm.articleNumber LIKE '" + searchString + "%' OR cmpt.typeVersion LIKE '" + searchString + "%') " +
	                                           "GROUP BY sp.itemID " +
	                                           "ORDER BY SUM(sp.quantity) DESC, cmpt.typeName ASC, itm.articleNumber ASC")

    def setDataTable(self, showZeroQuantity=True):
        self.__dataTableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.__dataTableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.__dataTableView.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.__dataTableView.setColumnCount(4)
        self.__dataTableView.setRowCount(0)

        self.__dataTableView.setHorizontalHeaderLabels(("Component", "Type", "Article No.", "Quantity"))

        self.__dataListView.clear()

        header = self.__dataTableView.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)       

        for i in range(1, 4):
            header.setSectionResizeMode(i, QHeaderView.ResizeToContents)

        for row in self.__data:
            rowPosition = self.__dataTableView.rowCount()
            if ((int(row[6]) != 0) or showZeroQuantity):
                self.__dataTableView.insertRow(rowPosition)

                if ((int(row[6]) == 0) and (row[1] > 0)):
                    lowQuantity = True
                    color = QColor(220, 20, 60)
                elif ((int(row[6]) < int(row[2])) and (row[1] > 0)):
                    lowQuantity = True
                    color = QColor(232, 153, 49)
                else:
                    lowQuantity = False

                for i in range(4):
                    item = QTableWidgetItem(str(row[i + 3]))

                    if (i > 0):
                        item.setTextAlignment(Qt.AlignCenter)

                    if(lowQuantity):
                        item.setBackground(color)
                    self.__dataTableView.setItem(rowPosition, i, item)

                vHeader = self.__dataTableView.verticalHeader()
                vHeader.setSectionResizeMode(rowPosition, QHeaderView.Fixed)
            else:
                self.__data = (self.__data[ : rowPosition] + self.__data[(rowPosition+1) : ])

class DataHandlerStorageScreen:
    def __init__(self, **kwargs):
        self.__dataTableView = kwargs.get('dtv')
        self.__dataListView = kwargs.get('liv')
        self.__textboxSearch = kwargs.get('txb')

    def rowSelected(self):
        try:
            self.rowIndex = self.__dataTableView.selectedItems()[0].row()
            self.quantity = self.__data[self.rowIndex][4]
            self.rowIndex = self.__data[self.rowIndex][0]            
            itemDataResult = MySQLDatabase.execSelect("SELECT rfn.name, itd.propertyValue, itd.unit FROM itemdata itd, referencenames rfn WHERE " +
                                                      "itd.referenceID = rfn.ID AND itd.itemID = " + str(self.rowIndex) + " ORDER BY rfn.name ASC")
            self.__dataListView.clear()
            i = 0
            for row in itemDataResult:
                if (row[2] == "none"):
                    unit = ""
                else:
                    unit = (" " + str(row[2]))

                self.__dataListView.addItem(str(row[0]) + " = " + str(row[1]) + unit)
                itemState = self.__dataListView.item(i)
                itemState.setFlags(itemState.flags() & ~Qt.ItemIsSelectable)
                i += 1
        except:
            self.rowIndex = 0
            print("Could not select a row!")

    def updateDataTable(self):
        self.getData()
        self.setDataTable()

    def getData(self):
        searchString = self.__textboxSearch.text()

        self.__data = MySQLDatabase.execSelect("SELECT itm.ID, cmpt.typeName, cmpt.typeVersion, itm.articleNumber, " +
	                                            "COALESCE((SELECT SUM(stp.quantity) sum FROM storagep stp " +
	                                            "WHERE stp.itemID=itm.ID GROUP BY stp.itemID), 0) sumQuantity " +
	                                            "FROM items itm, componenttypes cmpt " +
	                                            "WHERE itm.typeID = cmpt.ID AND " +
                                                "(cmpt.typeName LIKE '" + searchString + "%' OR itm.articleNumber LIKE '" + searchString + "%' OR cmpt.typeVersion LIKE '" + searchString + "%') " +
	                                            "ORDER BY sumQuantity DESC, cmpt.typeName ASC, itm.articleNumber ASC")

    def setDataTable(self):
        self.__dataTableView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.__dataTableView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.__dataTableView.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.__dataTableView.setColumnCount(4)
        self.__dataTableView.setRowCount(0)

        self.__dataTableView.setHorizontalHeaderLabels(("Component", "Type", "Article No.", "Quantity"))

        self.__dataListView.clear()

        header = self.__dataTableView.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)       

        for i in range(1, 4):
            header.setSectionResizeMode(i, QHeaderView.ResizeToContents)

        for row in self.__data:
            rowPosition = self.__dataTableView.rowCount()    
            self.__dataTableView.insertRow(rowPosition)

            for i in range(4):
                item = QTableWidgetItem(str(row[i + 1]))

                if (i > 0):
                    item.setTextAlignment(Qt.AlignCenter)

                self.__dataTableView.setItem(rowPosition, i, item)

            vHeader = self.__dataTableView.verticalHeader()
            vHeader.setSectionResizeMode(rowPosition, QHeaderView.Fixed)