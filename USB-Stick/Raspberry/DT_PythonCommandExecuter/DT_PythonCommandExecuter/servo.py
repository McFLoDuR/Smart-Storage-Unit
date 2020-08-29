# import the GPIO libary
import RPi.GPIO as GPIO
# import the time libary
import time

# set the GPIO pinout to BCM and turn off the warnings
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# define class Servo
class Servo:
    # constructor of the class
    def __init__(self, **kwargs):
        self.__pin = int(kwargs.get('pin'))
        self.__servoPWMRetract = float(kwargs.get('retractPWM'))
        self.__servoPWMExtend = float(kwargs.get('extendPWM'))

        # set the GPIO pin to OUTPUT
        GPIO.setup(self.__pin, GPIO.OUT)

        self.__pwm = GPIO.PWM(self.__pin, 50)
        self.__pwm.start(0)

    # public method to extend the drawer
    def extendDrawer(self):
        self.__pwm.ChangeDutyCycle(self.__servoPWMExtend)
        time.sleep(1)
        self.__pwm.ChangeDutyCycle(0)

    # public method to retract the drawer
    def retractDrawer(self):
        self.__pwm.ChangeDutyCycle(self.__servoPWMRetract)
        time.sleep(1)
        self.__pwm.ChangeDutyCycle(0)