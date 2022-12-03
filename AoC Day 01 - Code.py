# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 14:12:50 2022

@author: margboz
"""
### Approach 1
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

### Approach 2

#Top elf
with open("/Users/margaritabozhinova/Desktop/AoC/Day 1 Input.txt") as f:
    top_calorie_count = 0
    calorie_count = 0
    
    for line in f:
        if line != "\n":
            calorie_count += int(line.strip("\n"))
        if line == "\n":
            if calorie_count > top_calorie_count:
                top_calorie_count = calorie_count
            calorie_count = 0
            continue
        
print(top_calorie_count)

#Top 3 elves
with open("/Users/margaritabozhinova/Desktop/AoC/Day 1 Input.txt") as f:
    first = 0
    second = 0
    third = 0
    calorie_count = 0
        
    for line in f:
        if line != "\n":
            calorie_count += int(line.strip("\n"))
            if line == "\n":
                if calorie_count > first:
                    third = second
                    second = first
                    first = calorie_count
                elif calorie_count > second:
                    third = second
                    second = calorie_count
                elif calorie_count > third:
                    third = calorie_count
                calorie_count = 0
                continue

print(sum([first, second, third]))
