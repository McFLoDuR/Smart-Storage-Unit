# import all necessary modules
import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.header import Header
from email import encoders
from email.utils import formataddr

# import database connector
import db_connector

# create database object
MySQLDatabase = db_connector.Database(host = "localhost", user = "ssu_db", password = "ssu_FRS", database = "ssu")

# define Email class
class Email:   
    # send an email to the email adresse of this userID
    def sendEmail(self, userID):
        # login data for smtp
        EMAIL = "smartstorageunit@gmx.at"
        PASSWORD = "ssu_FRS_mail"

        # create the smtp connection and log in to the server
        mail = smtplib.SMTP(host="mail.gmx.net", port=587)
        mail.starttls()
        mail.login(EMAIL, PASSWORD)

        # create the message content
        msg = MIMEMultipart()

        # get the user data with the userID
        userResult = MySQLDatabase.execSelect("SELECT * FROM users WHERE id=" + str(userID))[0]

        # set the header of the email
        msg['From'] = formataddr((str(Header(u'Smart Storage Unit', 'utf-8')), EMAIL))
        msg['To'] = str(userResult[4])
        msg['Subject'] = "Inventory Report"

        # filename of the pdf
        file = "/home/ssu/Desktop/PDF-Creator/PDFs/SmartStorageUnit_InventoryReport" + str(userResult[0]) + ".pdf"

        # open pdf and read the bytes
        with open(file, 'rb') as fp:
            attachPDF = MIMEBase('application', "octet-stream")
            attachPDF.set_payload(fp.read())
            fp.close()

        # encode the string and add it to the header
        encoders.encode_base64(attachPDF)
        attachPDF.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))

        # filename of the body schematic
        contentHTML = "/home/ssu/Desktop/PDF-Creator/content.html"

        # read a string from the hmtl
        with open(contentHTML, 'r') as file:
            content = file.read()
            file.close()

        # fill in the name of the user into the read content
        content = content.format(name=(str(userResult[1]).capitalize()))

        # attach the message body and the PDF to the email
        msg.attach(MIMEText(content, 'html'))
        msg.attach(attachPDF)

        # send the email
        mail.send_message(msg)
    
        del msg
        del attachPDF

        # close the connection to the smtp server
        mail.quit()