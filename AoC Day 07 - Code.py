# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 12:13:26 2022

@author: margboz
"""

import re
import pandas as pd

test = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

test_split = test.split("\n")


dir_level = 0 # 
dir_dict = {} # The directory dictionary keeps track of the direct and indirect directories a file is in
all_files = {} # The files dictionary contains data on each file and its directories

for line in test_split: 
    if re.match("\$ cd [^\.\.]", line): # If the string matches this pattern we are adding a directory level to dir_dict
        dir_name = re.findall("(?:\$ cd )([a-z\/]+)", line)[0] # Extract the directory name
        dir_level += 1 # Add 1 to the "depth" of directories
        
        dir_dict.update({"lvl_" + str(dir_level) : dir_name}) # Add the most recent directory to the dictionary of directories

    if re.match("\$ cd ..", line): # If the string matches this pattern we are removing a directory level from dir_dict
        dir_level -= 1 # Remove 1 from the "dept" of directories
        dir_dict.popitem() # Remove the directory

    if re.match("[0-9]+ .+", line): # If the string matches this pattern  we are recording a file's information to all_files
        file_size = int(re.findall("([0-9]+)(?: .+)", line)[0]) # Extract the file size
        file_name = re.findall("(?:[0-9]+ )(.+)", line)[0] # Extract the file name
        
        file_dict = dir_dict.copy() # Copy latest dictionary of directories
        file_dict['size'] = file_size # Add size
        file_dict = {file_name: file_dict} # Turn into a file-specific nested dictionary with the file name as the key
        
        all_files.update(file_dict) # Add the file-specific dictionary to the all_files dictionary

# Combine the all_files dictionary into a DataFrame:
directory_df = pd.DataFrame.from_dict(all_files).T

# Sum directories < 100,000
columns = directory_df.columns.values.tolist()
columns.remove('size')

size_total = 0
for j in columns:
    z = directory_df.groupby([j])["size"].sum().tolist()
    size_total += sum(filter(lambda dir_total: dir_total < 100000, z))
