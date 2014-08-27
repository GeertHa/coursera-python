# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 18:07:20 2014

@author: geert
"""

# Use the file name mbox-short.txt as the file name
counts = dict()

#fname = raw_input("Enter file name: ")

try:
    fh = open("mbox-short.txt")
except:
    print "Sorry, wrong file name."
    exit()
    
for line in fh:
    if line.find("From ") == 0:
        lst = line.split()
        for lineparts in lst:
            if lineparts.find(":") > 0:
                timeparts = lineparts.split(":")
                hour = timeparts[0]
                counts[hour] = counts.get(hour,0)+1
lsthours = list()
for key, value in counts.items():
    lsthours.append((key, value))

lsthours.sort()
for key, value in lsthours:
    print key, value