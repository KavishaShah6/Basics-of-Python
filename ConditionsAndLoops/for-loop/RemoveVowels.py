text=str(input("Enter any paragraph: "))

for char in text :
    if char not in 'aeiou':
        print (char, end='')