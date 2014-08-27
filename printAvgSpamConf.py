# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 18:07:20 2014

@author: geert
"""

# Use the file name mbox-short.txt as the file name
# Use words.txt as the file name
nbrLines = 0
fNum = 0.0
totNum = 0.0

fname = raw_input("Enter file name: ")

try:
    fh = open(fname)
except:
    print "Sorry, wrong file name."
    exit()
    
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    startNum = line.find('0')
    endNum = line.find('"')
    fNum = float(line[startNum:endNum])
    totNum = totNum + fNum
    nbrLines = nbrLines + 1
    
print "Average spam confidence: " + str(totNum/nbrLines)
