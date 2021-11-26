#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 25 10:59:19 2021

@author: bing
"""
a4_width_mm = 210
a4_height_mm = 297

letter_width_in = 8.5
letter_height_in = 11

inch_to_mm = 25.4

print("A4 纸张的尺寸是 {} 毫米 × {} 毫米,".format(
    a4_width_mm, a4_height_mm))
print("  或 {} 英寸 x {} 英寸。".format(
    a4_width_mm/inch_to_mm, a4_height_mm/inch_to_mm))
print("  约 {:2.2f} 英寸 x {:2.2f} 英寸。".format(
    a4_width_mm/inch_to_mm, a4_height_mm/inch_to_mm))

print("美国信纸的尺寸是 {} 英寸 × {} 英寸,".format(
    letter_width_in, letter_height_in))
print("  或 {} 毫米 x {} 毫米。".format(
    letter_width_in * inch_to_mm, letter_height_in * inch_to_mm))
print("  约 {:3.1f} 毫米 x {:3.1f} 毫米。".format(
    letter_width_in * inch_to_mm, letter_height_in * inch_to_mm))

#%% 
from math import sqrt
print("√2 = ", sqrt(2))
print("2 的平方根 = ", 2**.5)

#%% A系列纸张的理论尺寸
w = 1_000 / 2**.25  # 下划线"_"分隔仅为阅读方便，无实际编程作用
h = 1_000 * 2**.25  # 2**.25是2的4次方根即2的0.25次幂
print("A系列纸张的理论尺寸:")
for i in range(0, 11):
    # {:>3} 表示 3 个字符向右看齐。宽高四舍五入到整数
    print("{:>3}: {:3.0f}毫米 x {:4.0f}毫米".format('A'+str(i), w, h),
          end='  ')
    # {:6.2f}: 包括小数点，浮点数展示 6 个字符向右看齐，小数点后面保留 2 位数
    print(" {:6.2f}毫米 x {:7.2f}毫米".format(w, h), end='  ')
    # 用 int() 丢弃小数部分，宽高仅保留整数部分
    print("   {:3.0f}毫米 x {:4.0f}毫米".format(int(w), int(h)))
    tmp = w   #暂存原宽度备作下一个高度
    w = h/2   #新宽度为原高度的一半
    h = tmp   #新高度为原宽度

