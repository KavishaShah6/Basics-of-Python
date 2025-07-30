char = input("Enter a letter: ").lower()
if char in 'aeiou':
    print("Vowel")
elif char.isalpha():
    print("Consonant")
else:
    print("Not a letter")
