# -*- coding: utf-8 -*-
"""
Created on Thu Jul 10 18:07:20 2014

@author: geert
"""

# Use the file name mbox-short.txt as the file name
# Use words.txt as the file name
lst = list()
flst = list()

fname = raw_input("Enter file name: ")

try:
    fh = open(fname)
except:
    print "Sorry, wrong file name."
    exit()
    
for line in fh:
    lst = lst + line.split()
    flst.append('ok')
    
lst = list(set(lst))
lst.sort()
print lst