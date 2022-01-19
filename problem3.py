"""
Initialize your list and read in the  n value of  followed by n lines of commands where each command will be of the 7 types listed above. Iterate through each command in order and perform the corresponding operation on your list.
"""
if __name__ == '__main__':
    N = int(input())
    inls=[]
    for i in range(0,N):
        d=input().split(" ")
       if(d[0]=="insert"):
            inls.insert(int(d[1]),int(d[2]))
            #print(inls)
        elif("remove"== d[0]):
            inls.remove(int(d[1]))
        elif("append" == d[0]):
            inls.append(int(d[1]))
        elif("sort" == d[0]):
            inls.sort() 
        elif("print" == d[0]):
            print(inls)
        elif("pop" == d[0]):
            inls.pop()
        elif("reverse" in d[0]):
            inls.reverse()
        else:
            pass        
                               
            
