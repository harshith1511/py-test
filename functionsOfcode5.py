def average(marks):
    return sum(marks)/len(marks)
def gradeChecker(avg):
    if(avg>=90):
        return "A"
    elif(avg>=80):
        return "B"
    elif(avg>=70):
        return "C"
    elif(avg>=60):
        return "D"
    elif(avg>=50):
        return "E"
    else:
        return "F"
