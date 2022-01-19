"""
This is a staircase of size :N=4
   #
  ##
 ###
####
Its base and height are both equal to N. It is drawn using # symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size N.
"""
import math
import os
import random
import re
import sys
def staircase(n):
    li = [" " for sp in range(0, n)]
    for i in range(1,n+1): 
        ai = li  
        for j in range(1,i+1):
            ai[-j] = '#'
        print ("".join(ai))    
if __name__ == '__main__':
    n = int(input().strip())
    staircase(n)
