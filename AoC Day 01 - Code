# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 14:12:50 2022

@author: margboz
"""

#Import input file
with open("//fld5filer/iofdim/Sections/CSA/15 Staff folders/Margarita/Python/AoC/AoC Day 1 - Input.txt") as f:
    elf = f.read()

#Split among elves
elf_split = elf.split("\n\n")

#Split within each elf and cast to integer
elf_ints = [[int(y) if y != '' else 0 for y in x.split("\n")] for x in elf_split]

#Sum within elf
elf_sums = [sum(x) for x in elf_ints]

#Top elf
print(max(elf_sums))

#Top 3 elves
print(sum(sorted(elf_sums, reverse = True)[:3]))
