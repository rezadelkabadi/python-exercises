shopping_list = []

while True:
    print("----- Menu -----")
    print("1-Add item")
    print("2-Delete item")
    print("3-Show items")
    print("4-Search item")
    print("5-Count items")
    print("6-Clear list")
    print("7-Exit")
    print("-" * 16)
    choice = input("Enter your choice: ")
    
    if choice == "1":
        item = input("Enter item name: ")
        shopping_list.append(item)
        print(f"'{item}' added to list.")
        
    elif choice == "2":
        item = input("Enter item name: ")
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"'{item}' removed from list.")
        else:
            print(f"'{item}' does not exist in list.")
            
    elif choice == "3":
        if len(shopping_list) == 0:
            print("Shopping list is empty.")
        else:
            print("\nYour shopping list:")
            for i, item in enumerate(shopping_list, 1):
                print(f"{i}. {item}")
                
    elif choice == "4":
        item = input("Enter item name: ")
        if item in shopping_list:
            index = shopping_list.index(item) + 1
            print(f"'{item}' exists in list (index {index}).")
        else:
            print(f"'{item}' does not exist in list!")
            
    elif choice == "5":
        print(f"List item count: {len(shopping_list)}")
        
    elif choice == "6":
        shopping_list.clear()
        print("Shopping list cleared.")
        
    elif choice == "7":
        print("The program has finished.")
        break
        
    else:
        print("Error! Enter a number between 1 and 7.")