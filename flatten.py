#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: teresaferreira
"""

def flatten(alist):

    if alist == []:
        return alist
    if type(alist[0])==list:
        return flatten(alist[0]) + flatten(alist[1:])
    return alist[:1] + flatten(alist[1:])