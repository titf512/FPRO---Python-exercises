#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 09:15:34 2021

@author: teresaferreira
"""

def  sum_dicts(lst):
    dic=dict()
    for i in lst:
        for key,value in i.items():
            dic[key]=dic.get(key,0)+value
    return dic    