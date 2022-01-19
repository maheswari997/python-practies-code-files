"""
A counter is a container that stores elements as dictionary keys, and their counts are stored as dictionary values.
"""


i = input()
j = input()
li = j.split(" ")
li = list(map(int, li))
n=int(input())
sk=[]
# print (i)
# print (j)
# print (n)
for i in range(0,n):
    a = input().split(" ")
    items = list(map(int, a))
    size, price = items[0], items[1]
    #print (size, price)
    for j in li:   
        if(j==size):
            sk.append(price)
            # print(sk)
            li.remove(size)
            break
        else:
            pass
print (sum(sk))    
        
 
