#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 13:59:25 2024

@author: touaf
"""

def is_leap(year):
    leap = False
    
#    if ((year % 4 == 0 or year % 100 == 0) and year % 400 == 0):

    if (year % 4 == 0 and year % 100 == 0 and year % 400 == 0) :
        leap = True
    elif (year % 4 == 0 and year % 100 != 0) :
        leap = True
    else : 
        pass
    return leap

year = int(input())
print(is_leap(year))