#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: teresaferreira
"""
def  biggest_member(atuple):
    result=[]
    for i in atuple:
        if type(i)!=tuple:
            result.append(atuple)
        else:
            result.append(biggest_member(i))
    return sorted(result, key=lambda x: len(x))[-1]


