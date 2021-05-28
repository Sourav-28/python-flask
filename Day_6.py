list1=[]
c=int(input("Enter how many numbers you want to append in the list: "))
for i in range(c):
    a=int(input("Enter the numbers: "))
    list1.append(a)
#task-1
print(list1)
a=0
b=0
for i in list1:
    if i%2==0:
        a+=1
    else:
        b+=1

print("Even numbers present: ",a)
print("Odd numbers present: ",b)
# print(list1)
#task-2
b=sorted(list1)
print("Minimum element in the list= ",b[0])
print("Maximum element in the list= ",b[-1])
print(list1)
# print(list1[::-1])
#task-3
if list1==list1[::-1]:
    print("YES! The list is palindrome")
else:
    print("No! The list is not palindrome")

#task-4
for i in range(c):
    n=str(list1[i])
    if n==n[::-1]:
        print("{} is a palindrome".format(n))
    else:
        print("{} is not a palindrome".format(n))



