#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 09:14:56 2021

@author: teresaferreira
"""

def fib(start, end):
    lst=[]
    aa=[]
    for i in range(end):
        if i==0 or i==1:
            lst+=[1]
        else:
            a=lst[i-2]+lst[i-1]
            lst+=[a]
    for m in range(start-1,end):
        aa+=[lst[m]]
    for a in aa:
        yield a