# import raspberry i2c library
import smbus, time

# define class Arduinoi2C
class ArduinoI2C:
    # constructor of the class
    def __init__(self, **kwargs):
        self.__channel = int(kwargs.get('i2c'))        
        self.__address = int(kwargs.get('address'))
        self.bus = smbus.SMBus(self.__channel)
    
    # set the command
    # Bit 7 => activate LED
    # Bit 6 => LED is on/off (only on Arduino)
    # Bit 5,4,3 => not used
    # Bit 2,1,0 => set speed
    def setCommand(self, stateActive, speed):
        if(stateActive):
            self.__cmd = 0x80
        else:
            self.__cmd = 0x00
        
        # blink every 250ms 
        if (speed == 1):
            self.__cmd |= (1 << 0)
        # blink every 500ms 
        elif (speed == 2):
            self.__cmd |= (1 << 1)
        # blink every 750ms
        elif (speed == 3):
            self.__cmd |= ((1 << 1) | (1 << 0))
        # blink every 1s
        elif (speed == 4):
            self.__cmd |= (1 << 2)
        # continuously on
        else:
            self.__cmd &= ~0x0F

    # write the command, position and color to the arduino
    def write(self, ledID, color):
        try:
            colR = color[0]
            colG = color[1]
            colB = color[2]
            ledID -= 1
            self.bus.write_block_data(self.__address, self.__cmd, [ledID, colR, colG, colB])
            return True
        except:
            time.sleep(0.5)
            self.bus = smbus.SMBus(self.__channel)
            print("I2C-Bus error!")
            return False