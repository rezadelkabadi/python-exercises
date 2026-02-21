analyze_couant = 0

def advance_analyze(numbers,calc_median=False):
    global analyze_couant
    analyze_couant += 1
    count = len(numbers)
    total = sum(numbers)
    avarage = total / count
    max_v1 = max(numbers)
    min_v1 = min(numbers)
    
    result = {
        "count": count,
        "sum": total,
        "avarage": avarage,
        "max": max_v1,
        "min": min_v1
    }
    if calc_median:
        sorted_nums = sorted(numbers)
        if count % 2 == 1:
            median = sorted_nums[count // 2]
        else:
            median = (sorted_nums[count // 2 -1]+sorted_nums[count // 2])/2
        result["median"] = median
        
    return result    
    
num_list = []
while True:
    user_input = input("Enter a num ( or 'done' to stop): ")
    if user_input == "done":
        break
    if user_input.isdigit() or (user_input[0] == '-' and user_input[1:].isdigit()):
        num = int(user_input)
        num_list.append(num)
    else:
        print("Error! Enter an int num or 'done'.")
    
if  len(num_list) == 0:
        print("List is empty.")
            
else :
        result1 = advance_analyze(num_list,calc_median=False)
        print("\n--- Analyze without median ---")
        print(f"Count: {result1['count']}")
        print(f"Sum: {result1['sum']}")
        print(f"Avarage: {result1['avarage']}")
        print(f"Max: {result1['max']}")
        print(f"Min: {result1['min']}")
        
        result2 = advance_analyze(num_list,calc_median=True)
        print("\n--- Analyze with median ---")
        print(f"Count: {result2['count']}")
        print(f"Sum: {result2['sum']}")
        print(f"Avarage: {result2['avarage']}")
        print(f"Max: {result2['max']}")
        print(f"Min: {result2['min']}")
        print(f"Median: {result2['median']}")
        
        print(f"\nTotal analyze performed: {analyze_couant}")
            
            