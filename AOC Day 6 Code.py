#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 20:50:38 2022

@author: margaritabozhinova
"""

with open("/Users/margaritabozhinova/Desktop/AoC/Day 6 Input.txt") as f:
    buffer = f.read()

nbr_distinct = 4 # or 19 for part 2

for i in range(0, len(buffer)-nbr_distinct):
    if len(set(buffer[i:i+nbr_distinct])) == nbr_distinct:
        print(i+nbr_distinct)
        break

        

