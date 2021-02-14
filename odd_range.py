#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: teresaferreira
"""

def odd_range(start, stop, step):
    oi=[x for x in range(start,stop) if x%2!=0]
    x=0
    while x<len(oi):
        yield oi[x]
        x=x+step