#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 07:27:22 2021

@author: bing
"""

y = [x**2 for x in range(1, 21)]
print (y)
z = any (x%3 == 0 for x in y)
print(z)
