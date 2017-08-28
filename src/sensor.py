import os
import sys

class PH_Sensor(object):
	def __init__(self):
		self.motor_address0 = 0
		self.motor_address1 = 1
		self.motor_address2 = 2
		self.motor_address3 = 3
		self.motor_address4 = 4

	def check_pH(self):
		# write this
		pass

class Temp_Sensor(object):
	def __init__(self):
		self.temp_sensor_address0 = 0
		self.temp_sensor_address1 = 1

	def check_temp(self):
		# write this
		pass

	def average_temps(self):
		# write this
		pass

class Light_Sensor(object):
	def __init__(self):
		self.light_sensor_address0 = 0
		self.light_sensor_address1 = 1

	def check_light_level(self):
		# write this
		pass

	def average_light_levels(self):
		# write this
		pass

class Water_Level_Sensor
	def __init__(self):
		self.water_level_sensor_address0 = 0

	def check_water_level(self):
		# write this
		pass