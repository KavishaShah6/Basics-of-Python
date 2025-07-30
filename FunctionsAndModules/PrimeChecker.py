def prime (a):
    if a <=1:
         return False;
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False 
    return True

num = int(input("Enter a number: "))
if prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not prime number.")