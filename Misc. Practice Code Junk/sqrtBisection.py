# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 12:01:04 2016

@author: ericgrimson
"""

x = 196
epsilon = 0.001
numGuess = 0 
lowVal = 0.0
highVal = x
ans = (lowVal + highVal)/2.0

while abs(ans**2-x) >= epsilon:
    print("Low Value: " + str(lowVal) + "High Value: " + str(highVal) + ' MidPoint = ' + str(ans))
    numGuess += 1
    if ans**2 < x:
        lowVal = ans
    else:
        highVal = ans
    ans = (highVal+lowVal)/2.0
print('numGuesses = ' + str(numGuess))
print(str(ans) + ' is close to square root of ' + str(x))