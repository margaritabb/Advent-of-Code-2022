# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 16:39:50 2022

@author: margboz
"""

# Part 1

score = 0

with open("//fld5filer/iofdim/Sections/CSA/15 Staff folders/Margarita/Python/AoC/AoC Day 2 - Input.txt") as f:
    for line in f:
        curr_line = line.strip("\n").split(" ")
        if curr_line[1] == 'X':
            score += 1
            if curr_line[0] == 'A':
                score += 3
            if curr_line[0] == 'C':
                score += 6
        if curr_line[1] == 'Y':
            score +=2 
            if curr_line[0] == 'A':
                score +=6
            if curr_line[0] == 'B':
                score += 3
        if curr_line[1] == 'Z':
            score += 3
            if curr_line[0] == 'B':
                score += 6
            if curr_line[0] == 'C':
                score += 3

print(score)

# Part 2
score = 0

with open("//fld5filer/iofdim/Sections/CSA/15 Staff folders/Margarita/Python/AoC/AoC Day 2 - Input.txt") as f:
    for line in f:
        curr_line = line.strip("\n").split(" ")
        if curr_line[1] == 'X':
            score += 0
            if curr_line[0] == 'A':
                score += 3
            if curr_line[0] == 'B':
                score += 1
            if curr_line[0] == 'C':
                score += 2
        if curr_line[1] == 'Y':
            score +=3
            if curr_line[0] == 'A':
                score += 1
            if curr_line[0] == 'B':
                score += 2
            if curr_line[0] == 'C':
                score += 3
        if curr_line[1] == 'Z':
            score += 6
            if curr_line[0] == 'A':
                score += 2
            if curr_line[0] == 'B':
                score += 3
            if curr_line[0] == 'C':
                score += 1
                
print(score)
