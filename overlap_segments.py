#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 09:14:10 2021

@author: teresaferreira
"""

def overlaps(segments):
    lst=[]
    sett=set()
    for i in range(len(segments)):
        a=[x for x in range(segments[i][0],segments[i][1]+1)]
        lst+=[a]
    for k in range(len(lst)):
        for m in range(k+1,len(lst)):
            for element in lst[k]:
                if element in lst[m]:
                    comum=element
                    b=(k,m)
                    sett.add(b)
    return sett