import db_connector, User

MySQLDatabase = db_connector.Database(host = "localhost", user = "ssu_db", password = "ssu_FRS", database = "ssu")

def convertRGB2HEX(colorRGB):
    return "".join([format(val, '02X') for val in colorRGB])

def convertHEX2RGB(colorHEX):
    return tuple(int(colorHEX[i:i+2], 16) for i in (0, 2, 4))

def isColorOK(colorRGB, newUser=True, minDifference=70):
    if (not newUser):
        userAddon = " WHERE NOT ID=" + str(User.User.Id)
    else:
        userAddon = ""

    colors = MySQLDatabase.execSelect("SELECT color FROM users" + userAddon)

    for color in colors:
        if (areColorsTooClose(colorRGB, convertHEX2RGB(str(color[0])), minDifference)):
            return False

    return True

def areColorsTooClose(colorA, colorB, minDifference=30):
    r = (int(colorA[0]) - int(colorB[0]))
    g = (int(colorA[1]) - int(colorB[1]))
    b = (int(colorA[2]) - int(colorB[2]))

    if (((r*r) + (g*g) + (b*b)) <= (minDifference*minDifference)):
        return True
    else:
        return False

def isStringEmptyOrSpace(string):
    if ((not string) or string.isspace()):
        return True
    else:
        return False

def isPasswordLengthOK(password):
    if ((len(password) >= 8) and (len(password) <= 16)):
        return True
    else:
        return False

def hashString(string, rounds=5):
    import hashlib

    for i in range(rounds):
        h = hashlib.sha256()
        string = string.encode()
        h.update(string)
        string = str(h.hexdigest())
        string = string.upper()

    return string

def getMicroScaleUser():
    return int(MySQLDatabase.execSelect("SELECT UserID FROM stateStorage")[0][0])

def isMicroScaleUsageOK(itemID, quantity):
    result = float(MySQLDatabase.execSelect("SELECT weight FROM items WHERE ID=" + str(itemID))[0][0])

    if ((result > 0.00000000) and (result < 100.00000000)):
        if (quantity >= 20):
            if ((result * quantity) < 90.00000000):
                if (getMicroScaleUser() == 0):
                    return True
    
    return False

def isItemForMicroScaleOK(itemID, quantity):
    result = float(MySQLDatabase.execSelect("SELECT weight FROM items WHERE ID=" + str(itemID))[0][0])

    if (((result * quantity) > 90.00000000) and (result < 100.00000000)):
        return 0
    elif (result <= 0):
        return 1
    else:
        return 2

def isMicroScaleEmpty():
    tolerance = 2 # 0.03
    weight = getMicroScaleResult()
    if ((weight >= -tolerance) and (weight <= tolerance)):
        return True
    else:
        return False

# 0 = LED on
# 1 = blinks every 250ms
# 2 = blinks every 500ms
# 3 = blinks every 750ms
# 4 = blinks every 1s
def startLED(SlotID, colorHEX, speed):
    return MySQLDatabase.execDML("INSERT INTO activeLEDs(SlotID, color, speed, stateActivated, stateChanged)" +
                                 "VALUES(" + str(SlotID) + ", '" + str(colorHEX) + "', " + str(speed) + ", TRUE, TRUE)")

def stopLED(SlotID):
    return MySQLDatabase.execDML("UPDATE activeLEDs SET stateActivated=0, stateChanged=1 WHERE SlotID=" + str(SlotID))


def startMicroScale():
    return MySQLDatabase.execDML("UPDATE stateStorage SET UserID=" + str(User.User.Id) + ", stateActivated=1, stateChanged=1 WHERE ID=1")

def getMicroScaleResult():
    return float(MySQLDatabase.execSelect("SELECT stateValue FROM stateStorage WHERE ID=1")[0][0])

def stopMicroScale():
    return MySQLDatabase.execDML("UPDATE stateStorage SET stateActivated=0, stateChanged=1 WHERE ID=1")