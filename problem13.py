"""
Given an array of integers, where all elements but one occur twice, find the unique element.
"""
def lonelyinteger(a):
    ls=[]
    di = {}
    for i in a:
        if i in di:
            di[i] = di[i] + 1
        else:
            di[i] = 1
    
    for k,v in di.items():
        if v == 1:
            return k
    return None
 if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
