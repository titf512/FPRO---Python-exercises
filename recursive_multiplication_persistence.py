#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: teresaferreira
"""

def mult(n):
    if n//10<10:
        return (n%10)*(n//10)
    else:
        return (n%10)*mult(n//10)

def rec_multiplicative_persistence(n):
    if mult(n)<10:
        count=1
        return count
    else:
        count=1
        return rec_multiplicative_persistence(mult(n))+ count
