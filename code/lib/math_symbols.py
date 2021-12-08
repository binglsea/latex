#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 10:28:35 2021

@author: bing


http://www.unicode.org/charts/
"""
#%%
"""

数学符号的统一码（Unicode）是从哪里
"""
for i in range(1, 128):
    print(chr(i))
    

#%%

print(str(ord('"')) + ": " + "\"")
print(str(ord('"')) + ": " + "\"")
print('\u201C数学\u201D')
print('\u2230')

#%%

j = 0
for i in range(ord('\u2200'), ord('\u22FF') + 1):
    j += 1
    if j%10 == 0:
        print('')
    print(chr(i), sep=' ', end=' ')

print(0x2200)


#%%
print(12/0)
