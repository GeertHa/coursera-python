# -*- coding: utf-8 -*-
"""
Spyder Editor

This script file is located here:
/home/geert/python
"""
largest = None
smallest = None
while True:
score = raw_input("Enter score:")

try:
    fScore = float(score)
except:
    fScore = -1
    
if fScore < 0 or fScore > 1:
    msg = "Please enter a correct score"
elif fScore >= 0.9:
    msg = "A"
elif fScore >= 0.8:
    msg = "B"
elif fScore >= 0.7:
    msg = "C"
elif fScore >= 0.6:
    msg = "D"
elif fScore < 0.6:
    msg = "F"   

print msg