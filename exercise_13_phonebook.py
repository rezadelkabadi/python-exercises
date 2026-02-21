phonebook = {}
while True:
    print("-"*7,"Menu","-"*7)
    print("1- Add contact")
    print("2- Search contact")
    print("3- Edit contact")
    print("4- Delete contact")
    print("5- Show all contact")
    print("6- Show contact count")
    print("7- Exit")
    print("-"*20)
    
    choice =input("Enter your choice : ")
    
    if choice == "1":
        Name = input("Enter Name : ")
        num = input("Enter Number : ")
        phonebook[Name] = num
        print(f"contact '{Name}' added.")
    elif choice == "2":
        Name = input("Enter name to search: ")
        if Name in phonebook:
            print (f"{Name}: {phonebook[Name]}")
        else:
            print(f"Contact '{Name}' dose not exist.")
    elif choice == "3":
        Name = input("Enter name to edit : ")
        if Name in phonebook:
            new_num = input("Enter new num : ")
            phonebook[Name] = new_num
            print(f"Contact '{Name}' updated.")
        else:
            print(f"Contact '{Name}' Dose not exist.")
    elif choice == "4":
        Name = input("Enter name to delete : ")
        if Name in phonebook:
            del phonebook[Name]
            print(f"Contact '{Name}' Deleted.")
        else:
            print(f"Contact '{Name}' does not exist.")
    elif choice == "5":
        if len(phonebook) == 0:
            print("Phonebook is empty.")
        else:
            print("\nAll contact (sorted):")
            for Name in sorted(phonebook.keys()):
                print(f"{Name} : {phonebook[Name]}")
    elif choice == "6":
        print(f"Total contact: {len(phonebook)}")
    elif choice == "7":
        print("Progrram has finished.")
        break
    else:
        print("Error! Enter a num between 1 and 7.")