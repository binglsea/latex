#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 07:07:44 2021

@author: bing
"""
for i in range(0x03b1, 0x03c9):
  print(hex(i), chr(i), ' ' , chr(i).encode('utf-8'), ' ', '{0:b}'.format(i))