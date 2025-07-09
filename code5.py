from functionsOfcode5 import average, gradeChecker
name=input("Enter your name:")
marks=list(map(int,input("Enter marks of student:").split()))
avg=average(marks)
print("Marks:",marks)
print("the avg is",avg)
print("the grade is",gradeChecker(avg))
