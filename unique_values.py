#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: teresaferreira
"""

def unique_values(alist):
    final=set()
    for i in alist:
        if type(i)==dict:
            for key, value in i.items():
                final.add(value)
    return final

