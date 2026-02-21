h = int(input("Enter a num for Hieght : "))
while h <=0 :
    print("Error! Num must be pos.")
    h = int(input("Enter another pos Num : "))
for i in range (1 , h+1):
    for j in range(i):
        print("*",end="")
    print()