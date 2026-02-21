text = input("Enter a Text : ")

cleaned_text = text.strip()
print(f"\nCleared text : '{cleaned_text}'")

words = cleaned_text.split()
word_count = len(words)
print(f"Words count : '{word_count}'")

letter_count = 0
for char in cleaned_text:
    if char.isalpha():
        letter_count+= 1
print(f"Letter count : '{letter_count}'")

reversed_text = cleaned_text[::-1]
print(f"Reversed text : '{reversed_text}'")

if cleaned_text.startswith("hello"):
    print("Is text start with \" hello \" ? Yes")
else:
    print("Is text start with \" hello \" ? No")
    
letter = input("Enter a letter to search : ")
if len(letter)==1:
    cout_letter = cleaned_text.count(letter)
    print(f"Count of '{letter}' in text is '{cout_letter}'")
else:
    print(f"Please enter a letter.")