# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 17:58:03 2014

@author: geert
"""

# Use words.txt as the file name
fname = raw_input("Enter file name: ")

try:
    fh = open(fname)
except:
    print "Sorry, wrong file name."
    exit()
    
wordsTxt = fh.read()
print wordsTxt.upper().rstrip()
