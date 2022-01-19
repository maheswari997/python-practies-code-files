"""
The defaultdict tool is a container in the collections class of Python. It's similar to the usual dictionary (dict) container, but the only difference is that a defaultdict will have a default value if that key has not been set yet. If you didn't use a defaultdict you'd have to check to see if that key exists, and if it doesn't, set it to what you want.
"""
n,m=list(map(int,input().split(" ")))
ls1=[]
ls2=[]
for i in range(1,n+1):
    n1=input()
    ls1.append(n1)

for j in range(1,m+1):
    m1=input()
    ls2.append(m1)

for k in ls2:
    l=[i for i in range(1, len(ls1)+1) if ls1[i-1] == k]
    if (len(l)==0):
        print("-1")
    else:
        g=map(str,l)
        print(" ".join(g)) 