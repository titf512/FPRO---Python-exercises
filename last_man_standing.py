#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: teresaferreira
"""

def last_man_standing(alist, step):
    if len(alist) == 1:
        return alist[0]
    else:
        if step % len(alist) == 0:
            return last_man_standing(alist[:len(alist)-1],step)
        else:
            return last_man_standing(alist[(step % len(alist)):] + alist[:step % len(alist) - 1], step)