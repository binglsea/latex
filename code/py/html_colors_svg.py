#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 20:20:05 2021

@author: bing
"""

in_file = __file__
out_file = __file__.replace('py', 'txt').replace('html_', '')
out_file2 = __file__.replace(r'code/txt', 'figs/svg').replace('py', 'txt')
in_lines = None

print(in_file)
print(out_file)
"""
color_names = dict()
color_values = dict()

with open(in_file) as in_file_object:
  in_lines = in_file_object.readlines()
  
n = len(in_lines)
key = None
for i in range(n):
  line = in_lines[i].strip()
  if line.startswith('#'):
    color_values[key] = line
  else:
    words = line.split('\t')
    # print(words)
    key = words[0].strip()
    if len(words) > 1:
      color_names[key] = words[1].strip()
    if len(words) > 2:
      color_values[key] = words[2].strip()

with open(out_file, 'w') as out_file_object:
  for key in color_names.keys():
    out_file_object.write('{} {} {}\n'.format(key, color_names[key], color_values[key]))
    
"""
