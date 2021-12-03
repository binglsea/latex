#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 20:20:05 2021

@author: bing
"""

in_file = __file__.replace('py', 'txt').replace('_svg', '')
out_file = in_file.replace(r'code/txt', 'figs/svg').replace('py', 'svg')
in_lines = None

#print(in_file)
#print(out_file)
color_names = dict()
color_values = dict()

with open(in_file) as in_file_object:
  in_lines = in_file_object.readlines()
  for line in in_lines:
    words = line.split(' ')
    key = words[0].strip()
    color_names[words[0]] = words[1]
    color_values[words[0]] = words[2].strip()

print(color_names)

print(len(color_names))
with open(out_file, 'w') as out_file_object:
  for key in color_names.keys():
    out_file_object.write('{} {} {}\n'.format(key, color_names[key], color_values[key]))


