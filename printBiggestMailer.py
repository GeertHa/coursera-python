# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 18:07:20 2014

@author: geert
"""

# Use the file name mbox-short.txt as the file name
# Use words.txt as the file name
biggestMailer = None
biggestCount = 0
counts = dict()

fname = raw_input("Enter file name: ")

try:
    fh = open(fname)
except:
    print "Sorry, wrong file name."
    exit()
    
for line in fh:
    if line.find("From ") == 0:
        lst = line.split()
        email = lst[1]
        counts[email] = counts.get(email,0)+1        

for key, value in counts.items():
    if value > biggestCount:
        biggestCount = value
        biggestMailer = key
        
print biggestMailer + " " + str(biggestCount)