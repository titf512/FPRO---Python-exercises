#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: teresaferreira
"""

def number_of_collisions(objects):
    count=0
    for i in objects:
        for j in objects[objects.index(i)+1:]:
            if i["x2"]<j["x1"] or i["x1"]>j["x2"]:
                count =count
            elif i["y2"]<j["y1"] or i["y1"]>j["y2"]:
                count=count
            else:
                count+=1

    return count