import re

text = input("Enter the text: ")


email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,5}'

emails = re.findall(email_pattern, text)


print("\nExtracted email addresses:")
for email in emails:
    print(email)
