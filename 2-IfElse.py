#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 13:37:47 2024

@author: touaf
"""

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 == 1 :
        print('Weird')
    if (n % 2 ==0) and (2 <= n <= 5):
        print('Not Weird')
    if (n % 2 ==0) and (6 <= n <= 30):
        print('Weird')
    if (n % 2 ==0) and (20 < n):
        print('Not Weird')    