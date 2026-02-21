input_str = input("Enter a list of numbers with space: ")
numbers = list(map(int, input_str.split()))

print("Main list:", numbers)

unique_nums = set(numbers)
print("Unique numbers:", unique_nums)

duplicate_count = len(numbers) - len(unique_nums)
print("Duplicate count:", duplicate_count)

evens = {num for num in unique_nums if num % 2 == 0}
odds = {num for num in unique_nums if num % 2 != 0}

print("Even numbers:", evens)
print("Odd numbers:", odds)
print("Union (even | odd):", evens | odds)
print("Intersection (even & odd):", evens & odds)
print("Difference (even - odd):", evens - odds)
print("Difference (odd - even):", odds - evens)