import re

email = input()

# Basic email pattern: [word characters/dots/hyphens]@[domain].[extension]
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

if re.match(pattern, email):
    print("Valid")
else:
    print("Invalid")
