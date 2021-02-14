#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 09:12:54 2021

@author: teresaferreira
"""

def fetch_middle(llists):
    result=[]
    for i in (llists):
        print(i)
        
        if len(i)%2!=0:
            result+=[i[len(i)//2]]
                
        else:
            a= ((i[len(i)//2-1])+(i[len(i)//2]))/2
            result+=[a]
        
    
    return result