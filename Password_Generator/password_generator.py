import random
import string

print("=" * 30)
print("      PASSWORD GENERATOR")
print("=" * 30)

length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""
for i in range(length):
    password += random.choice(characters)

print("\nYour Generated Password is:")
print(password)

print("\nThank you for using Password Generator!")
