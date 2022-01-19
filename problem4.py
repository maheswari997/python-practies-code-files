"""
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.
"""



if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        name,*line= input().split()
        #print(name,line)
        scores = list(map(float, line))
        # student_marks[name] = scores
        sum=float(0)
        for j in scores:
            sum=sum+j
            
        student_marks[name] = '{:.2f}'.format(sum/len(scores))
    query_name = input()
    print(student_marks[query_name])
    
            
        
