from functionsOfcode5 import average, gradeChecker

marks=list(map(int,input("Enter marks of student:").split()))
avg=average(marks)
print("the avg is",avg)
print("the grade is",gradeChecker(avg))
