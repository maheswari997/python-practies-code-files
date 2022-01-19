"""
Let's learn about list comprehensions! You are given three integers x,y and z  representing the dimensions of a cuboid along with an integer n . Print a list of all possible coordinates given by(x,y,z) on a 3D grid where the sum of x+y+z is not equal to n. Here,0<=i<=x;0<=j<=y;0<=k<=z . Please use list comprehensions rather than multiple loops, as a learning exercise.
"""
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    ls=[[p,q,r] for p in range(x+1) for q in range(y+1) for r in range(z+1)]
    ouput = []
    for i in ls:
        if sum(i) != n:
            ouput.append(i)
    print(ouput)   
