def rectan_proper(a,b):
    Masahat = a*b
    Mohit = (a+b) *2
    return Masahat, Mohit

arz = int(input("Enter a num for arz : "))
tol = int(input("Enter a num for tol : "))
Masahat , Mohit = rectan_proper(arz,tol)
print(f"Masahat : {Masahat}")
print(f"Mohit : {Mohit}")