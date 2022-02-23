"""
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
Print the decimal value of each fraction on a new line with 6 places after the decimal.
"""
def plusMinus(arr):
    ps=0
    ne=0
    z=0
    a=len(arr)
    for i in arr:
        if(i<0):
            ps+=1
        elif(i>0):
            ne+=1
        elif(i==0):
            z+=1
    print("{:.6f}".format(ne/a))
    print("{:.6f}".format(ps/a))
    print("{:.6f}".format(z/a))
 if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
