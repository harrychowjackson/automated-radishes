EESchema Schematic File Version 2
LIBS:radPi-rescue
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
LIBS:devs
LIBS:relays
LIBS:radPi-cache
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 2 3
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L ADS1115 U3
U 1 1 59B29154
P 6250 1950
F 0 "U3" H 6400 1250 60  0000 C CNN
F 1 "ADS1115" H 6250 1350 60  0000 C CNN
F 2 "Connectors_Terminal_Blocks:TerminalBlock_Pheonix_MPT-2.54mm_10pol" H 6250 2050 60  0001 C CNN
F 3 "" H 6250 2050 60  0001 C CNN
	1    6250 1950
	1    0    0    -1  
$EndComp
$Comp
L ADS1115 U4
U 1 1 59B29192
P 6250 3250
F 0 "U4" H 6400 2550 60  0000 C CNN
F 1 "ADS1115" H 6250 2650 60  0000 C CNN
F 2 "Connectors_Terminal_Blocks:TerminalBlock_Pheonix_MPT-2.54mm_10pol" H 6250 3350 60  0001 C CNN
F 3 "" H 6250 3350 60  0001 C CNN
	1    6250 3250
	1    0    0    -1  
$EndComp
$Comp
L ADS1115 U5
U 1 1 59B291B4
P 6250 4550
F 0 "U5" H 6400 3850 60  0000 C CNN
F 1 "ADS1115" H 6250 3950 60  0000 C CNN
F 2 "Connectors_Terminal_Blocks:TerminalBlock_Pheonix_MPT-2.54mm_10pol" H 6250 4650 60  0001 C CNN
F 3 "" H 6250 4650 60  0001 C CNN
	1    6250 4550
	1    0    0    -1  
$EndComp
$Comp
L ADS1115 U2
U 1 1 59B29207
P 6200 5850
F 0 "U2" H 6350 5150 60  0000 C CNN
F 1 "ADS1115" H 6200 5250 60  0000 C CNN
F 2 "Connectors_Terminal_Blocks:TerminalBlock_Pheonix_MPT-2.54mm_10pol" H 6200 5950 60  0001 C CNN
F 3 "" H 6200 5950 60  0001 C CNN
	1    6200 5850
	1    0    0    -1  
$EndComp
Text HLabel 4400 1500 0    60   UnSpc ~ 0
VDD
Wire Wire Line
	4600 2800 5800 2800
Wire Wire Line
	4600 4100 5800 4100
Wire Wire Line
	4600 5400 5750 5400
Wire Wire Line
	4400 1500 5800 1500
Wire Wire Line
	4600 1500 4600 5400
Connection ~ 4600 1500
Connection ~ 4600 2800
Connection ~ 4600 4100
$Comp
L GND #PWR07
U 1 1 59B29CD3
P 5150 1650
F 0 "#PWR07" H 5150 1400 50  0001 C CNN
F 1 "GND" H 5150 1500 50  0000 C CNN
F 2 "" H 5150 1650 50  0000 C CNN
F 3 "" H 5150 1650 50  0000 C CNN
	1    5150 1650
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR08
U 1 1 59B29D2D
P 5200 2950
F 0 "#PWR08" H 5200 2700 50  0001 C CNN
F 1 "GND" H 5200 2800 50  0000 C CNN
F 2 "" H 5200 2950 50  0000 C CNN
F 3 "" H 5200 2950 50  0000 C CNN
	1    5200 2950
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR09
U 1 1 59B29D44
P 5250 4250
F 0 "#PWR09" H 5250 4000 50  0001 C CNN
F 1 "GND" H 5250 4100 50  0000 C CNN
F 2 "" H 5250 4250 50  0000 C CNN
F 3 "" H 5250 4250 50  0000 C CNN
	1    5250 4250
	1    0    0    -1  
$EndComp
$Comp
L GND #PWR010
U 1 1 59B29DB3
P 5250 5550
F 0 "#PWR010" H 5250 5300 50  0001 C CNN
F 1 "GND" H 5250 5400 50  0000 C CNN
F 2 "" H 5250 5550 50  0000 C CNN
F 3 "" H 5250 5550 50  0000 C CNN
	1    5250 5550
	1    0    0    -1  
$EndComp
Wire Wire Line
	5250 5550 5250 5500
Wire Wire Line
	5250 5500 5750 5500
Wire Wire Line
	5250 4250 5250 4200
Wire Wire Line
	5250 4200 5800 4200
Wire Wire Line
	5200 2950 5200 2900
Wire Wire Line
	5200 2900 5800 2900
Wire Wire Line
	5150 1650 5150 1600
Wire Wire Line
	5150 1600 5800 1600
Text HLabel 5700 1700 0    60   Input ~ 0
SCLK
Wire Wire Line
	5700 1700 5800 1700
Text HLabel 5700 3000 0    60   Input ~ 0
SCLK
Wire Wire Line
	5700 3000 5800 3000
Text HLabel 5650 4300 0    60   Input ~ 0
SCLK
Wire Wire Line
	5650 4300 5800 4300
Text HLabel 5650 5600 0    60   Input ~ 0
SCLK
Wire Wire Line
	5650 5600 5750 5600
Text HLabel 5700 1800 0    60   BiDi ~ 0
SDA
Wire Wire Line
	5700 1800 5800 1800
Text HLabel 5700 3100 0    60   BiDi ~ 0
SDA
Wire Wire Line
	5700 3100 5800 3100
Text HLabel 5650 4400 0    60   BiDi ~ 0
SDA
Wire Wire Line
	5650 4400 5800 4400
Text HLabel 5650 5700 0    60   BiDi ~ 0
SDA
Wire Wire Line
	5650 5700 5750 5700
Wire Wire Line
	4600 3200 5800 3200
Text HLabel 5750 3300 0    60   Output ~ 0
ALERT
Wire Wire Line
	5800 3300 5750 3300
$Comp
L CONN_01X04 P2
U 1 1 59B2AE3D
P 5100 3550
F 0 "P2" H 5250 3400 50  0000 C CNN
F 1 "CONN_01X04" H 5300 3300 50  0000 C CNN
F 2 "Connectors_Terminal_Blocks:TerminalBlock_Pheonix_MPT-2.54mm_4pol" H 5100 3550 50  0001 C CNN
F 3 "" H 5100 3550 50  0000 C CNN
	1    5100 3550
	-1   0    0    1   
$EndComp
Wire Wire Line
	5300 3400 5800 3400
Wire Wire Line
	5800 3500 5300 3500
Wire Wire Line
	5300 3600 5800 3600
Wire Wire Line
	5300 3700 5800 3700
Text HLabel 5750 2000 0    60   Output ~ 0
ALERT
Wire Wire Line
	5750 2000 5800 2000
$Comp
L CONN_01X04 P1
U 1 1 59B2B108
P 5100 2250
F 0 "P1" H 5250 2100 50  0000 C CNN
F 1 "CONN_01X04" H 5300 2000 50  0000 C CNN
F 2 "Connectors_Terminal_Blocks:TerminalBlock_Pheonix_MPT-2.54mm_4pol" H 5100 2250 50  0001 C CNN
F 3 "" H 5100 2250 50  0000 C CNN
	1    5100 2250
	-1   0    0    1   
$EndComp
$Comp
L CONN_01X04 P3
U 1 1 59B2B15A
P 5100 4850
F 0 "P3" H 5250 4700 50  0000 C CNN
F 1 "CONN_01X04" H 5300 4600 50  0000 C CNN
F 2 "Connectors_Terminal_Blocks:TerminalBlock_Pheonix_MPT-2.54mm_4pol" H 5100 4850 50  0001 C CNN
F 3 "" H 5100 4850 50  0000 C CNN
	1    5100 4850
	-1   0    0    1   
$EndComp
$Comp
L CONN_01X04 P4
U 1 1 59B2B315
P 5100 6150
F 0 "P4" H 5250 6000 50  0000 C CNN
F 1 "CONN_01X04" H 5300 5900 50  0000 C CNN
F 2 "Connectors_Terminal_Blocks:TerminalBlock_Pheonix_MPT-2.54mm_4pol" H 5100 6150 50  0001 C CNN
F 3 "" H 5100 6150 50  0000 C CNN
	1    5100 6150
	-1   0    0    1   
$EndComp
Wire Wire Line
	5300 6300 5750 6300
Wire Wire Line
	5300 6200 5750 6200
Wire Wire Line
	5750 6100 5300 6100
Wire Wire Line
	5300 6000 5750 6000
Wire Wire Line
	5300 5000 5800 5000
Wire Wire Line
	5300 4900 5800 4900
Wire Wire Line
	5800 4800 5300 4800
Wire Wire Line
	5300 4700 5800 4700
Wire Wire Line
	5800 2100 5300 2100
Wire Wire Line
	5300 2200 5800 2200
Wire Wire Line
	5800 2300 5300 2300
Wire Wire Line
	5300 2400 5800 2400
Text HLabel 5750 4600 0    60   Output ~ 0
ALERT
Text HLabel 5700 5900 0    60   Output ~ 0
ALERT
Wire Wire Line
	5750 5900 5700 5900
Wire Wire Line
	5800 4600 5750 4600
Text Notes 6550 1550 0    60   ~ 0
Address 0x48 (1001000)
Text Notes 6550 2850 0    60   ~ 0
Address 0x49 (1001001)
Text Notes 6550 4150 0    60   ~ 0
Address 0x4A (1001010)
Text Notes 6500 5450 0    60   ~ 0
Address 0x4B (1001011)
Wire Wire Line
	5800 1900 5300 1900
Wire Wire Line
	5300 1900 5300 1600
Connection ~ 5300 1600
Connection ~ 4600 3200
Wire Wire Line
	5750 5800 5700 5800
Wire Wire Line
	5700 5800 5700 5600
Connection ~ 5700 5600
Wire Wire Line
	5800 4500 5750 4500
Wire Wire Line
	5750 4500 5750 4400
Connection ~ 5750 4400
$EndSCHEMATC
