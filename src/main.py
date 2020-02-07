#!/usr/bin/env python3
import sys
import os
from sensor import print_ADS1115_sensor_data

def main(argv):
    print_ADS1115_sensor_data.blockA()

if __name__ == "__main__":
    main(sys.argv)
