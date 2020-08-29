# import all necessary modules
import argparse
import sys
from datetime import datetime 
from fpdf import FPDF, HTMLMixin

# import database connector and email handler
import email_handler
import db_connector

# create database object
MySQLDatabase = db_connector.Database(host = "localhost", user = "ssu_db", password = "ssu_FRS", database = "ssu")
# create email objects
EmailHandler = email_handler.Email()

# define some global variables
Statement = ""
dateTimeObj = datetime.now()
userID = 0

# create a new PDF class and let it be the sibling of the FPDF and HTMLMixin class
class PDF(FPDF, HTMLMixin):
    def header(self):
        if(self.page_no() > 1):
            self.image('/home/ssu/Desktop/PDF-Creator/ssu.png', 25, 15, 30)
            self.set_font('Arial', 'B', 24)
            self.cell(0, 23, 'Smart Storage Unit', 0, 0, 'R')
            self.ln(30)
        else:
            self.image('/home/ssu/Desktop/PDF-Creator/ssu.png', 98.5, 35, 100)
            self.set_font('Arial', 'B', 36)
            self.ln(115)
            self.cell(0, 36, 'Smart Storage Unit', 0, 0, 'C')
            self.ln(35)
            self.set_font('Arial', 'B', 24)
            self.cell(0, 0, 'Inventory Report', 0, 0, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', '', 14)
        if(self.page_no() > 1):
            currentDate = ("Date: " + dateTimeObj.strftime("%d.%m.%Y") + 
                           "  Time: " + 
                           dateTimeObj.strftime("%H:%M:%S"))
            self.cell(0, 0, currentDate, 0, 0, 'L')
            self.cell(0, 0, 'Page %s' % (self.page_no() - 1), 0, 0, 'R')


# create a pdf object and set the orientation, unit, and page size
pdf = PDF(orientation='L', unit='mm', format='A4')

def table():
    # get the itemdata from the choosen statement
    itemData = MySQLDatabase.execSelect(Statement)

    # create table head -> it will be displayed on every new page on top of the table
    head = """
           <thead>
               <tr bgcolor=\"#38aae8;\">
                   <th width="23%">Article No.</th>
                   <th width="19%">Component</th>
                   <th width="14%">Type</th>
                   <th width="32%">Item Data</th>
                   <th width="12%">Quantity</th>
               </tr>
           </thead>
           """

    body = "<tbody>"
    i=0

    # write every dataset from the list into the table
    for row in itemData:
        # set correct background colors
        col = i % 2 and "#b6e2fa" or "#d7ecf7"

        if ((int(row[6]) == 0) and (row[1] > 0)):
            col = i % 2 and "#db7070" or "#db9393"
        elif ((int(row[6]) < int(row[2])) and (row[1] > 0)):
            col = i % 2 and "#f5bc71" or "#edc48e"

        i+=1

        # get the single item data
        itemResult = MySQLDatabase.execSelect("SELECT rfn.name, itd.propertyValue, itd.unit FROM itemdata itd, referencenames rfn WHERE " +
                                              "itd.referenceID = rfn.ID AND itd.itemID = " + str(row[0]))

        # hard coded solution for texts that are bigger than the column
        if (len(itemResult) > 0):
            if(itemResult[0][2] == "none"):
                unit = ""
            else:
                unit = itemResult[0][2]
            firstData = (itemResult[0][0] + ": " + itemResult[0][1] + " " + unit)
            itemResult = itemResult[1:]
        else:
            firstData = ("no available data")

        if(pdf.get_string_width(str(row[5])) < 53):
            columnAlign1 = "align=\"center\""
        else:
            columnAlign1 = ""
        
        if(pdf.get_string_width(str(row[3])) < 44):
            columnAlign2 = "align=\"center\""
        else:
            columnAlign2 = ""

        if(pdf.get_string_width(str(row[4])) < 32):
            columnAlign3 = "align=\"center\""
        else:
            columnAlign3 = ""

        if(pdf.get_string_width(str(row[6])) < 29):
            columnAlign5 = "align=\"center\""
        else:
            columnAlign5 = ""
            
        # clear every < or > out of the text, otherwise the pdf will be bugged
        colT1 = str(row[5]).replace("<", "")
        colT1 = str(row[5]).replace(">", "")
        colT2 = str(row[3]).replace("<", "")
        colT2 = str(row[3]).replace(">", "")
        colT3 = str(row[4]).replace("<", "")
        colT3 = str(row[4]).replace(">", "")
        colT4 = firstData.replace("<", "")
        colT4 = firstData.replace(">", "")
        colT5 = str(row[6]).replace("<", "")
        colT5 = str(row[6]).replace(">", "")

        # add the data row to the pdf
        stringConstructor = ("<tr bgcolor=\"" + col + "\"><td " + 
                             columnAlign1 + ">{col1}</td><td " + 
                             columnAlign2 + ">{col2}</td><td " + 
                             columnAlign3 + ">{col3}</td><td>{col4}</td><td " + 
                             columnAlign5 + ">{col5}</td></tr>")
        stringConstructor = stringConstructor.format(col1=colT1, col2=colT2, 
                                                     col3=colT3, col4=colT4, col5=colT5)
        body += stringConstructor

        # write additional item data in the following lines
        for data in itemResult:
            if(data[2] == "none"):
                unit = ""
            else:
                unit = data[2]

            dataCol = (data[0] + ": " + data[1] + " " + unit)

            dataCol = dataCol.replace("<", "")
            dataCol = dataCol.replace(">", "")

            stringConstructor = ("<tr bgcolor=\"" + col + 
                                 "\"><td> </td><td> </td><td> " +
                                 "</td><td>{dataCol}</td><td> </td></tr>")
            stringConstructor = stringConstructor.format(dataCol=dataCol)
            body += stringConstructor 

    body += "</tbody>"


    table = "<font face=\"Arial\"><table border=\"1\" align=\"center\" width=\"100%\">" + head + body + "</table></font>"
    return table

def NewPage():
    # create a new pdf page
    pdf.add_page()   

# define add the page content to a page, it will display the whole items
def AddPageContent():
    pdf.ln(2)
    pdf.set_font('Arial', 'B', 24)
    pdf.cell(0, 0, 'List of Items', 0, 0, 'C')
    pdf.ln(2)
    pdf.set_font('Arial', '', 12)
    # add the table in the pdf
    pdf.write_html(table())

# main for creating a pdf
def CreatePDF():
    pdf.set_margins(25, 20, 25)
    pdf.set_auto_page_break(True, 20)
    NewPage()
    NewPage()
    AddPageContent()

    pdf.output("/home/ssu/Desktop/PDF-Creator/" +
               "PDFs/SmartStorageUnit_InventoryReport" + 
               str(userID) + ".pdf") 

# main for sending an email
def SendEmail():
    EmailHandler.sendEmail(userID)

if (__name__ == "__main__"):
    try:
        # parse the required arguments at the console call
        parser = argparse.ArgumentParser(description='PDF-Creator: Mode Selector!')
        parser.add_argument("--mode", required=True, type=int)
        parser.add_argument("--userID", required=True, type=int)
        args = parser.parse_args()

        # save the arguments into variables
        mode = int(args.mode)
        userID = int(args.userID)

        # select the choosen printing method
        if (mode == 1):
            Statement = ("SELECT itm.ID, SUM(sp.alarmActivated), " + 
	                        "(SELECT COALESCE(SUM(quantityMin), 0) FROM storagep sp WHERE sp.alarmActivated = TRUE AND sp.itemID = itm.ID) AS SUMquantityMin, " +
	                        "cmpt.typeName, cmpt.typeVersion, itm.articleNumber, SUM(sp.quantity) " +
	                        "FROM items itm, storagep sp, componenttypes cmpt " +
	                        "WHERE (sp.itemID = itm.ID AND itm.typeID = cmpt.ID) " +
	                        "GROUP BY sp.itemID " +
	                        "ORDER BY SUM(sp.quantity), itm.articleNumber ASC")
        elif (mode == 2):
            Statement = ("SELECT itm.ID, " +
	                    "(SELECT COALESCE(SUM(sp.alarmActivated), 0) FROM storagep sp WHERE sp.alarmActivated = TRUE AND sp.itemID = itm.ID) AS alarmActivated, " +
	                    "(SELECT COALESCE(SUM(sp.quantityMin), 0) FROM storagep sp WHERE sp.alarmActivated = TRUE AND sp.itemID = itm.ID) AS quantityMin, " +
	                    "cmpt.typeName, cmpt.typeVersion, itm.articleNumber, " +
	                    "(SELECT COALESCE(SUM(sp.quantity), 0) FROM storagep sp WHERE sp.itemID = itm.ID) AS quantity " +
	                    "FROM items itm, componenttypes cmpt " +
	                    "WHERE itm.typeID = cmpt.ID " +
	                    "GROUP BY itm.ID " +
	                    "ORDER BY (SELECT COALESCE(SUM(sp.quantity), 0) FROM storagep sp WHERE sp.itemID = itm.ID), itm.articleNumber ASC");
        elif (mode == 3):
            Statement = ("SELECT itm.ID, " +
	                        "(SELECT COALESCE(SUM(sp.alarmActivated), 0) FROM storagep sp WHERE sp.alarmActivated = TRUE AND sp.itemID = itm.ID) AS alarmActivated, " +
	                        "(SELECT COALESCE(SUM(sp.quantityMin), 0) FROM storagep sp WHERE sp.alarmActivated = TRUE AND sp.itemID = itm.ID) AS quantityMin, " +
	                        "cmpt.typeName, cmpt.typeVersion, itm.articleNumber, " +
	                        "(SELECT COALESCE(SUM(sp.quantity), 0) FROM storagep sp WHERE sp.itemID = itm.ID) AS quantity " +
	                        "FROM items itm, componenttypes cmpt " +
	                        "WHERE (itm.typeID = cmpt.ID AND (SELECT COALESCE(SUM(sp.quantity), 0) FROM storagep sp WHERE sp.itemID = itm.ID) <= (SELECT COALESCE(SUM(sp.quantityMin), 0) FROM storagep sp WHERE sp.itemID = itm.ID) OR NOT itm.ID IN (SELECT itemID FROM storagep)) " +
	                        "GROUP BY itm.ID " +
	                        "ORDER BY (SELECT COALESCE(SUM(sp.quantity), 0) FROM storagep sp WHERE sp.itemID = itm.ID), itm.articleNumber ASC")
        else:
            print("PDF-Creator: FAIL: This mode doesn't exist!")
            sys.exit()

        result = MySQLDatabase.execSelect("SELECT * FROM users WHERE ID=" + str(userID))

        # check if the userID exists
        if (len(result) < 1):
            print("PDF-Creator: FAIL: This user doesn't exist!")
            sys.exit()

        # create a PDF and send it to the users email
        CreatePDF()
        SendEmail()
    except:
        print("PDF-Creator: FAIL: Critical error while creating PDF!")