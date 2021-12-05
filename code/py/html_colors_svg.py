#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 20:20:05 2021

@author: bing
"""
#本程序文件路径: .../code/py/html_colors_svg.py
#输入文件路径: .../code/txt/html_colors.txt
#输出文件路径: .../code/svg/html_colors.svg
in_file = __file__.replace('py', 'txt').replace('_svg', '')
out_file = in_file.replace('txt', 'svg')

out_file_obj = open(out_file, 'w')
# HTML 支持 141 种颜色，每行 3 种，47 行
# 小矩形 5cm x 0.45cm
# 大矩行 15cm x 21.15cm (= 3*5 x 47*0.45)
box_height = .45  #cm
out_file_obj.write('<svg version="1.1" width="15cm" height="21.15cm"\n')
out_file_obj.write('    xmlns="http://www.w3.org/2000/svg">\n')

with open(in_file) as in_file_object:
  x, y, column = 0, 0, 0
  for line in in_file_object:
    line = line.strip()  # 去掉回车键
    words = line.split(' ')  # 颜色列表: [英文名, 中文名, HEX 值]
    if column > 2:
      column, y = 0, y + box_height
    x = 5 * column
    out_file_obj.write('<rect x="{}cm" y="{:.2f}cm" '.format(x, y))
    out_file_obj.write('width="5cm" height=".45cm" fill="{}"'.format(words[0]))
    out_file_obj.write(' />\n')
    out_file_obj.write(' <text x="{}cm" y="{:.2f}cm" '.format(x+2.5, y+.35))
    # 字体 10px
    out_file_obj.write(' font-size="10" text-anchor="middle" fill="black">')
    out_file_obj.write('{}</text>\n'.format(line))
    column += 1

# 深底重新配白字
out_file_obj.write(' <text x="7.5cm" y="1.25cm"  font-size="10" text-anchor="middle" fill="white">Black 黑色 #000000</text>')
out_file_obj.write(' <text x="2.5cm" y="3.5cm"  font-size="10" text-anchor="middle" fill="white">DarkBlue 暗蓝 #00008B</text>')
out_file_obj.write(' <text x="12.5cm" y="8.45cm"  font-size="10" text-anchor="middle" fill="white">Indigo 靛色 #4B0082</text>')
out_file_obj.write('<text x="7.5cm" y="12.50cm"  font-size="10" text-anchor="middle" fill="white">MediumBlue 中蓝色 #0000CD</text>')
out_file_obj.write(' <text x="2.5cm" y="13.85cm"  font-size="10" text-anchor="middle" fill="white">MidnightBlue 午夜蓝 #191970</text>')
out_file_obj.write(' <text x="12.5cm" y="14.3cm"  font-size="10" text-anchor="middle" fill="white">Navy 藏青 #000080</text>')

out_file_obj.write('</svg>')
out_file_obj.close()
