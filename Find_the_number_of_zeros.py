#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: teresaferreira
"""

def pos(alist):
   
    upper=len(alist)
    lower=0
    while True:
        i=(upper+lower)//2
        if alist[i-1]==1 and alist[i]==0:
            return i
        if alist[i-1]==1:
            lower=i
        else:
            upper=i


def count_zeros(f):
    alist=f()
    i=pos(alist)
    return len(alist[i:])