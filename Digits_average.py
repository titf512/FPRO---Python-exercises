#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: teresaferreira
"""

import math
def media(n):
    if(n<10):
        return 0
    else:
        a = n%10
        n = n//10 
        b = n%10
        c = math.ceil((a +b) /2)
        c += media(n)*10 
        print(c)
        return c
 
    
def digits_average(n):
    if n < 10:
        return n
    return digits_average(media(n))