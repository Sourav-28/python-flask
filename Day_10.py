def num(n):
    if n<=0:
        print(n,end=" ")
        return
    print(n, end=" ")
    num(n-5)
    print(n,end=" ")

n=int(input("Enter the value: "))
num(n)
