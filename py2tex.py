#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 20:13:25 2021

@author: bing
"""
import os

latex_dir = os.path.dirname(os.path.abspath(__file__))
code_py_dir = latex_dir + '/code/py/'

dir_names = list()
for x in os.listdir(code_py_dir):
  if os.path.isdir(code_py_dir+x) and not x.startswith('.'):
    dir_names.append(x)


for x in dir_names:
  in_file_dir = code_py_dir + x
  for y in os.listdir(in_file_dir):
    in_file = in_file_dir + '/' + y
    out_file = latex_dir + '/' + x + '/' + y + '.tex'
    print('From: ' + in_file)
    print('To: ' + out_file)
    with open(out_file, 'w') as out_file__obj:
      out_file__obj.write(r'\begin{spacing}{0.8}' + '\n')
      out_file__obj.write(r'\begin{lstlisting}[language=Python]' + '\n')
      
      line_num = 0
      for line in open(in_file, 'r'):
        line_num += 1
        out_file__obj.write('{:>3.0f}  '.format(line_num))
        out_file__obj.write(line)
      
      out_file__obj.write(r'\end{lstlisting}' + '\n')
      out_file__obj.write(r'\end{spacing}' + '\n')
    