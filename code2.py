print('Enter 5 element:')
l=list(map(int,input().split()))
for i in range(1,6):
    print(l[-i])
print("the sum of elements is:",sum(l))
print("the avg of elements is:",sum(l)/len(l))