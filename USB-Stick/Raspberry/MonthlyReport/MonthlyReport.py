import os, time
import db_connector

MySQLDatabase = db_connector.Database(host = "localhost", user = "ssu_db", password = "ssu_FRS", database = "ssu")

def main():
    reportReceiver = MySQLDatabase.execSelect(
        "SELECT ID FROM users WHERE monthlyNotification=1")
    def executeCommand(mode, userID):
        os.system("python3 /home/ssu/Desktop/PDF-Creator" +
                  "/PDF_Creator.py --mode " + str(mode) + 
                  " --userID " + str(userID) + " &")

    for receiver in reportReceiver:
        executeCommand(2, int(receiver[0]))
        time.sleep(300)

if (__name__ == "__main__"):
    main()