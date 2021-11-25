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
print("  约 {:2.1f} 英寸 x {:2.1f} 英寸。".format(
    a4_width_mm/inch_to_mm, a4_height_mm/inch_to_mm))

print("美国信纸的尺寸是 {} 英寸 × {} 英寸,".format(
    letter_width_in, letter_height_in))
print("  或 {} 毫米 x {} 毫米。".format(
    letter_width_in * inch_to_mm, letter_height_in * inch_to_mm))
print("  约 {:3.0f} 毫米 x {:3.0f} 毫米。".format(
    letter_width_in * inch_to_mm, letter_height_in * inch_to_mm))
