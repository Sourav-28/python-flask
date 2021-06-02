# def factorial(n):
#     s=1
#     if n==0:
#         print(0)
#
#     elif n==1:
#         print(1)
#     else:
#         for i in range(1,n+1):
#             s=s*i
#         print(s)
#
# a=int(input("Enter the number: "))
# factorial(a)

def prime(n):
    if n==1 or n==0:
        print(f"Number {n} is not prime")
    elif n==2:
        print(f"Number {n} is prime")
    else:
        for i in range(2,n):
            if n%i==0:
                print(f"Number {n} is not a prime number")
                break
        else:
            print(f"Number {n} is a prime number")

a=int(input("Enter the number: "))
prime(a)