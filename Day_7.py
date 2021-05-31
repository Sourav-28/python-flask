#task-1
# a=input("Enter a string: ")
# list1=['a','e','i','o','u']
# b=a.lower()
# list2=[i for i  in range(len(b)) for j in list1 if b[i]==j]
# print(list2)

#task-2

# b=input("Enter a string: ")
# l=b.split()
# for i in l[::-1]:
#     c=i
#     print(c,end=" ")

#task-3
q=int(input("Enter how many numbers you want to enter: "))
w=[]
for i in range(q):
    a=int(input("Enter the numbers: "))
    w.append(a)
q=[]
for i in w:
    if i not in q:
        q.append(i)

print(q)