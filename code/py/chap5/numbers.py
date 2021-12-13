#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 07:07:44 2021

@author: bing
"""
from numpy import arange
from numpy import array

a = arange(2, 12).reshape(2,5)
print(a)
print(3*a)
print(a.dtype)
print(a[1,:])