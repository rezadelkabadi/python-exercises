input1 = input("Enter your first input : ")
input2 = input("Enter your second input : ")

if input1.isdigit():
    v1 = int(input1)
else :
    v1 = input1
if input2.isdigit():
    v2 = int(input2)
else :
    v2 = input2
    
print("first Type : " , type(v1))
print("second Type : " , type(v2))

if type(v1) == int and type(v2) == int :
    print(f"Majmoy : {v1+v2}")
    print(f"Tafrigh : {v1-v2}")
    print(f"Zarb : {v1*v2}")
    if v2 != 0:
        print(f"Majmoy : {v1//v2}")
    else:
        print("Taghsim dose not exist!")
elif type(v1) == str and type(v2) == str :
    print(f"Conected str : {v1+v2}")
    print(f"Num of char : {len(v1+v2)}")
else :
    print("They have different type!")
