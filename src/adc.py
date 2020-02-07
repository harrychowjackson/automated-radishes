import Adafruit_ADS1x15

# To install this package on the raspberry pi, use:
# 
# sudo apt-get update
# sudo apt-get install build-essential python-dev python-smbus python-pip
# sudo pip install adafruit-ads1x15
# 
# Additional information available from Adafruit:
# https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters/ads1015-slash-ads1115

class Taris_ADC():

    def __init__(self,adc_address,i2c_bus):
        self.i2c_bus = i2c_bus             # default: 1 (0 on older pi's)
        self.adc_address = adc_address     # default: 0x48

    def setupADC(self):
        # Configure ADC for Adafruit's ADS1115 chip
        print("Connected sensor: ADS1115 @ " + str(self.adc_address))
        self.adc = Adafruit_ADS1x15.ADS1115(address=self.adc_address, busnum=self.i2c_bus)
        return self.adc

    def readADC(self,adc_pin_address, adc_gain):
    	return self.adc.read_adc(adc_pin_address, adc_gain)