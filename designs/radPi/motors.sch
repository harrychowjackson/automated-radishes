EESchema Schematic File Version 4
LIBS:radPi-cache
EELAYER 26 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 3 3
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
L radPi-rescue:LEMO2-RESCUE-radPi K?
U 1 1 59B32C2E
P 3950 1950
AR Path="/59B32C2E" Ref="K?"  Part="1" 
AR Path="/59B326C6/59B32C2E" Ref="K1"  Part="1" 
F 0 "K1" H 3950 2150 50  0000 C CNN
F 1 "LEMO2" H 3950 1750 50  0000 C CNN
F 2 "" H 3950 1950 50  0001 C CNN
F 3 "" H 3950 1950 50  0000 C CNN
	1    3950 1950
	0    -1   -1   0   
$EndComp
$Comp
L power:GND #PWR011
U 1 1 59B32CBE
P 3750 2200
F 0 "#PWR011" H 3750 1950 50  0001 C CNN
F 1 "GND" H 3750 2050 50  0000 C CNN
F 2 "" H 3750 2200 50  0000 C CNN
F 3 "" H 3750 2200 50  0000 C CNN
	1    3750 2200
	1    0    0    -1  
$EndComp
$Comp
L power:+12V #PWR012
U 1 1 59B32CE4
P 4200 2250
F 0 "#PWR012" H 4200 2100 50  0001 C CNN
F 1 "+12V" H 4200 2390 50  0000 C CNN
F 2 "" H 4200 2250 50  0000 C CNN
F 3 "" H 4200 2250 50  0000 C CNN
	1    4200 2250
	1    0    0    -1  
$EndComp
$Comp
L relays:G6DN_Relay SW1
U 1 1 59B5F092
P 3250 3050
F 0 "SW1" H 3750 2600 60  0000 C CNN
F 1 "G6DN_Relay" H 3550 2700 60  0000 C CNN
F 2 "" H 3000 3050 60  0001 C CNN
F 3 "" H 3000 3050 60  0001 C CNN
	1    3250 3050
	1    0    0    -1  
$EndComp
$Comp
L radPi-rescue:D D1
U 1 1 59B5F17D
P 2200 3050
F 0 "D1" H 2200 3150 50  0000 C CNN
F 1 "D" H 2200 2950 50  0000 C CNN
F 2 "Diodes_THT:D_5KPW_P12.70mm_Horizontal" H 2200 3050 50  0001 C CNN
F 3 "" H 2200 3050 50  0000 C CNN
	1    2200 3050
	0    1    1    0   
$EndComp
Text HLabel 1100 3300 0    60   UnSpc ~ 0
PUMP_IN
$Comp
L radPi-rescue:C C3
U 1 1 59B60A7A
P 4500 3450
F 0 "C3" H 4525 3550 50  0000 L CNN
F 1 "100pF" H 4525 3350 50  0000 L CNN
F 2 "Capacitors_THT:C_Axial_L12.0mm_D6.5mm_P15.00mm_Horizontal" H 4538 3300 50  0001 C CNN
F 3 "" H 4500 3450 50  0000 C CNN
	1    4500 3450
	1    0    0    -1  
$EndComp
$Comp
L radPi-rescue:CP C2
U 1 1 59B60AE8
P 4250 2750
F 0 "C2" H 4275 2850 50  0000 L CNN
F 1 "CP" H 4275 2650 50  0000 L CNN
F 2 "Capacitors_THT:CP_Axial_L18.0mm_D10.0mm_P25.00mm_Horizontal" H 4288 2600 50  0001 C CNN
F 3 "" H 4250 2750 50  0000 C CNN
	1    4250 2750
	1    0    0    -1  
$EndComp
$Comp
L radPi-rescue:CONN_01X02 P5
U 1 1 59B60C39
P 5150 3450
F 0 "P5" H 5150 3600 50  0000 C CNN
F 1 "PUMP_OUT" H 5300 3700 50  0000 C CNN
F 2 "" H 5150 3450 50  0001 C CNN
F 3 "" H 5150 3450 50  0000 C CNN
	1    5150 3450
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR013
U 1 1 59B610C8
P 2200 3650
F 0 "#PWR013" H 2200 3400 50  0001 C CNN
F 1 "GND" H 2200 3500 50  0000 C CNN
F 2 "" H 2200 3650 50  0000 C CNN
F 3 "" H 2200 3650 50  0000 C CNN
	1    2200 3650
	1    0    0    -1  
$EndComp
$Comp
L radPi-rescue:LED D2
U 1 1 59B616E3
P 4250 4000
F 0 "D2" H 4250 4100 50  0000 C CNN
F 1 "LED" H 4250 3900 50  0000 C CNN
F 2 "LEDs:LED_D5.0mm" H 4250 4000 50  0001 C CNN
F 3 "" H 4250 4000 50  0000 C CNN
	1    4250 4000
	0    -1   -1   0   
$EndComp
$Comp
L radPi-rescue:R R2
U 1 1 59B618AA
P 4250 3550
F 0 "R2" V 4330 3550 50  0000 C CNN
F 1 "100" V 4250 3550 50  0000 C CNN
F 2 "Resistors_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal" V 4180 3550 50  0001 C CNN
F 3 "" H 4250 3550 50  0000 C CNN
	1    4250 3550
	1    0    0    -1  
$EndComp
$Comp
L power:GNDD #PWR014
U 1 1 59B62B40
P 4250 2950
F 0 "#PWR014" H 4250 2700 50  0001 C CNN
F 1 "GNDD" H 4250 2800 50  0000 C CNN
F 2 "" H 4250 2950 50  0000 C CNN
F 3 "" H 4250 2950 50  0000 C CNN
	1    4250 2950
	1    0    0    -1  
$EndComp
$Comp
L power:GNDD #PWR015
U 1 1 59B62B9D
P 3350 4150
F 0 "#PWR015" H 3350 3900 50  0001 C CNN
F 1 "GNDD" H 3350 4000 50  0000 C CNN
F 2 "" H 3350 4150 50  0000 C CNN
F 3 "" H 3350 4150 50  0000 C CNN
	1    3350 4150
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR016
U 1 1 59B62C20
P 3050 4150
F 0 "#PWR016" H 3050 3900 50  0001 C CNN
F 1 "GND" H 3050 4000 50  0000 C CNN
F 2 "" H 3050 4150 50  0000 C CNN
F 3 "" H 3050 4150 50  0000 C CNN
	1    3050 4150
	1    0    0    -1  
$EndComp
$Comp
L radPi-rescue:L L1
U 1 1 59B62C45
P 3200 4100
F 0 "L1" V 3150 4100 50  0000 C CNN
F 1 "L" V 3275 4100 50  0000 C CNN
F 2 "Inductors_THT:L_Axial_L9.5mm_D4.0mm_P12.70mm_Horizontal_Fastron_SMCC" H 3200 4100 50  0001 C CNN
F 3 "" H 3200 4100 50  0000 C CNN
	1    3200 4100
	0    -1   -1   0   
$EndComp
$Comp
L radPi-rescue:R R1
U 1 1 59B5F2DD
P 1350 3300
F 0 "R1" V 1430 3300 50  0000 C CNN
F 1 "R" V 1350 3300 50  0000 C CNN
F 2 "Resistors_THT:R_Axial_DIN0204_L3.6mm_D1.6mm_P5.08mm_Horizontal" V 1280 3300 50  0001 C CNN
F 3 "" H 1350 3300 50  0000 C CNN
	1    1350 3300
	0    1    1    0   
$EndComp
$Comp
L radPi-rescue:BC556 Q1
U 1 1 59B65C2E
P 1700 3300
F 0 "Q1" H 1900 3375 50  0000 L CNN
F 1 "BC556" H 1900 3300 50  0000 L CNN
F 2 "TO-92" H 1900 3225 50  0000 L CIN
F 3 "" H 1700 3300 50  0000 L CNN
	1    1700 3300
	1    0    0    -1  
$EndComp
$Comp
L radPi-rescue:D D3
U 1 1 59B65D7A
P 4750 3450
F 0 "D3" H 4750 3550 50  0000 C CNN
F 1 "D" H 4750 3350 50  0000 C CNN
F 2 "Diodes_THT:D_5KPW_P12.70mm_Horizontal" H 4750 3450 50  0001 C CNN
F 3 "" H 4750 3450 50  0000 C CNN
	1    4750 3450
	0    1    1    0   
$EndComp
Wire Wire Line
	1800 2900 2500 2900
Connection ~ 2200 2900
Connection ~ 2200 3200
Wire Wire Line
	1100 3300 1200 3300
Wire Wire Line
	3900 2300 3850 2300
Wire Wire Line
	3850 2300 3850 2200
Wire Wire Line
	3850 2200 3750 2200
Wire Wire Line
	3950 3200 4950 3200
Connection ~ 4000 3200
Connection ~ 4250 3200
Wire Wire Line
	4200 2250 4200 2300
Wire Wire Line
	4200 2300 4000 2300
Wire Wire Line
	4250 3850 4250 3700
Wire Wire Line
	4250 4150 4250 4250
Wire Wire Line
	3350 4150 3350 4100
Wire Wire Line
	3050 4150 3050 4100
Wire Wire Line
	4250 3200 4250 3400
Wire Wire Line
	2500 3200 2200 3200
Wire Wire Line
	2200 3200 2200 3650
Wire Wire Line
	1800 2900 1800 3100
Wire Wire Line
	4500 3200 4500 3300
Wire Wire Line
	4950 3700 4950 3500
Wire Wire Line
	4950 3200 4950 3400
Connection ~ 4500 3200
Wire Wire Line
	4500 3700 4950 3700
Wire Wire Line
	4500 3700 4500 3600
Wire Wire Line
	4750 3300 4750 3200
Connection ~ 4750 3200
Wire Wire Line
	4750 3600 4750 3700
Connection ~ 4750 3700
Wire Wire Line
	1800 3500 1800 3650
Wire Wire Line
	1800 3650 2200 3650
Wire Wire Line
	1500 3300 1500 3300
Wire Wire Line
	4000 2900 3950 2900
Wire Wire Line
	4000 2300 4000 2900
Wire Wire Line
	4250 2600 4000 2600
Connection ~ 4000 2600
Wire Wire Line
	4250 2950 4250 2900
$Comp
L power:GNDD #PWR017
U 1 1 59B6663B
P 4250 4250
F 0 "#PWR017" H 4250 4000 50  0001 C CNN
F 1 "GNDD" H 4250 4100 50  0000 C CNN
F 2 "" H 4250 4250 50  0000 C CNN
F 3 "" H 4250 4250 50  0000 C CNN
	1    4250 4250
	1    0    0    -1  
$EndComp
$Comp
L radPi-rescue:CP C1
U 1 1 59B71339
P 2450 3050
F 0 "C1" H 2475 3150 50  0000 L CNN
F 1 "CP" H 2475 2950 50  0000 L CNN
F 2 "Capacitors_THT:CP_Axial_L18.0mm_D10.0mm_P25.00mm_Horizontal" H 2488 2900 50  0001 C CNN
F 3 "" H 2450 3050 50  0000 C CNN
	1    2450 3050
	1    0    0    -1  
$EndComp
Connection ~ 2450 3200
Connection ~ 2450 2900
$EndSCHEMATC
