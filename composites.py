#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: teresaferreira
"""

def primes(numero):
    lista=[]
    
    divisores = 0
    for divisor in range(1, numero):
        if numero % divisor == 0:
            divisores = divisores + 1
            if divisores > 1:
                break
    if divisores > 1:
        return[]
    else:
        lista+=[numero]
        return lista
  

  
def get_composites(n) :
    lista=[]
    for i in range(4,n+1):
        lista+=primes(i)
    final=(x for x in range(4,n+1) if x not in lista)
    return final