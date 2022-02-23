"""
Sam's house has an apple tree and an orange tree that yield an abundance of fruit. Using the information given below, determine the number of apples and oranges that land on Sam's house.
The red region denotes the house, where s is the start point, tand  is the endpoint. The apple tree is to the left of the house, and the orange tree is to its right.
Assume the trees are located on a single point, where the apple tree is at point a , and the orange tree is at point b .
When a fruit falls from its tree, it lands d units of distance from its tree of origin along the x -axis. *A negative value of d means the fruit fell d units to the tree's left, and a positive 
value of d means it falls d units to the tree's right. *
Apple and orange(2).png

Given the value of d for m apples and n oranges, determine how many apples and oranges will fall on Sam's house (i.e., in the inclusive range[s,t] )?

For example, Sam's house is between s=7 and t=10 . The apple tree is located at a=4  and the orange at b=12 . There are m=3 apples and n=3 oranges. Apples are thrown apples=[2,3,-4]  units distance from a , and  orang=[3,-2,-4]units
b distance. Adding each apple distance to the position of the tree, they land at [4+2,4+3,4+-4]=[6,7,0] Oranges land at[12+3,12+-2,12+-4] =[15,10,8].
One apple and two oranges land in the inclusive range 7-10 so we print
1
2
"""def countApplesAndOranges(s, t, a, b, apples, oranges):
    count=0
    ls=[]
    c1=0
    ls1=[]
    for i in apples:
        c=a+i
        ls.append(c)
    # print(ls)
    for j in ls:
        if(j>=s and j<=t):
            count+=1
        else:
            pass
    for k in oranges:
        d=b+k
        ls1.append(d)
    for l in ls1:
        if(l>=s and l<=t):
            c1+=1
        else:
            pass            
    print(count)    
    print(c1)                
    
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)

    
