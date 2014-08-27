# -*- coding: utf-8 -*-
"""
Spyder Editor

This script file is located here:
/home/geert/python
"""
hrs = raw_input("Enter hours:")
rate = raw_input("Enter your rate:")

fHrs = float(hrs)
fRate = float(rate)

if fHrs > 40:
    cost = 40*fRate + 1.5*fRate*(fHrs-40)
else:
    cost = fHrs*fRate

print cost