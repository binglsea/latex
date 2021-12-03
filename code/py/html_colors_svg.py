#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 20:20:05 2021

@author: bing
"""

in_file = __file__.replace('py', 'txt').replace('_svg', '')
out_file = in_file.replace(r'txt', 'svg').replace('code', 'figs')
in_lines = None

color_names = dict()
color_values = dict()

out_file_obj = open(out_file, 'w')
out_file_obj.write('<svg version="1.1" width="16cm" height="24cm"\n')
#out_file_obj.write('    width="300" height="200"\n')
out_file_obj.write('    xmlns="http://www.w3.org/2000/svg">\n')

box_height = 1
#box_width = 

with open(in_file) as in_file_object:
  y = 1 
  for line in in_file_object:
    words = line.split(' ')
    out_file_obj.write('<rect x="5" y="')
    out_file_obj.write(str(y))
    y += 1
    out_file_obj.write(r'cm" ')
    out_file_obj.write('width="5cm" height="1cm" fill="')
    out_file_obj.write(words[2].strip())
    out_file_obj.write('" />\n')



  
out_file_obj.write(r'</svg>')
out_file_obj.close()
