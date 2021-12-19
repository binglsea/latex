#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 07:07:44 2021

@author: bing
"""
import numpy as np
import matplotlib.pyplot as plt
X = np.linspace(-3, 2, 200)
Y = X ** 2 - 2 * X + 1.
plt.plot(X, Y)
plt.show()