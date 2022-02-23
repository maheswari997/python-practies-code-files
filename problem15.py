"""Given an array of integers, find the sum of its elements.
For example , if the arrayar=[1,2,3] ,1+2+3 = 6 , so return 6.
"""
def simpleArraySum(ar):
    sum=0
    for i in ar:
        sum+=i
    return sum
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()