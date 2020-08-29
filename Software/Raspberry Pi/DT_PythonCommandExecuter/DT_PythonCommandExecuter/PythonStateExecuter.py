# import time and datetime
import time
import datetime
# import owm libaries
import adc_1115
import servo
import db_connector
import i2c_handler

# define database object
MySQLDatabase = db_connector.Database(host = "localhost", user = "ssu_db", password = "ssu_FRS", database = "ssu")
# define servo object
DrawerServo = servo.Servo(pin = 17, retractPWM = 9.29, extendPWM = 2.37)
# define adc object
MicroScaleADC = adc_1115.ADC(gain = 4, divider = 20, offset = -30000)
# define i2c connection
I2CConnection = i2c_handler.ArduinoI2C(i2c = 1, address = 0x51)

# retract the drawer and set every to 'default'
DrawerServo.retractDrawer()
while (not MySQLDatabase.execDML("UPDATE stateStorage SET UserID=0, stateActivated=0, stateChanged=0, stateValue=0 WHERE id=1")):
    time.sleep(5)

# set every user to logged out
while (not MySQLDatabase.execDML("UPDATE users SET userSignedIn = 0")):
    time.sleep(5)

# delete every LED which is turned on (Reset after restart)
while (not MySQLDatabase.execDML("DELETE FROM activeLEDs WHERE stateChanged = 0")):
    time.sleep(5)

# define globale variables
WeightMeasureActive = False

i2cSleep = 0.05

# endless loop the programm
while True:
    endSleepTime = 1.0

    # after ervery second passed, get the datasets for comparison
    resultStates = MySQLDatabase.execSelect("SELECT * FROM stateStorage WHERE id = 1")[0]
    resultLEDs = MySQLDatabase.execSelect("SELECT * FROM activeLEDs WHERE stateChanged = 1")

    # check if there where any changes in the activeLEDs table
    if (len(resultLEDs) > 0):
        # if there where some, write the new datasets to the arduino
        for row in resultLEDs:
            I2CConnection.setCommand(int(row[3]), int(row[2]))
            hexColor = row[1]
            color = tuple(int(hexColor[i:i+2], 16) for i in (0, 2, 4))
            if (I2CConnection.write(int(row[0]), color)):                
                # reset the changed flag in the database
                if (int(row[3]) > 0):
                    MySQLDatabase.execDML("UPDATE activeLEDs SET stateChanged = 0 WHERE SlotID = " + str(row[0]))
                else:
                    MySQLDatabase.execDML("DELETE FROM activeLEDs WHERE SlotID = " + str(row[0]))

                time.sleep(i2cSleep)
                endSleepTime -= i2cSleep

        # set the result string to empty
        resultLEDs = tuple()

    # if a user and changed is set
    if((int(resultStates[2]) != 0) and (int(resultStates[4]) == 1)):
        # activate
        if(int(resultStates[3]) == 1):
            # set the offset of the micro scale and extend the drawer
            MicroScaleADC.setOffset(5)
            DrawerServo.extendDrawer()
            addition = "stateChanged=0"
            WeightMeasureActive = True
        # deactivate
        else:
            # retract the drawer
            DrawerServo.retractDrawer()
            addition = "UserID=0, stateActivated=0, stateChanged=0"
            WeightMeasureActive = False

        # reset the dataset in the database
        MySQLDatabase.execDML("UPDATE stateStorage SET " + str(addition) + " WHERE id=1")

    # if the measurement is activated
    if(WeightMeasureActive):
        # after every 1s get the measurement and update the database        
        MySQLDatabase.execDML("UPDATE stateStorage SET stateValue=" + str(MicroScaleADC.measureGram()) + " WHERE id=1")

    # save cpu performance not time
    time.sleep(endSleepTime)