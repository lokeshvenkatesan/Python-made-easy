# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kJaHSZMRu_oSTASVepXRv26ZbadEKPIL
"""

FACTORIAL

def fact(n):
  if n==0:
   return 1
  small= fact(n-1)
  return n * small

n= int(input())
print(sum_n(n))
print(fact(n))

summation of n= n + summation (n -1 )

def sum_n(n):
  if (n==0):
    return 0
  assumption = sum_n(n -1)
  output = n + assumption
  return output