"""
You have a non-empty set , and you have to execute N commands given in N lines.
The commands will be pop, remove and discard.
"""
n=int(input())
m = input()
c = int(input())

s=set()
items = m.split(" ")
for i in items:
    s.add(int(i))
for j in range(0,c):
    d=input().split(" ")
    # print(d)
    if(d[0]=="pop"):
        s.pop()
    elif("remove" in d[0]):
        s.remove(int(d[1]))
    elif("discard" in d[0]):
        s.discard(int(d[1]))
    else:
        pass
print(sum(s))        
                     
