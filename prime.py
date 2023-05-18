"""Prime number"""
n = int(input("Enter a number :"))

if n <= 0:
    print("Enter positive number")
elif n == 1:
    print("1 is not prime ")
else:
    for i in range(2, (n/2)+1):
        if n % i == 0:
            print("Given number not prime")
        else:
            print("Given number is prime")
