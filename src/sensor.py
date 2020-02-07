import os
import sys
import time
import Adafruit_ADS1x15


class Block_A_Sensors(object):
    def __init__(self):
        # Create an ADS1115 ADC (16-bit) instance for the I2C address.
        self.sensorBlockA = Adafruit_ADS1x15.ADS1015(address=0x48, busnum=1)

        # Choose a gain of 1 for reading voltages from 0 to 4.09V.
        # Pick a different gain to change the range of voltages.
        # See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
        self.gain = 1

        # SensorBlock A: Assigned Sensor Pins
        self.tempPin0  = 0
        self.tempPin1  = 1
        self.lightPin2 = 2
        self.lightPin3 = 3

    def check_raw0(self):
        return self.sensorBlockA.read_adc(self.tempPin0, gain=self.gain)

    def check_raw1(self):
        return self.sensorBlockA.read_adc(self.tempPin1, gain=self.gain)

    def check_raw2(self):
        return self.sensorBlockA.read_adc(self.lightPin2, gain=self.gain)

    def check_raw3(self):
        return self.sensorBlockA.read_adc(self.lightPin3, gain=self.gain)

    def check_temp(self):
        '''Checks the voltage output of two thermistor voltage dividers,
        and returns the average of 10 values (from each).'''
        total_temp0 = 0
        total_temp1 = 0
        for i in range(10):
            temp0 = self.sensorBlockA.read_adc(self.tempPin0, gain=self.gain)
            temp1 = self.sensorBlockA.read_adc(self.tempPin1, gain=self.gain)
            # Note you can also pass in an optional data_rate parameter that controls
            # the ADC conversion time (in samples/second). Each chip has a different
            # set of allowed data rate values, see datasheet Table 9 config register
            # DR bit values.
            # adc.read_adc(i, gain=GAIN, data_rate=128)
            # Each value will be a 12 or 16 bit signed integer value depending on the
            # ADC (ADS1015 = 12-bit, ADS1115 = 16-bit).
            total_temp0 = total_temp0 + temp0
            total_temp1 = total_temp1 + temp1
        average_temp0 = float(total_temp0) / float(10)
        average_temp1 = float(total_temp1) / float(10)

        # if sensor averages are too different, warn the user
        percent_diff = abs(average_temp0 / average_temp1)
        if percent_diff > 0.30:
            print('Warning: thermistor average readings > 30% different.')

        return float(average_temp0 + average_temp1) / float(2)

    def check_light_level(self):
        '''Checks the voltage output of two photoresistor voltage dividers,
        and returns the average of 10 values (from each).'''
        total_light0 = 0
        total_light1 = 0
        for i in range(10):
            light0 = self.sensorBlockA.read_adc(self.lightPin2, gain=self.gain)
            light1 = self.sensorBlockA.read_adc(self.lightPin3, gain=self.gain)
            # Note you can also pass in an optional data_rate parameter that controls
            # the ADC conversion time (in samples/second). Each chip has a different
            # set of allowed data rate values, see datasheet Table 9 config register
            # DR bit values.
            # adc.read_adc(i, gain=GAIN, data_rate=128)
            # Each value will be a 12 or 16 bit signed integer value depending on the
            # ADC (ADS1015 = 12-bit, ADS1115 = 16-bit).
            total_light0 = total_light0 + light0
            total_light1 = total_light1 + light1
        average_light0 = float(total_light0) / float(10)
        average_light1 = float(total_light1) / float(10)

        # if sensor averages are too different, warn the user
        percent_diff = abs(average_light0 / average_light1)
        if percent_diff > 0.30:
            print('Warning: photoresistor average readings > 30% different.')

        return float(average_light0 + average_light1) / float(2)

class Block_B_Sensors(object):
    def __init__(self):
        # Create an ADS1115 ADC (16-bit) instance for the I2C address.
        self.sensorBlockB = Adafruit_ADS1x15.ADS1015(address=0x49, busnum=1)

        # Choose a gain of 1 for reading voltages from 0 to 4.09V.
        # Pick a different gain to change the range of voltages.
        # See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
        self.gain = 1

        # SensorBlock A: Assigned Sensor Pins
        self.tempPin0  = 0
        self.tempPin1  = 1
        self.lightPin2 = 2
        self.lightPin3 = 3

    def check_raw0(self):
        return self.sensorBlockB.read_adc(self.tempPin0, gain=self.gain)

    def check_raw1(self):
        return self.sensorBlockB.read_adc(self.tempPin1, gain=self.gain)

    def check_raw2(self):
        return self.sensorBlockB.read_adc(self.lightPin2, gain=self.gain)

    def check_raw3(self):
        return self.sensorBlockB.read_adc(self.lightPin3, gain=self.gain)

    def check_temp(self):
        '''Checks the voltage output of two thermistor voltage dividers,
        and returns the average of 10 values (from each).'''
        total_temp0 = 0
        total_temp1 = 0
        for i in range(10):
            temp0 = self.sensorBlockB.read_adc(self.tempPin0, gain=self.gain)
            temp1 = self.sensorBlockB.read_adc(self.tempPin1, gain=self.gain)
            # Note you can also pass in an optional data_rate parameter that controls
            # the ADC conversion time (in samples/second). Each chip has a different
            # set of allowed data rate values, see datasheet Table 9 config register
            # DR bit values.
            # adc.read_adc(i, gain=GAIN, data_rate=128)
            # Each value will be a 12 or 16 bit signed integer value depending on the
            # ADC (ADS1015 = 12-bit, ADS1115 = 16-bit).
            total_temp0 = total_temp0 + temp0
            total_temp1 = total_temp1 + temp1
        average_temp0 = float(total_temp0) / float(10)
        average_temp1 = float(total_temp1) / float(10)

        # if sensor averages are too different, warn the user
        percent_diff = abs(average_temp0 / average_temp1)
        if percent_diff > 0.30:
            print('Warning: thermistor average readings > 30% different.')

        return float(average_temp0 + average_temp1) / float(2)

    def check_light_level(self):
        '''Checks the voltage output of two photoresistor voltage dividers,
        and returns the average of 10 values (from each).'''
        total_light0 = 0
        total_light1 = 0
        for i in range(10):
            light0 = self.sensorBlockB.read_adc(self.lightPin2, gain=self.gain)
            light1 = self.sensorBlockB.read_adc(self.lightPin3, gain=self.gain)
            # Note you can also pass in an optional data_rate parameter that controls
            # the ADC conversion time (in samples/second). Each chip has a different
            # set of allowed data rate values, see datasheet Table 9 config register
            # DR bit values.
            # adc.read_adc(i, gain=GAIN, data_rate=128)
            # Each value will be a 12 or 16 bit signed integer value depending on the
            # ADC (ADS1015 = 12-bit, ADS1115 = 16-bit).
            total_light0 = total_light0 + light0
            total_light1 = total_light1 + light1
        average_light0 = float(total_light0) / float(10)
        average_light1 = float(total_light1) / float(10)

        # if sensor averages are too different, warn the user
        percent_diff = abs(average_light0 / average_light1)
        if percent_diff > 0.30:
            print('Warning: photoresistor average readings > 30% different.')

        return float(average_light0 + average_light1) / float(2)

class Block_C_Sensors(object):
    def __init__(self):
        # Create an ADS1115 ADC (16-bit) instance for the I2C address.
        self.sensorBlockC = Adafruit_ADS1x15.ADS1015(address=0x4A, busnum=1)

        # Choose a gain of 1 for reading voltages from 0 to 4.09V.
        # Pick a different gain to change the range of voltages.
        # See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
        self.gain = 1

        # SensorBlock A: Assigned Sensor Pins
        self.tempPin0  = 0
        self.tempPin1  = 1
        self.lightPin2 = 2
        self.lightPin3 = 3

    def check_raw0(self):
        return self.sensorBlockC.read_adc(self.tempPin0, gain=self.gain)

    def check_raw1(self):
        return self.sensorBlockC.read_adc(self.tempPin1, gain=self.gain)

    def check_raw2(self):
        return self.sensorBlockC.read_adc(self.lightPin2, gain=self.gain)

    def check_raw3(self):
        return self.sensorBlockC.read_adc(self.lightPin3, gain=self.gain)

    def check_temp(self):
        '''Checks the voltage output of two thermistor voltage dividers,
        and returns the average of 10 values (from each).'''
        total_temp0 = 0
        total_temp1 = 0
        for i in range(10):
            temp0 = self.sensorBlockC.read_adc(self.tempPin0, gain=self.gain)
            temp1 = self.sensorBlockC.read_adc(self.tempPin1, gain=self.gain)
            # Note you can also pass in an optional data_rate parameter that controls
            # the ADC conversion time (in samples/second). Each chip has a different
            # set of allowed data rate values, see datasheet Table 9 config register
            # DR bit values.
            # adc.read_adc(i, gain=GAIN, data_rate=128)
            # Each value will be a 12 or 16 bit signed integer value depending on the
            # ADC (ADS1015 = 12-bit, ADS1115 = 16-bit).
            total_temp0 = total_temp0 + temp0
            total_temp1 = total_temp1 + temp1
        average_temp0 = float(total_temp0) / float(10)
        average_temp1 = float(total_temp1) / float(10)

        # if sensor averages are too different, warn the user
        percent_diff = abs(average_temp0 / average_temp1)
        if percent_diff > 0.30:
            print('Warning: thermistor average readings > 30% different.')

        return float(average_temp0 + average_temp1) / float(2)

    def check_light_level(self):
        '''Checks the voltage output of two photoresistor voltage dividers,
        and returns the average of 10 values (from each).'''
        total_light0 = 0
        total_light1 = 0
        for i in range(10):
            light0 = self.sensorBlockC.read_adc(self.lightPin2, gain=self.gain)
            light1 = self.sensorBlockC.read_adc(self.lightPin3, gain=self.gain)
            # Note you can also pass in an optional data_rate parameter that controls
            # the ADC conversion time (in samples/second). Each chip has a different
            # set of allowed data rate values, see datasheet Table 9 config register
            # DR bit values.
            # adc.read_adc(i, gain=GAIN, data_rate=128)
            # Each value will be a 12 or 16 bit signed integer value depending on the
            # ADC (ADS1015 = 12-bit, ADS1115 = 16-bit).
            total_light0 = total_light0 + light0
            total_light1 = total_light1 + light1
        average_light0 = float(total_light0) / float(10)
        average_light1 = float(total_light1) / float(10)

        # if sensor averages are too different, warn the user
        percent_diff = abs(average_light0 / average_light1)
        if percent_diff > 0.30:
            print('Warning: photoresistor average readings > 30% different.')

        return float(average_light0 + average_light1) / float(2)

class Block_D_Sensors(object):
    def __init__(self):
        # Create an ADS1115 ADC (16-bit) instance for the I2C address.
        self.sensorBlockD = Adafruit_ADS1x15.ADS1015(address=0x4B, busnum=1)

        # Choose a gain of 1 for reading voltages from 0 to 4.09V.
        # Pick a different gain to change the range of voltages.
        # See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
        self.gain = 1

        # SensorBlock A: Assigned Sensor Pins
        self.tempPin0  = 0
        self.tempPin1  = 1
        self.lightPin2 = 2
        self.lightPin3 = 3

    def check_raw0(self):
        return self.sensorBlockD.read_adc(self.tempPin0, gain=self.gain)

    def check_raw1(self):
        return self.sensorBlockD.read_adc(self.tempPin1, gain=self.gain)

    def check_raw2(self):
        return self.sensorBlockD.read_adc(self.lightPin2, gain=self.gain)

    def check_raw3(self):
        return self.sensorBlockD.read_adc(self.lightPin3, gain=self.gain)

    def check_temp(self):
        '''Checks the voltage output of two thermistor voltage dividers,
        and returns the average of 10 values (from each).'''
        total_temp0 = 0
        total_temp1 = 0
        for i in range(10):
            temp0 = self.sensorBlockD.read_adc(self.tempPin0, gain=self.gain)
            temp1 = self.sensorBlockD.read_adc(self.tempPin1, gain=self.gain)
            # Note you can also pass in an optional data_rate parameter that controls
            # the ADC conversion time (in samples/second). Each chip has a different
            # set of allowed data rate values, see datasheet Table 9 config register
            # DR bit values.
            # adc.read_adc(i, gain=GAIN, data_rate=128)
            # Each value will be a 12 or 16 bit signed integer value depending on the
            # ADC (ADS1015 = 12-bit, ADS1115 = 16-bit).
            total_temp0 = total_temp0 + temp0
            total_temp1 = total_temp1 + temp1
        average_temp0 = float(total_temp0) / float(10)
        average_temp1 = float(total_temp1) / float(10)

        # if sensor averages are too different, warn the user
        percent_diff = abs(average_temp0 / average_temp1)
        if percent_diff > 0.30:
            print('Warning: thermistor average readings > 30% different.')

        return float(average_temp0 + average_temp1) / float(2)

    def check_light_level(self):
        '''Checks the voltage output of two photoresistor voltage dividers,
        and returns the average of 10 values (from each).'''
        total_light0 = 0
        total_light1 = 0
        for i in range(10):
            light0 = self.sensorBlockD.read_adc(self.lightPin2, gain=self.gain)
            light1 = self.sensorBlockD.read_adc(self.lightPin3, gain=self.gain)
            # Note you can also pass in an optional data_rate parameter that controls
            # the ADC conversion time (in samples/second). Each chip has a different
            # set of allowed data rate values, see datasheet Table 9 config register
            # DR bit values.
            # adc.read_adc(i, gain=GAIN, data_rate=128)
            # Each value will be a 12 or 16 bit signed integer value depending on the
            # ADC (ADS1015 = 12-bit, ADS1115 = 16-bit).
            total_light0 = total_light0 + light0
            total_light1 = total_light1 + light1
        average_light0 = float(total_light0) / float(10)
        average_light1 = float(total_light1) / float(10)

        # if sensor averages are too different, warn the user
        percent_diff = abs(average_light0 / average_light1)
        if percent_diff > 0.30:
            print('Warning: photoresistor average readings > 30% different.')

        return float(average_light0 + average_light1) / float(2)

class PH_Sensor(object):
    def __init__(self):
        # write this
        self.pH_sensor_address = None

    def check_pH(self):
        # write this
        pass

class Water_Level_Sensor(object):
    def __init__(self):
        # write this
        self.water_level_sensor_address = None

    def check_water_level(self):
        # write this
        pass

class print_ADS1115_sensor_data(object):
    
    def blockA():
        print('Reading ADS1115 Block A values, press Ctrl-C to quit...')
        print('\n')
        A = Block_A_Sensors()
        while True:
            A_pin0 = A.check_raw0()
            A_pin1 = A.check_raw1()
            A_pin2 = A.check_raw2()
            A_pin3 = A.check_raw3()
            A_temp = A.check_temp()
            A_light = A.check_light_level()
            _ = os.system("clear")
            print('----------Block A----------'  + '\n' \
                  'Light Level: ' + str(A_light) + '\n' \
                  'Temperature: ' + str(A_temp)  + '\n' \
                  'Pin0 (Temp): ' + str(A_pin0)  + '\n' \
                  'Pin1 (Temp): ' + str(A_pin1)  + '\n' \
                  'Pin2 (Lite): ' + str(A_pin2)  + '\n' \
                  'Pin3 (Lite): ' + str(A_pin3)  + '\n')
            time.sleep(0.4)
    
    def blockB():
        print('Reading ADS1115 Block B values, press Ctrl-C to quit...')
        print('\n')
        B = Block_B_Sensors()
        while True:
            B_pin0 = B.check_raw0()
            B_pin1 = B.check_raw1()
            B_pin2 = B.check_raw2()
            B_pin3 = B.check_raw3()
            B_temp = B.check_temp()
            B_light = B.check_light_level()
            _ = os.system("clear")
            print('----------Block B----------'  + '\n' \
                  'Light Level: ' + str(B_light) + '\n' \
                  'Temperature: ' + str(B_temp)  + '\n' \
                  'Pin0 (Temp): ' + str(B_pin0)  + '\n' \
                  'Pin1 (Temp): ' + str(B_pin1)  + '\n' \
                  'Pin2 (Lite): ' + str(B_pin2)  + '\n' \
                  'Pin3 (Lite): ' + str(B_pin3)  + '\n')
            time.sleep(0.4)
    
    def blockC():
        print('Reading ADS1115 Block C values, press Ctrl-C to quit...')
        print('\n')
        C = Block_C_Sensors()
        while True:
            C_pin0 = C.check_raw0()
            C_pin1 = C.check_raw1()
            C_pin2 = C.check_raw2()
            C_pin3 = C.check_raw3()
            C_temp = C.check_temp()
            C_light = C.check_light_level()
            _ = os.system("clear")
            print('----------Block C----------'  + '\n' \
                  'Light Level: ' + str(C_light) + '\n' \
                  'Temperature: ' + str(C_temp)  + '\n' \
                  'Pin0 (Temp): ' + str(C_pin0)  + '\n' \
                  'Pin1 (Temp): ' + str(C_pin1)  + '\n' \
                  'Pin2 (Lite): ' + str(C_pin2)  + '\n' \
                  'Pin3 (Lite): ' + str(C_pin3)  + '\n')
            time.sleep(0.4)
    
    def blockD():
        print('Reading ADS1115 Block D values, press Ctrl-C to quit...')
        print('\n')
        D = Block_D_Sensors()
        while True:
            D_pin0 = D.check_raw0()
            D_pin1 = D.check_raw1()
            D_pin2 = D.check_raw2()
            D_pin3 = D.check_raw3()
            D_temp = D.check_temp()
            D_light = D.check_light_level()
            _ = os.system("clear")
            print('----------Block D----------'  + '\n' \
                  'Light Level: ' + str(D_light) + '\n' \
                  'Temperature: ' + str(D_temp)  + '\n' \
                  'Pin0 (Temp): ' + str(D_pin0)  + '\n' \
                  'Pin1 (Temp): ' + str(D_pin1)  + '\n' \
                  'Pin2 (Lite): ' + str(D_pin2)  + '\n' \
                  'Pin3 (Lite): ' + str(D_pin3)  + '\n')
            time.sleep(0.4)
