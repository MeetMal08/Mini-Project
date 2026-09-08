# Python Email Slicer 

email = input("Enter Your Email: ")

index = email.index("@")

username = email[:index]
domain = email[index + 1:]

print(f"Username: {username}")
print(f"Domain: {domain}")
