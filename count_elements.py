#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: teresaferreira
"""

def count(i,dic):
    
    for k in i:
        if type(k)!=list:
            dic[k]=dic.get(k,0)+1
        else:
            dic=count(k,dic)
    return dic

def rec_count(alist):
    dic=dict()
    for i in alist:
        if type(i)!=list:
            dic[i]=dic.get(i,0)+1
        else: 
            dic=count(i,dic)
            
    return dic