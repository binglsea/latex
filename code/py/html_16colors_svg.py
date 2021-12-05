#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 18:24:54 2021

@author: bing
"""

#本程序文件路径: .../code/py/html_16colors_svg.py
#输入文件2路径: .../code/txt/html_16colors_en.txt
#输入文件路径: .../code/txt/html_colors.txt
#输出文件路径: .../code/svg/html_16colors.svg
in_file = __file__.replace('py', 'txt').replace('svg', 'en')
in_file2 = in_file.replace('16colors_en', 'colors')
out_file = in_file.replace('txt', 'svg').replace('_en', '')

out_file_obj = open(out_file, 'w')
# HTML 支持 141 种颜色，每行 3 种，47 行
# 小矩形 5cm x 0.45cm
# 大矩行 15cm x 21.15cm (= 3*5 x 47*0.45)
box_width = 3.7    # cm
box_height = .45  # cm
out_file_obj.write('<svg version="1.1" width="15cm" height="21.15cm"\n')
out_file_obj.write('    xmlns="http://www.w3.org/2000/svg">\n')

basic_color_names = list()
with open(in_file) as in_file_object:
  for line in in_file_object:
    words = line.split('\t')
    words = words[0].split(' ')
    basic_color_names.append(words[0].lower())

with open(in_file2) as in_file2_object:
  x, y, column = 0, 0, 0
  for line in in_file2_object:
    line = line.strip()  # 去掉回车键
    words = line.split(' ')  # 颜色列表: [英文名, 中文名, HEX 值]
    if words[0].lower() not in basic_color_names:
      continue
    if column > 3:
      column, y = 0, y + box_height
    x = box_width * column
    out_file_obj.write('<rect x="{:.2f}cm" y="{:.2f}cm" '.format(x, y))
    out_file_obj.write('width="{}cm" height=".45cm" fill="{}"'
                       .format(box_width, words[2]))
    out_file_obj.write('" />\n')
    out_file_obj.write(' <text x="{:.2f}cm" y="{:.2f}cm" '.format(x+box_width/2, y+.35))
    # 字体 10px
    out_file_obj.write(' font-size="10" text-anchor="middle" fill="black">')
    out_file_obj.write('{}</text>\n'.format(line))
    column += 1

# 深底重新配白字
out_file_obj.write('\n <text x="5.55cm" y="0.35cm"  font-size="10" text-anchor="middle" fill="white">Black 黑色 #000000</text>\n')
out_file_obj.write(' <text x="9.25cm" y="0.35cm"  font-size="10" text-anchor="middle" fill="white">Blue 蓝色 #0000FF</text>\n')
out_file_obj.write(' <text x="1.85cm" y="1.25cm"  font-size="10" text-anchor="middle" fill="white">Navy 藏青 #000080</text>\n')
out_file_obj.write(' <text x="9.25cm" y="1.25cm"  font-size="10" text-anchor="middle" fill="white">Purple 紫色 #800080</text>\n')

out_file_obj.write('</svg>')
out_file_obj.close()
