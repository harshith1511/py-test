def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Division by zero is not possible")
a=int(input("Enter a:"))
b=int(input("Enter b:"))
print(divide(a,b))