"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.
"""
def mergesort(ml):
    if(len(ml)>1):
        mid= len(ml)//2
        left=ml[:mid]
        right=ml[mid:]
        mergesort(left)
        mergesort(right)
        i=0
        j=0
        k=0
        while(i<len(left) and j<len(right)):
            if(left[i]<right[j]):
               ml[k]=left[i]
               i+=1
            else:
                ml[k]=right[j]
                j+=1
            k+=1
        while(i<len(left)):
            ml[k]=left[i]
            i+=1
            k+=1
        while(j<len(right)):
            ml[k]=right[j]
            j+=1
            k+=1
            
if __name__ == '__main__':
    n = int(input())
    data = input()
    mli=[]
    li = data.split(" ")
    for i in li:
        m=int(i)
        mli.append(m)
            
    
    mergesort(mli)
    #print(mli)
    mli.reverse()
    temp=mli[0]
    count=0
    #print(mli)
    for i in (mli[1:]):
        if(i<temp):
            temp=i
            count+=1
        if(count==1):
            break
    print(temp)        
    
   
        
    
             
        
    
