# -*- coding: utf-8 -*-
"""
Created on Sat Jul  5 23:09:56 2014

@author: geert
"""

text = "X-DSPAM-Confidence:    0.8475"

startNum = text.find('0')
endNum = text.find('5')+1
fNum = float(text[startNum:endNum])

print fNum