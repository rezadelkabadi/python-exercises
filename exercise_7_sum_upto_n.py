num = int(input("Enter a num : "))
while num <= 0 :
    print("Eror! Num must be posetive.")
    num = int(input("Enter a posetive num : "))
total = 0
for i in range (1 , num+1):
    total += i
print("Majmoy num from 1 to",num,"is :",total)