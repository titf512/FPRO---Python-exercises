#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: teresaferreira
"""

from math import sqrt
def comprehensions(i, j):
    lista1=[x for x in range(i,j+1) if x%10==3 or x%10== 8]
    tup2=tuple([round(sqrt(x),2) for x in range(i,j+1)])
    ter={x:chr(x) for x in range(i,j+1)}
    return(lista1,tup2,ter)