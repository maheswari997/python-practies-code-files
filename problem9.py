"""
You are given a string S .
Your task is to print all possible size K replacement combinations of the string in lexicographic sorted order.
"""
from itertools import combinations_with_replacement
s=input().split(" ")
b=sorted(s[0])
a=sorted(list(combinations_with_replacement(b,int(s[1]))))
for i in a:
    print("".join(i))
