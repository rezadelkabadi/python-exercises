def is_prime (n):
    if n<=1:
        return False
    elif n==2:
        return True
    elif n%2==0 :
        return False
    limit = int(n ** 0.5)
    for i in range (3, limit+1 ,2):
        if n%i == 0:
            return False
    return True

n = int(input("Enter a num : "))
result = is_prime(n)

if result== True:
    print (f"{n} is prime.")
else:
    print(f"{n} is not prime.")

