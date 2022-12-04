#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 08:49:22 2022

@author: margaritabozhinova
"""

lists_az = [chr(x) for x in [*range(ord('a'), ord('z')+1)]] + [chr(x) for x in [*range(ord('A'), ord('Z')+1)]]

priority_dict = dict(zip(lists_az, range(1, 53)))

# Part 1

priorities_sum = 0

with open("/Users/margaritabozhinova/Desktop/AoC/Day 3 Input.txt") as f:
    for line in f:
        first_half = set(line[:int(len(line.strip("\n"))/2)])
        second_half = set(line[int(len(line.strip("\n"))/2):])
        intersection = first_half.intersection(second_half)
        priorities_sum += priority_dict[list(intersection)[0]]
        
# Part 2
priorities_sum = 0

with open("/Users/margaritabozhinova/Desktop/AoC/Day 3 Input.txt") as f:
    rucksacks = f.readlines()
    for i in range(0, len(rucksacks), 3):
        first_rucksack = set(rucksacks[i].strip("\n"))
        second_rucksack = set(rucksacks[i+1].strip("\n"))
        third_rucksack = set(rucksacks[i+2].strip("\n"))
        intersection = first_rucksack & second_rucksack & third_rucksack
        priorities_sum += priority_dict[list(intersection)[0]]
