# task1.py

# ✅ Tuple Example (Fixed list of fruits)
fruits = ("apple", "banana", "cherry")
print("Fruits in the tuple:")
for fruit in fruits:
    print("-", fruit)

# ✅ Dictionary Example (User info)
user = {
    "name": "Simran",
    "email": "simran@example.com",
    "phone": "1234567890"
}

print("\nUser details from dictionary:")
for key, value in user.items():
    print(key, ":", value)

# ✅ Set Example (Numbers with duplicates)
nums = {1, 2, 2, 3, 4, 4}
print("\nNumbers in the set (duplicates removed):")
print(nums)
