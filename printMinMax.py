# -*- coding: utf-8 -*-
"""
Spyder Editor

This script file is located here:
/home/geert/python
"""
first = True

while True:
    num = raw_input("Enter number:")
    if num == "done" : break
 
    try:
        iNum = int(num)
    except:
        msg = "Invalid input"
        print msg
        continue
    
    if first:
        largest = iNum
        smallest = iNum
        first = False
    else:
        if iNum > largest:
            largest = iNum
        elif iNum < smallest:
            smallest = iNum

print "Maximum is", largest
print "Minimum is", smallest
