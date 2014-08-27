# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 18:07:20 2014

@author: geert
"""

# Use the file name mbox-short.txt as the file name
# Use words.txt as the file name
nbrEmail = 0

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
        print email
        nbrEmail = nbrEmail + 1
        
print "There were " + str(nbrEmail) + " lines in the file with From as the first word"