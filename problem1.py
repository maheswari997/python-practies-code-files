"""
Given the names and grades for each student in a class of N  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
"""

def bubblesort(m):
    if(len(m)):
        for i in range(len(m)-1):
            for j in range(len(m)-1):
                if(m[j]>m[j+1]):
                    temp=m[j]
                    m[j]=m[j+1]
                    m[j+1]=temp
        return m            
n=int(input())
ls=[]
ls1=[]
for i in range(0,n):
    name=input()
    score=float(input())
    ls.append([name,score])
    ls1.append(score)
rs=bubblesort(ls1)
#print(rs)
small=ls1[0]
count=0
for i in range(1,len(ls1)):
    if(small<ls1[i]):
        small=ls1[i]
        count+=1
    if(count==1):
        break
#print(small)
ls2=[]
for k in ls:
    #print(k)
    l=k[0]
    m=k[1]
    if(small==m):
        #print(l)
        ls2.append(l)
ls2.sort()
for k in ls2:
    print(k)