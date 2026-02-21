Num = int(input("Enter a num : "))
while Num<=1 :
    print("Error! Num must be bigger than 1.")
    Num=int(input("Enter another Nam: "))
is_prime = True
for i in range (2,Num):
    if Num % i == 0:
        is_prime = False
        break
if is_prime == True:
    print(f"{Num} is prime")
else:
    print(f"{Num} is not prime!!")
