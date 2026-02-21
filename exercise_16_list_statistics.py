def analyze_numbers(numbers):
    count = len(numbers)
    total = sum(numbers)
    average = total / count
    maximum = max(numbers)
    minimum = min(numbers)
    return {
        "count": count,
        "sum": total,
        "average": average,
        "max": maximum,
        "min": minimum
    }

num_list = []
while True:
    user_input = input("Enter a number (or 'done' to stop): ")
    if user_input == "done":
        break
    if user_input.isdigit() or (user_input[0] == '-' and user_input[1:].isdigit()):
        num = int(user_input)
        num_list.append(num)
    else:
        print("Error! Enter a valid integer.")

if len(num_list) == 0:
    print("List is empty.")
else:
    result = analyze_numbers(num_list)
    print("\nResult of analysis:")
    print(f"Count of numbers: {result['count']}")
    print(f"Sum of numbers: {result['sum']}")
    print(f"Average of numbers: {result['average']}")
    print(f"Maximum: {result['max']}")
    print(f"Minimum: {result['min']}")