"""
HackerLand University has the following grading policy:

Every student receives a grade  in the inclusive range from  0 to 100 .
Any grade  less than grade 40 is a failing grade.
Sam is a professor at the university and likes to round each student's grade according to these rules:

If the difference between the grade  and the next multiple of 5 is less than 3, round grade  up to the next multiple of .
If the value of grade is less than38 , no rounding occurs as the result will still be a failing grade
"""
def gradingStudents(grades):
    result = []
    for i in grades:
        m=i-i%5
        k=m+5
        if(i<38):
            print(i)
            result.append(i)
        elif(k-i<3):
            print(k)
            result.append(k)
        elif(k-i>=3):
            print(i)
            result.append(i)  
          
        else:
            pass
    return result
                    
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for i in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

    
    
    
    

    
