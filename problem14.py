"""Given a square matrix, calculate the absolute difference between the sums of its diagonals.
For example, the square matrix arr is shown below:
1 2 3
4 5 6
9 8 9  
The left-to-right diagonal = 1+5+9 = 15 . The right to left diagonal = 3+5+9 = 17 . Their absolute difference is |15-17| = 2.
"""
def diagonalDifference(arr):
    sum_=0
    for i in range(0,n):
        for j in range(0,n):
            if(i==j):
                sum_+=arr[i][j]
    i=0
    j=len(arr) - 1
    sum1_=0
    while(i <= len(arr) -1 and j >= 0):
        sum1_+=arr[i][j]
        i+=1
        j-=1
    return abs(sum_ - sum1_)
 if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
	arr = []
	for i in range(n):
        arr.append(list(map(int, input().rstrip().split())))
	result = diagonalDifference(arr)
	fptr.write(str(result) + '\n')
	fptr.close()
