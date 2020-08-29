# import the libary of the adc
import Adafruit_ADS1x15

# define class Analog-Digital-Converter
class ADC:
    # constructor of the class
    def __init__(self, **kwargs):
        self.__gain = int(kwargs.get('gain'))
        self.__divider = int(kwargs.get('divider'))
        self.__offset = int(kwargs.get('offset'))
        # initialize the ADC
        self.__adc = Adafruit_ADS1x15.ADS1115()

    # public method to take multiple measurements of the micro scale and calculate the avarage value -> returns the measurement in digital
    def measure(self):
        value = 0
        for i in range(self.__divider):
            value += self.__adc.read_adc_difference(0, gain=self.__gain)
        value /= self.__divider

        return value

    # public method to measure and convert the result to gramm -> returns the measurement in gramm
    def measureGram(self):
        return self.__convertToGram(self.measure())

    # private method to convert the input digtal value to gramm -> returns the input digital value in gramm
    def __convertToGram(self, digitalValue):
        return (0.0015 * float(digitalValue) + self.__offset)

    # public method to measure and set the offset of the micro scale
    def setOffset(self, measurements = 5):
        result = 0
        for i in range(measurements):
            result += self.measure()
          
        self.__offset = round(float(result) / float(measurements))
        self.__offset = -(0.0015 * float(self.__offset))