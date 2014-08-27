# -*- coding: utf-8 -*-
"""
Spyder Editor

This script file is located here:
/home/geert/python
"""
def computepay(h,r):
    if h > 40:
       cost = 40*r + 1.5*r*(h-40)
    else:
       cost = h*r
    return cost

hrs = raw_input("Enter Hours:")
rate = raw_input("Enter Rate:")
p = computepay(float(hrs),float(rate))
print p
